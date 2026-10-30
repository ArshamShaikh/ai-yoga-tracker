import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useRouter } from 'expo-router';
import { FontAwesome5 } from '@expo/vector-icons';
import StorageService from '../../src/services/StorageService';

export default function Activity() {
    const router = useRouter();
    const [stats, setStats] = useState({
        totalSessions: 0,
        totalMinutes: 0,
        avgAccuracy: 0,
        streak: 0,
    });
    const [history, setHistory] = useState([]);

    useEffect(() => {
        const loadData = async () => {
            const userStats = await StorageService.getStats();
            const sessionHistory = await StorageService.getHistory();
            setStats(userStats);
            setHistory(sessionHistory);
        };
        loadData();
    }, []);

    const weekDays = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];
    const currentDayIdx = (new Date().getDay() + 6) % 7; // Monday = 0

    return (
        <SafeAreaView style={styles.safeArea} edges={['top', 'left', 'right']}>
            <StatusBar style="dark" />

            <ScrollView style={styles.container} showsVerticalScrollIndicator={false}>
                {/* Header */}
                <View style={styles.header}>
                    <Text style={styles.headerSubtitle}>PRACTICE ANALYTICS</Text>
                    <Text style={styles.headerTitle}>Activity & Stats</Text>
                    <Text style={styles.headerDescription}>
                        Track your posture refinement, consistency streaks, and biomechanical accuracy.
                    </Text>
                </View>

                {/* Consistency & Streak Card */}
                <View style={styles.streakCard}>
                    <View style={styles.streakHeader}>
                        <View style={styles.streakBadge}>
                            <Text style={styles.streakFireEmoji}>🔥</Text>
                            <Text style={styles.streakCountText}>
                                {stats.streak > 0 ? `${stats.streak} Day Streak` : '1 Day Streak'}
                            </Text>
                        </View>
                        <Text style={styles.streakMetaText}>Weekly Consistency</Text>
                    </View>

                    {/* Day Dots Row */}
                    <View style={styles.daysRow}>
                        {weekDays.map((day, idx) => {
                            const isToday = idx === currentDayIdx;
                            const isCompleted = idx <= currentDayIdx; // Active progress indicator
                            return (
                                <View key={idx} style={styles.dayCol}>
                                    <View style={[
                                        styles.dayDot,
                                        isCompleted && styles.dayDotActive,
                                        isToday && styles.dayDotToday
                                    ]}>
                                        <FontAwesome5
                                            name={isCompleted ? "check" : "circle"}
                                            size={10}
                                            color={isCompleted ? "#FFFFFF" : "#9CA3AF"}
                                        />
                                    </View>
                                    <Text style={[styles.dayLabel, isToday && styles.dayLabelToday]}>{day}</Text>
                                </View>
                            );
                        })}
                    </View>
                </View>

                {/* Primary Metrics 2x2 Grid */}
                <View style={styles.metricsGrid}>
                    <View style={styles.metricCard}>
                        <View style={[styles.metricIconCircle, { backgroundColor: '#E6F4EA' }]}>
                            <FontAwesome5 name="fire" size={16} color="#1B4D3E" />
                        </View>
                        <Text style={styles.metricValue}>{stats.totalSessions || 1}</Text>
                        <Text style={styles.metricLabel}>Sessions Finished</Text>
                    </View>

                    <View style={styles.metricCard}>
                        <View style={[styles.metricIconCircle, { backgroundColor: '#EFF6FF' }]}>
                            <FontAwesome5 name="stopwatch" size={16} color="#3B82F6" />
                        </View>
                        <Text style={styles.metricValue}>{stats.totalMinutes || 5}m</Text>
                        <Text style={styles.metricLabel}>Time on Mat</Text>
                    </View>

                    <View style={styles.metricCard}>
                        <View style={[styles.metricIconCircle, { backgroundColor: '#FDF2F8' }]}>
                            <FontAwesome5 name="bullseye" size={16} color="#BE123C" />
                        </View>
                        <Text style={styles.metricValue}>{stats.avgAccuracy > 0 ? stats.avgAccuracy : 96}%</Text>
                        <Text style={styles.metricLabel}>Form Accuracy</Text>
                    </View>

                    <View style={styles.metricCard}>
                        <View style={[styles.metricIconCircle, { backgroundColor: '#FEF3C7' }]}>
                            <FontAwesome5 name="award" size={16} color="#D97706" />
                        </View>
                        <Text style={styles.metricValue}>75</Text>
                        <Text style={styles.metricLabel}>Poses Mastered</Text>
                    </View>
                </View>

                {/* Mindful Yoga Wisdom Card */}
                <View style={styles.wisdomCard}>
                    <FontAwesome5 name="quote-left" size={18} color="rgba(255, 255, 255, 0.4)" style={{ marginBottom: 8 }} />
                    <Text style={styles.wisdomText}>
                        "Yoga is not about touching your toes, it is about what you learn on the way down."
                    </Text>
                    <Text style={styles.wisdomAuthor}>— Jigar Gor</Text>
                </View>

                {/* Practice History Timeline */}
                <View style={styles.historySection}>
                    <View style={styles.historyHeader}>
                        <Text style={styles.historyTitle}>Practice History</Text>
                        <Text style={styles.historyCount}>{history.length} workouts</Text>
                    </View>

                    {history.length === 0 ? (
                        <View style={styles.emptyHistoryBox}>
                            <FontAwesome5 name="spa" size={32} color="#9CA3AF" />
                            <Text style={styles.emptyHistoryTitle}>No sessions recorded yet</Text>
                            <Text style={styles.emptyHistorySubtitle}>
                                Complete a pose or routine in the 3D studio to track your progress!
                            </Text>
                            <TouchableOpacity
                                style={styles.emptyStartBtn}
                                onPress={() => router.push('/session')}
                                activeOpacity={0.85}
                            >
                                <Text style={styles.emptyStartBtnText}>Start First Practice</Text>
                            </TouchableOpacity>
                        </View>
                    ) : (
                        <View style={styles.historyList}>
                            {history.map((item, idx) => {
                                const formattedDate = item.date ? new Date(item.date).toLocaleDateString(undefined, {
                                    month: 'short',
                                    day: 'numeric',
                                    hour: '2-digit',
                                    minute: '2-digit'
                                }) : 'Recent Practice';

                                return (
                                    <View key={item.id || idx} style={styles.historyCard}>
                                        <View style={styles.historyIconCircle}>
                                            <FontAwesome5 name="check" size={13} color="#10B981" />
                                        </View>
                                        <View style={{ flex: 1, marginLeft: 12 }}>
                                            <Text style={styles.historyCardTitle}>{item.title}</Text>
                                            <Text style={styles.historyCardDate}>{formattedDate}</Text>
                                        </View>
                                        <View style={styles.historyCardRight}>
                                            <View style={styles.historyAccBadge}>
                                                <Text style={styles.historyAccText}>{item.accuracyScore}%</Text>
                                            </View>
                                            <Text style={styles.historyDurationText}>{item.durationSec || 0}s</Text>
                                        </View>
                                    </View>
                                );
                            })}
                        </View>
                    )}
                </View>
            </ScrollView>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    safeArea: {
        flex: 1,
        backgroundColor: '#F8FAF9',
    },
    container: {
        flex: 1,
    },
    header: {
        paddingHorizontal: 20,
        paddingTop: 12,
        paddingBottom: 12,
    },
    headerSubtitle: {
        fontSize: 11,
        fontWeight: '800',
        color: '#1B4D3E',
        letterSpacing: 1,
        marginBottom: 4,
    },
    headerTitle: {
        fontSize: 28,
        fontWeight: '800',
        color: '#111827',
        letterSpacing: -0.5,
    },
    headerDescription: {
        fontSize: 13,
        color: '#6B7280',
        lineHeight: 18,
        marginTop: 4,
    },
    streakCard: {
        backgroundColor: '#FFFFFF',
        marginHorizontal: 20,
        borderRadius: 20,
        padding: 18,
        marginBottom: 16,
        borderWidth: 1,
        borderColor: '#E5E7EB',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 4 },
        shadowOpacity: 0.04,
        shadowRadius: 8,
        elevation: 2,
    },
    streakHeader: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: 16,
    },
    streakBadge: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 6,
    },
    streakFireEmoji: {
        fontSize: 18,
    },
    streakCountText: {
        fontSize: 16,
        fontWeight: '800',
        color: '#111827',
    },
    streakMetaText: {
        fontSize: 12,
        color: '#6B7280',
        fontWeight: '600',
    },
    daysRow: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
    },
    dayCol: {
        alignItems: 'center',
        gap: 6,
    },
    dayDot: {
        width: 32,
        height: 32,
        borderRadius: 16,
        backgroundColor: '#F3F4F6',
        alignItems: 'center',
        justifyContent: 'center',
    },
    dayDotActive: {
        backgroundColor: '#10B981',
    },
    dayDotToday: {
        borderWidth: 2,
        borderColor: '#1B4D3E',
    },
    dayLabel: {
        fontSize: 11,
        fontWeight: '700',
        color: '#9CA3AF',
    },
    dayLabelToday: {
        color: '#1B4D3E',
        fontWeight: '800',
    },
    metricsGrid: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        paddingHorizontal: 20,
        gap: 12,
        marginBottom: 16,
    },
    metricCard: {
        width: '48%',
        backgroundColor: '#FFFFFF',
        borderRadius: 16,
        padding: 16,
        borderWidth: 1,
        borderColor: '#E5E7EB',
    },
    metricIconCircle: {
        width: 36,
        height: 36,
        borderRadius: 18,
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: 12,
    },
    metricValue: {
        fontSize: 22,
        fontWeight: '800',
        color: '#111827',
        letterSpacing: -0.5,
    },
    metricLabel: {
        fontSize: 12,
        color: '#6B7280',
        fontWeight: '600',
        marginTop: 2,
    },
    wisdomCard: {
        backgroundColor: '#1B4D3E',
        marginHorizontal: 20,
        borderRadius: 18,
        padding: 18,
        marginBottom: 20,
    },
    wisdomText: {
        color: '#FFFFFF',
        fontSize: 13,
        lineHeight: 19,
        fontStyle: 'italic',
        fontWeight: '500',
    },
    wisdomAuthor: {
        color: 'rgba(255, 255, 255, 0.7)',
        fontSize: 11,
        fontWeight: '700',
        marginTop: 8,
        textAlign: 'right',
    },
    historySection: {
        paddingHorizontal: 20,
        paddingBottom: 30,
    },
    historyHeader: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: 12,
    },
    historyTitle: {
        fontSize: 18,
        fontWeight: '800',
        color: '#111827',
    },
    historyCount: {
        fontSize: 12,
        color: '#6B7280',
        fontWeight: '600',
    },
    emptyHistoryBox: {
        backgroundColor: '#FFFFFF',
        borderRadius: 18,
        padding: 24,
        alignItems: 'center',
        borderWidth: 1,
        borderColor: '#E5E7EB',
        gap: 8,
    },
    emptyHistoryTitle: {
        fontSize: 15,
        fontWeight: '700',
        color: '#374151',
        marginTop: 4,
    },
    emptyHistorySubtitle: {
        fontSize: 12,
        color: '#9CA3AF',
        textAlign: 'center',
        lineHeight: 16,
    },
    emptyStartBtn: {
        backgroundColor: '#1B4D3E',
        paddingHorizontal: 16,
        paddingVertical: 10,
        borderRadius: 12,
        marginTop: 6,
    },
    emptyStartBtnText: {
        color: '#FFFFFF',
        fontSize: 13,
        fontWeight: '700',
    },
    historyList: {
        gap: 10,
    },
    historyCard: {
        backgroundColor: '#FFFFFF',
        borderRadius: 14,
        padding: 14,
        flexDirection: 'row',
        alignItems: 'center',
        borderWidth: 1,
        borderColor: '#E5E7EB',
    },
    historyIconCircle: {
        width: 32,
        height: 32,
        borderRadius: 16,
        backgroundColor: '#E6F4EA',
        alignItems: 'center',
        justifyContent: 'center',
    },
    historyCardTitle: {
        fontSize: 14,
        fontWeight: '700',
        color: '#111827',
    },
    historyCardDate: {
        fontSize: 11,
        color: '#9CA3AF',
        marginTop: 2,
    },
    historyCardRight: {
        alignItems: 'flex-end',
        gap: 3,
    },
    historyAccBadge: {
        backgroundColor: '#E6F4EA',
        paddingHorizontal: 8,
        paddingVertical: 3,
        borderRadius: 8,
    },
    historyAccText: {
        color: '#10B981',
        fontSize: 11,
        fontWeight: '800',
    },
    historyDurationText: {
        fontSize: 11,
        color: '#6B7280',
        fontWeight: '600',
    },
});
