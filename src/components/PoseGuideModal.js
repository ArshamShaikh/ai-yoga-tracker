import React from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, ScrollView, Dimensions, Image } from 'react-native';
import { FontAwesome5 } from '@expo/vector-icons';
import { getPoseMetadata } from '../constants/poseVisuals';
import { getPoseImage } from '../constants/poseImages';

const { width, height } = Dimensions.get('window');

export default function PoseGuideModal({ visible, pose, onClose, onStartSession }) {
    if (!pose) return null;

    const meta = getPoseMetadata(pose.id);
    const accentColor = meta?.accentColor || '#1B4D3E';
    const iconName = meta?.icon || 'spa';

    const getDifficultyColor = (diff) => {
        switch (diff) {
            case 'advanced': return { bg: '#FEE2E2', text: '#991B1B' };
            case 'intermediate': return { bg: '#FEF3C7', text: '#92400E' };
            case 'beginner':
            default:
                return { bg: '#E8F5E9', text: '#1B4D3E' };
        }
    };

    const diffStyle = getDifficultyColor(pose.difficulty);

    return (
        <Modal
            visible={visible}
            animationType="slide"
            transparent={true}
            onRequestClose={onClose}
        >
            <View style={styles.backdrop}>
                <View style={styles.sheetContainer}>
                    {/* Top Bar with Close Button */}
                    <View style={styles.sheetHeader}>
                        <View style={styles.sheetPill} />
                        <TouchableOpacity style={styles.closeBtn} onPress={onClose} activeOpacity={0.8}>
                            <FontAwesome5 name="times" size={16} color="#6B7280" />
                        </TouchableOpacity>
                    </View>

                    <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={styles.scrollContent}>
                        {/* Pose Hero Card */}
                        <View style={styles.poseHero}>
                            {getPoseImage(pose.id) ? (
                                <View style={styles.poseImageHeroBox}>
                                    <Image
                                        source={getPoseImage(pose.id)}
                                        style={styles.poseImageHero}
                                        resizeMode="contain"
                                    />
                                </View>
                            ) : (
                                <View style={[styles.largeIconCircle, { backgroundColor: `${accentColor}1A`, borderColor: accentColor }]}>
                                    <FontAwesome5 name={iconName} size={36} color={accentColor} />
                                </View>
                            )}

                            <View style={styles.badgeRow}>
                                <View style={[styles.diffBadge, { backgroundColor: diffStyle.bg }]}>
                                    <Text style={[styles.diffText, { color: diffStyle.text }]}>
                                        {pose.difficulty ? pose.difficulty.toUpperCase() : 'BEGINNER'}
                                    </Text>
                                </View>
                                {meta?.categoryTag && (
                                    <View style={styles.catBadge}>
                                        <Text style={styles.catBadgeText}>{meta.categoryTag}</Text>
                                    </View>
                                )}
                            </View>

                            <Text style={styles.poseName}>{pose.name}</Text>
                            <Text style={styles.sanskritName}>{pose.sanskrit || pose.name}</Text>
                        </View>

                        {/* Joint Checkpoints to Nail */}
                        {pose.joints && pose.joints.length > 0 && (
                            <View style={styles.section}>
                                <View style={styles.sectionHeaderRow}>
                                    <FontAwesome5 name="crosshairs" size={14} color="#1B4D3E" style={{ marginRight: 6 }} />
                                    <Text style={styles.sectionTitle}>3D Checkpoints Monitored</Text>
                                </View>
                                <View style={styles.checkpointsRow}>
                                    {pose.joints.map((joint, idx) => (
                                        <View key={idx} style={styles.checkpointCard}>
                                            <Text style={styles.jointName}>{joint.name}</Text>
                                            <Text style={styles.jointTarget}>
                                                Target: {joint.target?.ideal ? `${joint.target.ideal}°` : `${joint.target?.min}-${joint.target?.max}°`}
                                            </Text>
                                        </View>
                                    ))}
                                </View>
                            </View>
                        )}

                        {/* Step-by-Step Instructions */}
                        <View style={styles.section}>
                            <View style={styles.sectionHeaderRow}>
                                <FontAwesome5 name="clipboard-list" size={14} color="#1B4D3E" style={{ marginRight: 6 }} />
                                <Text style={styles.sectionTitle}>How to Perform</Text>
                            </View>
                            <View style={styles.instructionsList}>
                                {meta?.instructions?.map((step, idx) => (
                                    <View key={idx} style={styles.instructionStep}>
                                        <View style={styles.stepNumberCircle}>
                                            <Text style={styles.stepNumberText}>{idx + 1}</Text>
                                        </View>
                                        <Text style={styles.stepText}>{step}</Text>
                                    </View>
                                ))}
                            </View>
                        </View>

                        {/* Anatomical Benefits */}
                        {meta?.benefits && (
                            <View style={styles.benefitsCard}>
                                <View style={styles.sectionHeaderRow}>
                                    <FontAwesome5 name="heartbeat" size={14} color="#10B981" style={{ marginRight: 6 }} />
                                    <Text style={styles.benefitsTitle}>Key Benefits</Text>
                                </View>
                                <Text style={styles.benefitsText}>{meta.benefits}</Text>
                            </View>
                        )}

                        <View style={{ height: 20 }} />
                    </ScrollView>

                    {/* Bottom CTA to Launch 3D Camera Session */}
                    <View style={styles.footerContainer}>
                        <TouchableOpacity
                            style={[styles.startButton, { backgroundColor: accentColor }]}
                            onPress={() => onStartSession(pose.id)}
                            activeOpacity={0.85}
                        >
                            <FontAwesome5 name="camera" size={16} color="#FFFFFF" style={{ marginRight: 8 }} />
                            <Text style={styles.startButtonText}>Start 3D Session</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </View>
        </Modal>
    );
}

