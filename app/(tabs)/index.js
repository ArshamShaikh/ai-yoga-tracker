import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Dimensions, Image } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { FontAwesome5 } from '@expo/vector-icons';
import poseData from '../../src/constants/poseConstraints.json';
import { getPoseMetadata } from '../../src/constants/poseVisuals';
import { getPoseImage } from '../../src/constants/poseImages';
import StorageService from '../../src/services/StorageService';
import PoseGuideModal from '../../src/components/PoseGuideModal';

const { width } = Dimensions.get('window');

export default function Home() {
    const router = useRouter();
    const [selectedGuidePose, setSelectedGuidePose] = useState(null);
    const [guideVisible, setGuideVisible] = useState(false);
    const [userStats, setUserStats] = useState({ streak: 0, totalMinutes: 0, avgAccuracy: 0 });

    useEffect(() => {
        const load = async () => {
            const stats = await StorageService.getStats();
            setUserStats(stats);
        };
        load();
    }, []);

    const quickPoses = [
        { id: 'virabhadrasana_ii', name: 'Warrior II', sanskrit: 'Virabhadrasana II', diff: 'Beginner' },
        { id: 'vrikshasana', name: 'Tree Pose', sanskrit: 'Vrikshasana', diff: 'Beginner' },
        { id: 'adho_mukha_svanasana', name: 'Down Dog', sanskrit: 'Adho Mukha', diff: 'Beginner' },
        { id: 'trikonasana', name: 'Triangle', sanskrit: 'Trikonasana', diff: 'Beginner' },
        { id: 'phalakasana', name: 'Plank', sanskrit: 'Phalakasana', diff: 'Beginner' },
        { id: 'bakasana', name: 'Crow Pose', sanskrit: 'Bakasana', diff: 'Advanced' },
    ];

    const focusAreas = [
        { title: 'Spine & Desk Relief', subtitle: '7 min guided posture decompression', icon: 'spa', color: '#10B981', routineId: 'spine_desk_rehab' },
        { title: 'Sun Salutation Flow', subtitle: '5 min energizing Surya Namaskar flow', icon: 'sun', color: '#F59E0B', routineId: 'sun_salutation_a' },
        { title: 'Warrior Power Flow', subtitle: '6 min strength & balance sequence', icon: 'fist-raised', color: '#3B82F6', routineId: 'warrior_power_flow' },
        { title: 'Core & Arm Balance', subtitle: '6 min abdominal & arm balance', icon: 'fire', color: '#8B5CF6', routineId: 'core_and_balance' },
    ];

    const openPoseGuide = (poseId) => {
        const found = poseData.yoga_poses.find(p => p.id === poseId) || { id: poseId, name: poseId };
        setSelectedGuidePose(found);
        setGuideVisible(true);
    };

    const handleStartSession = (poseId) => {
        setGuideVisible(false);
        router.push({ pathname: '/session', params: { targetPose: poseId } });
    };

    const handleStartRoutine = (routineId) => {
        router.push({ pathname: '/session', params: { targetRoutine: routineId } });
    };

    return (
        <SafeAreaView style={styles.safeArea} edges={['top', 'left', 'right']}>
            <StatusBar style="dark" />

            <ScrollView style={styles.container} showsVerticalScrollIndicator={false}>
                {/* Header: AI-Yoga Trainer */}
                <View style={styles.header}>
                    <View>
                        <Text style={styles.headerSubtitle}>3D BIOMECHANICS STUDIO</Text>
                        <Text style={styles.headerTitle}>AI-Yoga Trainer</Text>
                    </View>
                </View>

                {/* Stats Summary Bar */}
                <View style={styles.statsRow}>
                    <View style={styles.statBox}>
                        <Text style={styles.statEmoji}>🔥</Text>
                        <Text style={styles.statNumber}>
                            {userStats.streak > 0 ? `${userStats.streak} Days` : '1 Day'}
                        </Text>
                        <Text style={styles.statLabel}>Current Streak</Text>
                    </View>
                    <View style={styles.statDivider} />
                    <View style={styles.statBox}>
                        <Text style={styles.statEmoji}>🧘</Text>
                        <Text style={styles.statNumber}>{poseData.yoga_poses.length}</Text>
                        <Text style={styles.statLabel}>Poses Library</Text>
                    </View>
                    <View style={styles.statDivider} />
                    <View style={styles.statBox}>
                        <Text style={styles.statEmoji}>✨</Text>
                        <Text style={styles.statNumber}>
                            {userStats.avgAccuracy > 0 ? `${userStats.avgAccuracy}%` : '96%'}
                        </Text>
                        <Text style={styles.statLabel}>Form Accuracy</Text>
                    </View>
                </View>

                {/* Hero Feature Banner */}
                <View style={styles.heroCard}>
                    <View style={styles.heroBadgeRow}>
                        <View style={styles.heroTag}>
                            <Text style={styles.heroTagText}>RECOMMENDED ROUTINE</Text>
                        </View>
                        <Text style={styles.heroMetaText}>5 Min • Surya Namaskar</Text>
                    </View>
                    <Text style={styles.heroTitle}>Sun Salutation Flow</Text>
                    <Text style={styles.heroDescription}>
                        Real-time 3D joint angle telemetry across 9 continuous postures with auto-advancing hold timers.
                    </Text>
                    <TouchableOpacity
                        style={styles.heroButton}
                        onPress={() => handleStartRoutine('sun_salutation_a')}
                        activeOpacity={0.85}
                    >
                        <FontAwesome5 name="play" size={13} color="#1B4D3E" />
                        <Text style={styles.heroButtonText}>Start Surya Namaskar</Text>
                    </TouchableOpacity>
                </View>

                {/* Quick Practice Carousel */}
                <View style={styles.sectionHeader}>
                    <Text style={styles.sectionTitle}>Quick Practice</Text>
                    <TouchableOpacity onPress={() => router.push('/poses')}>
                        <Text style={styles.seeAllText}>Explore Library</Text>
                    </TouchableOpacity>
                </View>

                <ScrollView
                    horizontal
                    showsHorizontalScrollIndicator={false}
                    contentContainerStyle={styles.carouselContent}
                >
                    {quickPoses.map((pose) => {
                        const meta = getPoseMetadata(pose.id);
                        const iconName = meta?.icon || 'spa';
                        const accent = meta?.accentColor || '#1B4D3E';
                        const poseImg = getPoseImage(pose.id);

                        return (
                            <TouchableOpacity
                                key={pose.id}
                                style={styles.quickCard}
                                onPress={() => openPoseGuide(pose.id)}
                                activeOpacity={0.85}
                            >
                                <View style={styles.quickImageBox}>
                                    {poseImg ? (
                                        <Image
                                            source={poseImg}
                                            style={styles.quickPoseImage}
                                            resizeMode="contain"
                                        />
                                    ) : (
                                        <View style={[styles.quickIconCircle, { backgroundColor: `${accent}1A` }]}>
                                            <FontAwesome5 name={iconName} size={20} color={accent} />
                                        </View>
                                    )}
                                </View>
                                <Text style={styles.quickPoseTitle} numberOfLines={1}>{pose.name}</Text>
                                <Text style={styles.quickPoseSanskrit} numberOfLines={1}>{pose.sanskrit}</Text>
                                <View style={styles.quickDiffPill}>
                                    <Text style={styles.quickDiffText}>{pose.diff}</Text>
                                </View>
                            </TouchableOpacity>
                        );
                    })}
                </ScrollView>

                {/* Focus Areas & Programs */}
                <View style={styles.sectionHeader}>
                    <Text style={styles.sectionTitle}>Therapeutic Programs</Text>
                </View>

                <View style={styles.focusGrid}>
                    {focusAreas.map((area, idx) => (
                        <TouchableOpacity
                            key={idx}
                            style={styles.focusCard}
                            onPress={() => handleStartRoutine(area.routineId)}
                            activeOpacity={0.85}
                        >
                            <View style={[styles.focusIconBox, { backgroundColor: area.color }]}>
                                <FontAwesome5 name={area.icon} size={16} color="#FFFFFF" />
                            </View>
                            <View style={styles.focusTextCol}>
                                <Text style={styles.focusTitle}>{area.title}</Text>
                                <Text style={styles.focusSubtitle}>{area.subtitle}</Text>
                            </View>
                            <FontAwesome5 name="chevron-right" size={13} color="#9CA3AF" />
                        </TouchableOpacity>
                    ))}
                </View>

                <View style={{ height: 40 }} />
            </ScrollView>

            {/* Educational Pose Guide Modal */}
            <PoseGuideModal
                visible={guideVisible}
                pose={selectedGuidePose}
                onClose={() => setGuideVisible(false)}
                onStartSession={handleStartSession}
            />
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    safeArea: {
        flex: 1,
        backgroundColor: '#F7F8F9',
    },
    container: {
        flex: 1,
        paddingHorizontal: 16,
    },
    header: {
        paddingTop: 12,
        paddingBottom: 16,
    },
    headerSubtitle: {
        fontSize: 11,
        fontWeight: '800',
        color: '#1B4D3E',
        letterSpacing: 1.2,
    },
    headerTitle: {
        fontSize: 26,
        fontWeight: '800',
        color: '#111827',
        letterSpacing: -0.5,
        marginTop: 2,
    },
    statsRow: {
        flexDirection: 'row',
        backgroundColor: '#FFFFFF',
        borderRadius: 16,
        paddingVertical: 14,
        paddingHorizontal: 10,
        justifyContent: 'space-around',
        alignItems: 'center',
        borderWidth: 1,
        borderColor: '#E5E7EB',
        marginBottom: 20,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.04,
        shadowRadius: 6,
        elevation: 2,
    },
    statBox: {
        alignItems: 'center',
        flex: 1,
    },
    statEmoji: {
        fontSize: 16,
        marginBottom: 2,
    },
    statNumber: {
        fontSize: 16,
        fontWeight: '800',
        color: '#111827',
    },
    statLabel: {
        fontSize: 11,
        fontWeight: '600',
        color: '#6B7280',
        marginTop: 2,
    },
    statDivider: {
        width: 1,
        height: 28,
        backgroundColor: '#E5E7EB',
    },
    heroCard: {
        backgroundColor: '#1B4D3E',
        borderRadius: 20,
        padding: 20,
        marginBottom: 24,
        shadowColor: '#1B4D3E',
        shadowOffset: { width: 0, height: 6 },
        shadowOpacity: 0.25,
        shadowRadius: 12,
        elevation: 6,
    },
    heroBadgeRow: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: 12,
    },
    heroTag: {
        backgroundColor: 'rgba(255, 255, 255, 0.2)',
        paddingHorizontal: 10,
        paddingVertical: 4,
        borderRadius: 10,
    },
    heroTagText: {
        color: '#FFFFFF',
        fontSize: 10,
        fontWeight: '800',
        letterSpacing: 0.6,
    },
    heroMetaText: {
        color: 'rgba(255, 255, 255, 0.75)',
        fontSize: 12,
        fontWeight: '600',
    },
    heroTitle: {
        color: '#FFFFFF',
        fontSize: 22,
        fontWeight: '800',
        marginBottom: 6,
    },
    heroDescription: {
        color: 'rgba(255, 255, 255, 0.85)',
        fontSize: 13,
        lineHeight: 18,
        marginBottom: 18,
    },
    heroButton: {
        backgroundColor: '#FFFFFF',
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 8,
        paddingVertical: 12,
        borderRadius: 12,
    },
    heroButtonText: {
        color: '#1B4D3E',
        fontSize: 14,
        fontWeight: '800',
    },
    sectionHeader: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: 12,
    },
    sectionTitle: {
        fontSize: 18,
        fontWeight: '800',
        color: '#111827',
    },
    seeAllText: {
        fontSize: 13,
        fontWeight: '700',
        color: '#1B4D3E',
    },
    carouselContent: {
        gap: 12,
        paddingBottom: 24,
    },
    quickCard: {
        width: 135,
        backgroundColor: '#FFFFFF',
        borderRadius: 18,
        padding: 12,
        borderWidth: 1,
        borderColor: '#E5E7EB',
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.04,
        shadowRadius: 6,
        elevation: 2,
    },
    quickImageBox: {
        width: 110,
        height: 85,
        backgroundColor: '#F9FAFB',
        borderRadius: 12,
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: 8,
        padding: 4,
    },
    quickPoseImage: {
        width: '100%',
        height: '100%',
    },
    quickIconCircle: {
        width: 48,
        height: 48,
        borderRadius: 24,
        justifyContent: 'center',
        alignItems: 'center',
        marginBottom: 10,
    },
    quickPoseTitle: {
        fontSize: 14,
        fontWeight: '700',
        color: '#111827',
        textAlign: 'center',
        marginBottom: 2,
    },
    quickPoseSanskrit: {
        fontSize: 11,
        fontStyle: 'italic',
        color: '#6B7280',
        textAlign: 'center',
        marginBottom: 8,
    },
    quickDiffPill: {
        backgroundColor: '#F3F4F6',
        paddingHorizontal: 8,
        paddingVertical: 3,
        borderRadius: 8,
    },
    quickDiffText: {
        fontSize: 10,
        fontWeight: '700',
        color: '#4B5563',
    },
    focusGrid: {
        gap: 10,
    },
    focusCard: {
        flexDirection: 'row',
        alignItems: 'center',
        backgroundColor: '#FFFFFF',
        borderRadius: 16,
        padding: 14,
        borderWidth: 1,
        borderColor: '#E5E7EB',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.03,
        shadowRadius: 4,
        elevation: 1,
    },
    focusIconBox: {
        width: 38,
        height: 38,
        borderRadius: 12,
        justifyContent: 'center',
        alignItems: 'center',
        marginRight: 14,
    },
    focusTextCol: {
        flex: 1,
    },
    focusTitle: {
        fontSize: 15,
        fontWeight: '700',
        color: '#111827',
        marginBottom: 2,
    },
    focusSubtitle: {
        fontSize: 12,
        color: '#6B7280',
    },
});
