import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Image, Modal } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useRouter } from 'expo-router';
import { FontAwesome5 } from '@expo/vector-icons';
import routinesData from '../../src/constants/routines.json';
import poseConstraints from '../../src/constants/poseConstraints.json';
import { getPoseImage } from '../../src/constants/poseImages';

export default function Routines() {
    const router = useRouter();
    const [selectedDifficulty, setSelectedDifficulty] = useState('All');
    const [previewRoutine, setPreviewRoutine] = useState(null);

    const difficulties = ['All', 'Beginner', 'Intermediate', 'Advanced'];

    const filteredRoutines = routinesData.routines.filter(r => {
        if (selectedDifficulty === 'All') return true;
        return r.difficulty.toLowerCase() === selectedDifficulty.toLowerCase();
    });

    const handleStartRoutine = (routineId) => {
        setPreviewRoutine(null);
        router.push({ pathname: '/session', params: { targetRoutine: routineId } });
    };

    return (
        <SafeAreaView style={styles.safeArea} edges={['top', 'left', 'right']}>
            <StatusBar style="dark" />

            <View style={styles.header}>
                <Text style={styles.headerSubtitle}>CURATED VINYASA FLOWS</Text>
                <Text style={styles.headerTitle}>Yoga Routines</Text>
                <Text style={styles.headerDescription}>
                    Guided multi-pose sequences with automated hold timers and 3D posture alignment.
                </Text>
            </View>

            {/* Filter Chips */}
            <View style={styles.filterRow}>
                {difficulties.map((diff) => {
                    const isSelected = selectedDifficulty === diff;
                    return (
                        <TouchableOpacity
                            key={diff}
                            onPress={() => setSelectedDifficulty(diff)}
                            style={[styles.filterChip, isSelected && styles.filterChipActive]}
                            activeOpacity={0.8}
                        >
                            <Text style={[styles.filterText, isSelected && styles.filterTextActive]}>
                                {diff}
                            </Text>
                        </TouchableOpacity>
                    );
                })}
            </View>

            {/* Routines List */}
            <ScrollView style={styles.listContainer} contentContainerStyle={styles.listContent} showsVerticalScrollIndicator={false}>
                {filteredRoutines.map((routine) => {
                    const diffColors = {
                        beginner: '#10B981',
                        intermediate: '#3B82F6',
                        advanced: '#8B5CF6',
                    };
                    const badgeColor = diffColors[routine.difficulty.toLowerCase()] || '#10B981';

                    return (
                        <TouchableOpacity
                            key={routine.id}
                            style={styles.routineCard}
                            onPress={() => setPreviewRoutine(routine)}
                            activeOpacity={0.9}
                        >
                            {/* Card Top: Accent icon, title, difficulty */}
                            <View style={styles.cardHeader}>
                                <View style={[styles.routineIconCircle, { backgroundColor: `${routine.accentColor}1A` }]}>
                                    <FontAwesome5 name={routine.icon} size={20} color={routine.accentColor} />
                                </View>
                                <View style={styles.headerTitles}>
                                    <Text style={styles.routineTitle}>{routine.title}</Text>
                                    <Text style={styles.routineSubtitle}>{routine.subtitle}</Text>
                                </View>
                                <View style={[styles.diffBadge, { backgroundColor: `${badgeColor}18`, borderColor: `${badgeColor}40` }]}>
                                    <Text style={[styles.diffBadgeText, { color: badgeColor }]}>
                                        {routine.difficulty.toUpperCase()}
                                    </Text>
                                </View>
                            </View>

                            {/* Poses Preview Row */}
                            <View style={styles.posePreviewStrip}>
                                <Text style={styles.stripLabel}>Poses ({routine.poses.length}):</Text>
                                <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.stripPosesRow}>
                                    {routine.poses.map((item, idx) => {
                                        const img = getPoseImage(item.poseId);
                                        const poseDef = poseConstraints.yoga_poses.find(p => p.id === item.poseId);
                                        return (
                                            <View key={idx} style={styles.poseThumbnailBox}>
                                                {img ? (
                                                    <Image source={img} style={styles.poseThumbImg} resizeMode="contain" />
                                                ) : (
                                                    <View style={styles.poseThumbPlaceholder}>
                                                        <FontAwesome5 name="spa" size={14} color="#1B4D3E" />
                                                    </View>
                                                )}
                                                <Text style={styles.poseThumbName} numberOfLines={1}>
                                                    {poseDef?.name || item.poseId}
                                                </Text>
                                            </View>
                                        );
                                    })}
                                </ScrollView>
                            </View>

                            {/* Card Footer: Duration & Start Button */}
                            <View style={styles.cardFooter}>
                                <View style={styles.metaRow}>
                                    <View style={styles.metaItem}>
                                        <FontAwesome5 name="clock" size={12} color="#6B7280" />
                                        <Text style={styles.metaText}>{routine.durationMinutes} mins</Text>
                                    </View>
                                    <View style={styles.metaItem}>
                                        <FontAwesome5 name="layer-group" size={12} color="#6B7280" />
                                        <Text style={styles.metaText}>{routine.poses.length} poses</Text>
                                    </View>
                                </View>

                                <TouchableOpacity
                                    style={[styles.startFlowBtn, { backgroundColor: routine.accentColor }]}
                                    onPress={() => handleStartRoutine(routine.id)}
                                    activeOpacity={0.85}
                                >
                                    <FontAwesome5 name="play" size={12} color="#FFFFFF" style={{ marginRight: 6 }} />
                                    <Text style={styles.startFlowBtnText}>Start Flow</Text>
                                </TouchableOpacity>
                            </View>
                        </TouchableOpacity>
                    );
                })}
            </ScrollView>

            {/* Routine Detailed Preview Modal */}
            <Modal visible={!!previewRoutine} transparent animationType="slide">
                <View style={styles.modalBackdrop}>
                    <View style={styles.modalCard}>
                        {previewRoutine && (
                            <>
                                <View style={styles.modalHeader}>
                                    <View style={[styles.routineIconCircle, { backgroundColor: `${previewRoutine.accentColor}1A` }]}>
                                        <FontAwesome5 name={previewRoutine.icon} size={22} color={previewRoutine.accentColor} />
                                    </View>
                                    <View style={{ flex: 1, marginLeft: 12 }}>
                                        <Text style={styles.modalTitle}>{previewRoutine.title}</Text>
                                        <Text style={styles.modalSubtitle}>{previewRoutine.subtitle}</Text>
                                    </View>
                                    <TouchableOpacity onPress={() => setPreviewRoutine(null)} style={styles.closeBtn}>
                                        <FontAwesome5 name="times" size={16} color="#6B7280" />
                                    </TouchableOpacity>
                                </View>

                                <Text style={styles.modalPosesHeading}>Flow Sequence Breakdown</Text>
                                <ScrollView style={styles.modalPosesList} showsVerticalScrollIndicator={false}>
                                    {previewRoutine.poses.map((item, idx) => {
                                        const poseDef = poseConstraints.yoga_poses.find(p => p.id === item.poseId);
                                        const img = getPoseImage(item.poseId);
                                        return (
                                            <View key={idx} style={styles.modalPoseItem}>
                                                <Text style={styles.modalPoseNumber}>{idx + 1}</Text>
                                                <View style={styles.modalPoseImageBox}>
                                                    {img ? (
                                                        <Image source={img} style={styles.modalPoseImage} resizeMode="contain" />
                                                    ) : (
                                                        <FontAwesome5 name="spa" size={16} color="#1B4D3E" />
                                                    )}
                                                </View>
                                                <View style={{ flex: 1 }}>
                                                    <Text style={styles.modalPoseName}>{poseDef?.name || item.poseId}</Text>
                                                    <Text style={styles.modalPoseSanskrit}>{poseDef?.sanskrit || ''}</Text>
                                                </View>
                                                <View style={styles.modalHoldBadge}>
                                                    <FontAwesome5 name="stopwatch" size={11} color="#1B4D3E" />
                                                    <Text style={styles.modalHoldText}>{item.targetHoldSec}s hold</Text>
                                                </View>
                                            </View>
                                        );
                                    })}
                                </ScrollView>

                                <TouchableOpacity
                                    style={[styles.modalStartBtn, { backgroundColor: previewRoutine.accentColor }]}
                                    onPress={() => handleStartRoutine(previewRoutine.id)}
                                    activeOpacity={0.85}
                                >
                                    <FontAwesome5 name="play" size={14} color="#FFFFFF" style={{ marginRight: 8 }} />
                                    <Text style={styles.modalStartBtnText}>Begin Guided Flow</Text>
                                </TouchableOpacity>
                            </>
                        )}
                    </View>
                </View>
            </Modal>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    safeArea: {
        flex: 1,
        backgroundColor: '#F8FAF9',
    },
    header: {
        paddingHorizontal: 20,
        paddingTop: 12,
        paddingBottom: 8,
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
    filterRow: {
        flexDirection: 'row',
        paddingHorizontal: 20,
        gap: 8,
        marginVertical: 12,
    },
    filterChip: {
        paddingHorizontal: 14,
        paddingVertical: 7,
        borderRadius: 20,
        backgroundColor: '#E5E7EB',
    },
    filterChipActive: {
        backgroundColor: '#1B4D3E',
    },
    filterText: {
        fontSize: 12,
        fontWeight: '700',
        color: '#4B5563',
    },
    filterTextActive: {
        color: '#FFFFFF',
    },
    listContainer: {
        flex: 1,
    },
    listContent: {
        paddingHorizontal: 20,
        paddingBottom: 24,
        gap: 16,
    },
    routineCard: {
        backgroundColor: '#FFFFFF',
        borderRadius: 20,
        padding: 16,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 4 },
        shadowOpacity: 0.05,
        shadowRadius: 10,
        elevation: 3,
        borderWidth: 1,
        borderColor: '#E5E7EB',
    },
    cardHeader: {
        flexDirection: 'row',
        alignItems: 'center',
        marginBottom: 12,
    },
    routineIconCircle: {
        width: 44,
        height: 44,
        borderRadius: 22,
        alignItems: 'center',
        justifyContent: 'center',
        marginRight: 12,
    },
    headerTitles: {
        flex: 1,
    },
    routineTitle: {
        fontSize: 17,
        fontWeight: '800',
        color: '#111827',
    },
    routineSubtitle: {
        fontSize: 12,
        color: '#6B7280',
        marginTop: 2,
    },
    diffBadge: {
        paddingHorizontal: 8,
        paddingVertical: 4,
        borderRadius: 8,
        borderWidth: 1,
    },
    diffBadgeText: {
        fontSize: 10,
        fontWeight: '800',
        letterSpacing: 0.5,
    },
    posePreviewStrip: {
        marginVertical: 8,
    },
    stripLabel: {
        fontSize: 11,
        fontWeight: '700',
        color: '#9CA3AF',
        textTransform: 'uppercase',
        letterSpacing: 0.5,
        marginBottom: 8,
    },
    stripPosesRow: {
        gap: 12,
    },
    poseThumbnailBox: {
        width: 76,
        alignItems: 'center',
    },
    poseThumbImg: {
        width: 54,
        height: 54,
        borderRadius: 14,
        backgroundColor: '#F3F4F6',
        marginBottom: 4,
    },
    poseThumbPlaceholder: {
        width: 54,
        height: 54,
        borderRadius: 14,
        backgroundColor: '#F3F4F6',
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: 4,
    },
    poseThumbName: {
        fontSize: 10,
        fontWeight: '600',
        color: '#4B5563',
        textAlign: 'center',
    },
    cardFooter: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        paddingTop: 12,
        borderTopWidth: 1,
        borderTopColor: '#F3F4F6',
        marginTop: 6,
    },
    metaRow: {
        flexDirection: 'row',
        gap: 12,
    },
    metaItem: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 5,
    },
    metaText: {
        fontSize: 12,
        color: '#6B7280',
        fontWeight: '600',
    },
    startFlowBtn: {
        flexDirection: 'row',
        alignItems: 'center',
        paddingHorizontal: 14,
        paddingVertical: 8,
        borderRadius: 12,
    },
    startFlowBtnText: {
        color: '#FFFFFF',
        fontSize: 12,
        fontWeight: '800',
    },
    modalBackdrop: {
        flex: 1,
        backgroundColor: 'rgba(0, 0, 0, 0.6)',
        justifyContent: 'flex-end',
    },
    modalCard: {
        backgroundColor: '#FFFFFF',
        borderTopLeftRadius: 28,
        borderTopRightRadius: 28,
        padding: 24,
        maxHeight: '80%',
    },
    modalHeader: {
        flexDirection: 'row',
        alignItems: 'center',
        marginBottom: 16,
    },
    modalTitle: {
        fontSize: 20,
        fontWeight: '800',
        color: '#111827',
    },
    modalSubtitle: {
        fontSize: 13,
        color: '#6B7280',
        marginTop: 2,
    },
    closeBtn: {
        padding: 8,
    },
    modalPosesHeading: {
        fontSize: 13,
        fontWeight: '800',
        color: '#111827',
        textTransform: 'uppercase',
        letterSpacing: 0.5,
        marginBottom: 12,
    },
    modalPosesList: {
        maxHeight: 300,
        marginBottom: 16,
    },
    modalPoseItem: {
        flexDirection: 'row',
        alignItems: 'center',
        paddingVertical: 10,
        borderBottomWidth: 1,
        borderBottomColor: '#F3F4F6',
    },
    modalPoseNumber: {
        fontSize: 13,
        fontWeight: '800',
        color: '#9CA3AF',
        width: 24,
    },
    modalPoseImageBox: {
        width: 44,
        height: 44,
        borderRadius: 10,
        backgroundColor: '#F3F4F6',
        alignItems: 'center',
        justifyContent: 'center',
        marginRight: 12,
    },
    modalPoseImage: {
        width: 38,
        height: 38,
    },
    modalPoseName: {
        fontSize: 14,
        fontWeight: '700',
        color: '#111827',
    },
    modalPoseSanskrit: {
        fontSize: 11,
        fontStyle: 'italic',
        color: '#9CA3AF',
    },
    modalHoldBadge: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 5,
        paddingHorizontal: 8,
        paddingVertical: 4,
        borderRadius: 8,
        backgroundColor: '#E6F4EA',
    },
    modalHoldText: {
        fontSize: 11,
        fontWeight: '700',
        color: '#1B4D3E',
    },
    modalStartBtn: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        paddingVertical: 15,
        borderRadius: 16,
    },
    modalStartBtnText: {
        color: '#FFFFFF',
        fontSize: 16,
        fontWeight: '800',
    },
});