const styles = StyleSheet.create({
    backdrop: {
        flex: 1,
        backgroundColor: 'rgba(0, 0, 0, 0.55)',
        justifyContent: 'flex-end',
    },
    sheetContainer: {
        maxHeight: height * 0.88,
        backgroundColor: '#FFFFFF',
        borderTopLeftRadius: 28,
        borderTopRightRadius: 28,
        paddingTop: 10,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: -4 },
        shadowOpacity: 0.15,
        shadowRadius: 16,
        elevation: 20,
    },
    sheetHeader: {
        alignItems: 'center',
        paddingHorizontal: 20,
        paddingBottom: 6,
        position: 'relative',
    },
    sheetPill: {
        width: 40,
        height: 5,
        borderRadius: 3,
        backgroundColor: '#E5E7EB',
        marginBottom: 8,
    },
    closeBtn: {
        position: 'absolute',
        right: 18,
        top: 2,
        width: 32,
        height: 32,
        borderRadius: 16,
        backgroundColor: '#F3F4F6',
        alignItems: 'center',
        justifyContent: 'center',
    },
    scrollContent: {
        paddingHorizontal: 20,
        paddingBottom: 20,
    },
    poseHero: {
        alignItems: 'center',
        paddingVertical: 12,
        borderBottomWidth: 1,
        borderBottomColor: '#F3F4F6',
        marginBottom: 16,
    },
    poseImageHeroBox: {
        width: 140,
        height: 140,
        backgroundColor: '#F7F8F9',
        borderRadius: 24,
        padding: 10,
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: 14,
        borderWidth: 1,
        borderColor: '#E5E7EB',
    },
    poseImageHero: {
        width: '100%',
        height: '100%',
    },
    largeIconCircle: {
        width: 76,
        height: 76,
        borderRadius: 38,
        borderWidth: 2,
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: 12,
    },
    badgeRow: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 8,
        marginBottom: 8,
    },
    diffBadge: {
        paddingHorizontal: 10,
        paddingVertical: 4,
        borderRadius: 10,
    },
    diffText: {
        fontSize: 10,
        fontWeight: '800',
        letterSpacing: 0.5,
    },
    catBadge: {
        paddingHorizontal: 10,
        paddingVertical: 4,
        borderRadius: 10,
        backgroundColor: '#F3F4F6',
    },
    catBadgeText: {
        fontSize: 10,
        fontWeight: '700',
        color: '#4B5563',
    },
    poseName: {
        fontSize: 22,
        fontWeight: '800',
        color: '#111827',
        textAlign: 'center',
        marginBottom: 2,
    },
    sanskritName: {
        fontSize: 14,
        fontStyle: 'italic',
        color: '#6B7280',
        textAlign: 'center',
    },
    section: {
        marginBottom: 18,
    },
    sectionHeaderRow: {
        flexDirection: 'row',
        alignItems: 'center',
        marginBottom: 10,
    },
    sectionTitle: {
        fontSize: 15,
        fontWeight: '800',
        color: '#111827',
    },
    checkpointsRow: {
        gap: 8,
    },
    checkpointCard: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        backgroundColor: '#F9FAFB',
        paddingHorizontal: 12,
        paddingVertical: 10,
        borderRadius: 12,
        borderWidth: 1,
        borderColor: '#E5E7EB',
    },
    jointName: {
        fontSize: 13,
        fontWeight: '700',
        color: '#374151',
    },
    jointTarget: {
        fontSize: 12,
        fontWeight: '700',
        color: '#1B4D3E',
    },
    instructionsList: {
        gap: 10,
    },
    instructionStep: {
        flexDirection: 'row',
        alignItems: 'flex-start',
        gap: 12,
    },
    stepNumberCircle: {
        width: 22,
        height: 22,
        borderRadius: 11,
        backgroundColor: '#E8F5E9',
        alignItems: 'center',
        justifyContent: 'center',
        marginTop: 2,
    },
    stepNumberText: {
        fontSize: 11,
        fontWeight: '800',
        color: '#1B4D3E',
    },
    stepText: {
        fontSize: 13,
        color: '#4B5563',
        flex: 1,
        lineHeight: 19,
    },
    benefitsCard: {
        backgroundColor: '#ECFDF5',
        borderRadius: 16,
        padding: 14,
        borderWidth: 1,
        borderColor: '#A7F3D0',
        marginBottom: 10,
    },
    benefitsTitle: {
        fontSize: 13,
        fontWeight: '800',
        color: '#065F46',
    },
    benefitsText: {
        fontSize: 12,
        color: '#047857',
        lineHeight: 18,
    },
    footerContainer: {
        paddingHorizontal: 20,
        paddingVertical: 14,
        borderTopWidth: 1,
        borderTopColor: '#F3F4F6',
        backgroundColor: '#FFFFFF',
    },
    startButton: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        paddingVertical: 14,
        borderRadius: 16,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 4 },
        shadowOpacity: 0.15,
        shadowRadius: 8,
        elevation: 4,
    },
    startButtonText: {
        color: '#FFFFFF',
        fontSize: 15,
        fontWeight: '800',
        letterSpacing: 0.3,
    },
});
