/**
 * StorageService.js
 * Offline-first persistence for workout history, daily streaks, and user preferences.
 */

import AsyncStorage from '@react-native-async-storage/async-storage';

const STORAGE_KEYS = {
    WORKOUT_HISTORY: '@yoga_tracker_history_v1',
    USER_STATS: '@yoga_tracker_stats_v1',
    SETTINGS: '@yoga_tracker_settings_v1',
};

class StorageService {
    /**
     * Records a completed workout session and recalculates streaks and cumulative stats.
     */
    async saveSession({ title, durationSec, accuracyScore, posesCount }) {
        try {
            const history = await this.getHistory();
            const newRecord = {
                id: `sess_${Date.now()}`,
                title: title || 'Yoga Practice',
                durationSec: durationSec || 0,
                accuracyScore: Math.round(accuracyScore || 0),
                posesCount: posesCount || 1,
                date: new Date().toISOString(),
            };

            const updatedHistory = [newRecord, ...history].slice(0, 50); // Keep last 50
            await AsyncStorage.setItem(STORAGE_KEYS.WORKOUT_HISTORY, JSON.stringify(updatedHistory));

            // Update stats
            await this.updateStats(newRecord, updatedHistory);
            return newRecord;
        } catch (e) {
            console.warn('[StorageService] Error saving session:', e);
            return null;
        }
    }

    async getHistory() {
        try {
            const raw = await AsyncStorage.getItem(STORAGE_KEYS.WORKOUT_HISTORY);
            return raw ? JSON.parse(raw) : [];
        } catch (e) {
            console.warn('[StorageService] Error reading history:', e);
            return [];
        }
    }

    async updateStats(latestRecord, allHistory) {
        try {
            let totalMinutes = 0;
            let totalAcc = 0;
            const uniqueDates = new Set();

            for (const item of allHistory) {
                totalMinutes += Math.round((item.durationSec || 0) / 60);
                totalAcc += (item.accuracyScore || 0);
                const dayStr = item.date ? item.date.split('T')[0] : '';
                if (dayStr) uniqueDates.add(dayStr);
            }

            const totalSessions = allHistory.length;
            const avgAccuracy = totalSessions > 0 ? Math.round(totalAcc / totalSessions) : 0;

            // Calculate streak (consecutive days ending today or yesterday)
            const streak = this.calculateStreak(uniqueDates);

            const stats = {
                totalSessions,
                totalMinutes,
                avgAccuracy,
                streak,
                lastWorkoutDate: latestRecord.date,
            };

            await AsyncStorage.setItem(STORAGE_KEYS.USER_STATS, JSON.stringify(stats));
            return stats;
        } catch (e) {
            console.warn('[StorageService] Error updating stats:', e);
            return null;
        }
    }

    calculateStreak(uniqueDateStringsSet) {
        let currentStreak = 0;
        let checkDate = new Date();

        while (true) {
            const dateStr = checkDate.toISOString().split('T')[0];
            if (uniqueDateStringsSet.has(dateStr)) {
                currentStreak++;
                // Check previous day
                checkDate.setDate(checkDate.getDate() - 1);
            } else {
                // If today hasn't had a workout yet, check if yesterday had one to maintain active streak
                if (currentStreak === 0) {
                    checkDate.setDate(checkDate.getDate() - 1);
                    const yesterdayStr = checkDate.toISOString().split('T')[0];
                    if (uniqueDateStringsSet.has(yesterdayStr)) {
                        currentStreak++;
                        checkDate.setDate(checkDate.getDate() - 1);
                        continue;
                    }
                }
                break;
            }
        }
        return currentStreak;
    }

    async getStats() {
        try {
            const raw = await AsyncStorage.getItem(STORAGE_KEYS.USER_STATS);
            if (raw) return JSON.parse(raw);
            return {
                totalSessions: 0,
                totalMinutes: 0,
                avgAccuracy: 0,
                streak: 0,
            };
        } catch (e) {
            return { totalSessions: 0, totalMinutes: 0, avgAccuracy: 0, streak: 0 };
        }
    }
}

export default new StorageService();
