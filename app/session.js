import React, { useEffect, useState, useRef } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, ScrollView, Modal } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useLocalSearchParams, useRouter } from 'expo-router';
import YogaCamera from '../src/components/YogaCamera';
import PoseOverlay from '../src/components/PoseOverlay';
import PoseDetectorService from '../src/services/PoseDetector';
import FeedbackEngine from '../src/services/FeedbackEngine';
import RoutineEngine, { SESSION_STATES } from '../src/services/RoutineEngine';
import StorageService from '../src/services/StorageService';
import poseConstraints from '../src/constants/poseConstraints.json';
import { FontAwesome5 } from '@expo/vector-icons';

export default function Session() {
    const { targetPose, targetRoutine } = useLocalSearchParams();
    const router = useRouter();
    const [modelReady, setModelReady] = useState(false);

    // Core camera & audio controls
    const [cameraType, setCameraType] = useState('front');
    const [isMuted, setIsMuted] = useState(false);

    // Active pose & telemetry states
    const [activePose, setActivePose] = useState(null);
    const [invalidJoints, setInvalidJoints] = useState([]);
    const [liveAngles, setLiveAngles] = useState([]);
    const [showSummary, setShowSummary] = useState(false);
    const [summaryData, setSummaryData] = useState(null);

    // Routine engine live state
    const [telemetry, setTelemetry] = useState({
        state: SESSION_STATES.CALIBRATING,
        isRoutine: false,
        routineTitle: 'Yoga Session',
        activePoseDef: null,
        currentPoseIndex: 0,
        totalPoses: 1,
        holdSeconds: 0,
        targetHoldSeconds: 10,
        holdProgress: 0,
        isCorrect: false,
        guidance: 'Align your full body in the camera frame',
        getReadySecondsLeft: 3,
        transitionSecondsLeft: 3,
        accuracyScore: 100,
        totalDurationSec: 0,
    });

    const activePoseDef = telemetry.activePoseDef
        || (targetPose ? poseConstraints.yoga_poses.find(p => p.id === targetPose) : null)
        || poseConstraints.yoga_poses[0];

    useEffect(() => {
        const init = async () => {
            const ready = await PoseDetectorService.initialize();
            setModelReady(ready);

            // Initialize RoutineEngine with routine or single pose
            const identifier = targetRoutine || targetPose || 'tadasana';
            RoutineEngine.initSession(identifier);
            setTelemetry(RoutineEngine.getTelemetry('Align yourself in the frame', 0, false));
        };
        init();

        return () => {
            FeedbackEngine.stop();
            RoutineEngine.reset();
        };
    }, [targetPose, targetRoutine]);

    const toggleAudioMute = () => {
        const muted = FeedbackEngine.toggleMute();
        setIsMuted(muted);
    };

    const handleSkipCalibration = () => {
        RoutineEngine.state = SESSION_STATES.GET_READY;
        RoutineEngine.stateStartTime = Date.now();
    };

    const handleSkipPose = () => {
        RoutineEngine.skipPose();
    };

    const handleFinishSession = async () => {
        if (summaryData) {
            await StorageService.saveSession({
                title: telemetry.routineTitle || 'Yoga Practice',
                durationSec: summaryData.durationSec,
                accuracyScore: summaryData.accuracyScore,
                posesCount: summaryData.posesCompleted,
            });
        }
        setShowSummary(false);
        router.back();
    };

    const handlePoseDetected = async (imageTensor) => {
        const rawPose = await PoseDetectorService.estimatePoses(imageTensor);

        if (rawPose && rawPose.length > 0) {
            const currentPoseId = RoutineEngine.activePoseDef?.id || activePoseDef.id;
            const evaluation = FeedbackEngine.process(rawPose[0], currentPoseId);

            setActivePose({ keypoints: evaluation.keypoints });
            setInvalidJoints(evaluation.invalidIndices || []);
            if (evaluation.angleReadings) setLiveAngles(evaluation.angleReadings);

            // Update routine finite state machine
            const updatedTelemetry = RoutineEngine.update(evaluation.keypoints, evaluation);
            setTelemetry(updatedTelemetry);

            // Trigger session complete modal when finished
            if (updatedTelemetry.state === SESSION_STATES.FINISHED && !showSummary) {
                setSummaryData({
                    durationSec: updatedTelemetry.totalDurationSec,
                    accuracyScore: updatedTelemetry.accuracyScore,
                    posesCompleted: updatedTelemetry.completedCount || updatedTelemetry.totalPoses,
                    title: updatedTelemetry.routineTitle,
                });
                setShowSummary(true);
            }
        }
    };

    const isCalibrating = telemetry.state === SESSION_STATES.CALIBRATING;
    const isGetReady = telemetry.state === SESSION_STATES.GET_READY;
    const isTransition = telemetry.state === SESSION_STATES.TRANSITION;
    const isPoseSuccess = telemetry.state === SESSION_STATES.POSE_SUCCESS;

    return (
        <SafeAreaView style={styles.container} edges={['top', 'left', 'right']}>
            <StatusBar style="light" />

            {/* Glassmorphic Top Studio Bar */}
            <View style={styles.topBar}>
                <TouchableOpacity onPress={() => router.back()} style={styles.glassButton} activeOpacity={0.8}>
                    <FontAwesome5 name="chevron-left" size={16} color="#FFFFFF" />
                </TouchableOpacity>

                <View style={styles.poseInfoCenter}>
                    {telemetry.isRoutine && (
                        <Text style={styles.routineSubtitle}>
                            {`Pose ${telemetry.currentPoseIndex + 1} of ${telemetry.totalPoses} • ${telemetry.routineTitle}`}
                        </Text>
                    )}
                    <Text style={styles.poseTitle} numberOfLines={1}>{activePoseDef.name}</Text>
                    <Text style={styles.poseSanskrit} numberOfLines={1}>{activePoseDef.sanskrit}</Text>
                </View>

                <View style={styles.topRightControls}>
                    {telemetry.isRoutine && (
                        <TouchableOpacity onPress={handleSkipPose} style={styles.glassButton} activeOpacity={0.8}>
                            <FontAwesome5 name="forward" size={14} color="#FFFFFF" />
                        </TouchableOpacity>
                    )}
                    <TouchableOpacity onPress={toggleAudioMute} style={styles.glassButton} activeOpacity={0.8}>
                        <FontAwesome5 name={isMuted ? "volume-mute" : "volume-up"} size={16} color={isMuted ? "#EF4444" : "#FFFFFF"} />
                    </TouchableOpacity>
                    <TouchableOpacity
                        onPress={() => setCameraType(prev => prev === 'front' ? 'back' : 'front')}
                        style={styles.glassButton}
                        activeOpacity={0.8}
                    >
                        <FontAwesome5 name="sync-alt" size={15} color="#FFFFFF" />
                    </TouchableOpacity>
                </View>
            </View>

            {/* Camera Viewport Container */}
            <View style={styles.cameraBox}>
                {modelReady ? (
                    <YogaCamera onPoseFrame={handlePoseDetected} cameraType={cameraType}>
                        <PoseOverlay pose={activePose} invalidJoints={invalidJoints} isMirrored={cameraType === 'front'} />
                    </YogaCamera>
                ) : (
                    <View style={styles.loadingContainer}>
                        <FontAwesome5 name="circle-notch" size={32} color="#10B981" />
                        <Text style={styles.loadingText}>Initializing 3D Pose Engine...</Text>
                    </View>
                )}

                {/* Overlaid Countdown Badge (GET_READY or TRANSITION) */}
                {(isGetReady || isTransition) && (
                    <View style={styles.countdownOverlay}>
                        <Text style={styles.countdownTitle}>
                            {isGetReady ? "GET READY" : "REST & TRANSITION"}
                        </Text>
                        <Text style={styles.countdownNumber}>
                            {isGetReady ? telemetry.getReadySecondsLeft : telemetry.transitionSecondsLeft}
                        </Text>
                        <Text style={styles.countdownPose}>{activePoseDef.name}</Text>
                    </View>
                )}

                {/* Pose Success Flash Celebration */}
                {isPoseSuccess && (
                    <View style={styles.celebrationOverlay}>
                        <FontAwesome5 name="check-circle" size={48} color="#10B981" />
                        <Text style={styles.celebrationTitle}>Pose Completed!</Text>
                        <Text style={styles.celebrationSubtitle}>Hold time achieved</Text>
                    </View>
                )}

                {/* Calibration Guide Banner */}
                {isCalibrating && (
                    <View style={styles.calibrationBanner}>
                        <View style={styles.calibrationRow}>
                            <FontAwesome5 name="arrows-alt" size={16} color="#3B82F6" />
                            <Text style={styles.calibrationText}>{telemetry.guidance}</Text>
                        </View>
                        <TouchableOpacity onPress={handleSkipCalibration} style={styles.skipCalibBtn}>
                            <Text style={styles.skipCalibText}>Skip</Text>
                        </TouchableOpacity>
                    </View>
                )}

                {/* Floating Bottom Studio HUD Card */}
                <View style={styles.floatingHud}>
                    {/* Status & Timer Row */}
                    <View style={styles.hudHeaderRow}>
                        <View style={[
                            styles.statusBadge,
                            telemetry.isCorrect ? styles.statusBadgeGood : styles.statusBadgeAdjust
                        ]}>
                            <FontAwesome5
                                name={telemetry.isCorrect ? "check-circle" : "exclamation-circle"}
                                size={14}
                                color={telemetry.isCorrect ? "#10B981" : "#F59E0B"}
                            />
                            <Text style={[
                                styles.statusBadgeText,
                                telemetry.isCorrect ? styles.statusTextGood : styles.statusTextAdjust
                            ]}>
                                {telemetry.isCorrect ? "FORM LOCKED" : (isCalibrating ? "CALIBRATING" : "ADJUSTING")}
                            </Text>
                        </View>

                        {/* Hold Progress Pill */}
                        <View style={[styles.timerPill, telemetry.holdSeconds > 0 && styles.timerPillActive]}>
                            <FontAwesome5 name="stopwatch" size={13} color={telemetry.holdSeconds > 0 ? "#10B981" : "#9CA3AF"} />
                            <Text style={styles.timerPillText}>
                                {`Hold: ${telemetry.holdSeconds}s / ${telemetry.targetHoldSeconds}s`}
                            </Text>
                        </View>
                    </View>

                    {/* Progress Bar (Visual Hold Feedback) */}
                    <View style={styles.progressBarBg}>
                        <View style={[styles.progressBarFill, { width: `${Math.round(telemetry.holdProgress * 100)}%` }]} />
                    </View>

                    {/* AI Coach Subtitle Prompt */}
                    <View style={styles.coachBubble}>
                        <FontAwesome5 name="comment-alt" size={13} color="#10B981" style={{ marginRight: 8, marginTop: 2 }} />
                        <Text style={styles.coachMessageText}>{telemetry.guidance}</Text>
                    </View>

                    {/* Live Joint Angle Telemetry Chips */}
                    {liveAngles.length > 0 && (
                        <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.telemetryRow}>
                            {liveAngles.map((item, idx) => (
                                <View
                                    key={idx}
                                    style={[
                                        styles.angleChip,
                                        (item.angle >= item.target.min && item.angle <= item.target.max) ? styles.angleChipGood : styles.angleChipAdjust
                                    ]}
                                >
                                    <Text style={styles.angleChipName}>{item.name}</Text>
                                    <Text style={[
                                        styles.angleChipValue,
                                        (item.angle >= item.target.min && item.angle <= item.target.max) ? styles.angleValGood : styles.angleValAdjust
                                    ]}>
                                        {item.angle}°
                                    </Text>
                                </View>
                            ))}
                        </ScrollView>
                    )}
                </View>
            </View>

            {/* Workout Completed Celebratory Modal */}
            <Modal visible={showSummary} transparent animationType="fade">
                <View style={styles.summaryModalOverlay}>
                    <View style={styles.summaryCard}>
                        <View style={styles.trophyCircle}>
                            <FontAwesome5 name="trophy" size={36} color="#10B981" />
                        </View>
                        <Text style={styles.summaryTitle}>Session Completed!</Text>
                        <Text style={styles.summarySubtitle}>{telemetry.routineTitle || 'Practice Session'}</Text>

                        {/* Summary Metrics */}
                        <View style={styles.summaryMetricsRow}>
                            <View style={styles.summaryMetricItem}>
                                <Text style={styles.summaryMetricVal}>{summaryData?.accuracyScore || 100}%</Text>
                                <Text style={styles.summaryMetricLabel}>Accuracy</Text>
                            </View>
                            <View style={styles.summaryMetricItem}>
                                <Text style={styles.summaryMetricVal}>{summaryData?.durationSec || 0}s</Text>
                                <Text style={styles.summaryMetricLabel}>Duration</Text>
                            </View>
                            <View style={styles.summaryMetricItem}>
                                <Text style={styles.summaryMetricVal}>{summaryData?.posesCompleted || 1}</Text>
                                <Text style={styles.summaryMetricLabel}>Poses</Text>
                            </View>
                        </View>

                        <TouchableOpacity onPress={handleFinishSession} style={styles.finishBtn} activeOpacity={0.85}>
                            <Text style={styles.finishBtnText}>Save & Finish</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </Modal>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#0A0F0D',
    },
    topBar: {
        height: 70,
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        paddingHorizontal: 16,
        paddingTop: 10,
        backgroundColor: '#0A0F0D',
    },
    poseInfoCenter: {
        alignItems: 'center',
        justifyContent: 'center',
        flex: 1,
        marginHorizontal: 10,
    },
    routineSubtitle: {
        fontSize: 10,
        fontWeight: '700',
        color: '#10B981',
        textTransform: 'uppercase',
        letterSpacing: 0.5,
        marginBottom: 2,
    },
    poseTitle: {
        fontSize: 17,
        fontWeight: '800',
        color: '#FFFFFF',
        letterSpacing: -0.3,
    },
    poseSanskrit: {
        fontSize: 11,
        fontStyle: 'italic',
        color: '#9CA3AF',
        marginTop: 1,
    },
    topRightControls: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 8,
    },
    glassButton: {
        width: 38,
        height: 38,
        borderRadius: 19,
        backgroundColor: 'rgba(255, 255, 255, 0.12)',
        borderWidth: 1,
        borderColor: 'rgba(255, 255, 255, 0.18)',
        alignItems: 'center',
        justifyContent: 'center',
    },
    cameraBox: {
        flex: 1,
        borderRadius: 24,
        overflow: 'hidden',
        marginHorizontal: 12,
        marginBottom: 16,
        backgroundColor: '#000000',
        position: 'relative',
    },
    loadingContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        gap: 12,
    },
    loadingText: {
        color: '#9CA3AF',
        fontSize: 15,
        fontWeight: '600',
    },
    calibrationBanner: {
        position: 'absolute',
        top: 14,
        left: 14,
        right: 14,
        backgroundColor: 'rgba(17, 24, 39, 0.92)',
        borderRadius: 14,
        paddingHorizontal: 14,
        paddingVertical: 10,
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        borderWidth: 1,
        borderColor: 'rgba(59, 130, 246, 0.4)',
        zIndex: 20,
    },
    calibrationRow: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 10,
        flex: 1,
    },
    calibrationText: {
        color: '#FFFFFF',
        fontSize: 12,
        fontWeight: '600',
        flex: 1,
    },
    skipCalibBtn: {
        paddingHorizontal: 10,
        paddingVertical: 4,
        backgroundColor: 'rgba(255, 255, 255, 0.15)',
        borderRadius: 8,
        marginLeft: 8,
    },
    skipCalibText: {
        color: '#9CA3AF',
        fontSize: 11,
        fontWeight: '700',
    },
    countdownOverlay: {
        position: 'absolute',
        top: '35%',
        left: '20%',
        right: '20%',
        backgroundColor: 'rgba(0, 0, 0, 0.82)',
        borderRadius: 24,
        padding: 24,
        alignItems: 'center',
        justifyContent: 'center',
        borderWidth: 1,
        borderColor: 'rgba(255, 255, 255, 0.2)',
        zIndex: 30,
    },
    countdownTitle: {
        color: '#9CA3AF',
        fontSize: 12,
        fontWeight: '800',
        letterSpacing: 1,
        marginBottom: 6,
    },
    countdownNumber: {
        color: '#10B981',
        fontSize: 52,
        fontWeight: '900',
    },
    countdownPose: {
        color: '#FFFFFF',
        fontSize: 15,
        fontWeight: '700',
        marginTop: 6,
    },
    celebrationOverlay: {
        position: 'absolute',
        top: '35%',
        left: '20%',
        right: '20%',
        backgroundColor: 'rgba(16, 185, 129, 0.92)',
        borderRadius: 24,
        padding: 24,
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 30,
    },
    celebrationTitle: {
        color: '#FFFFFF',
        fontSize: 20,
        fontWeight: '800',
        marginTop: 10,
    },
    celebrationSubtitle: {
        color: '#D1FAE5',
        fontSize: 13,
        fontWeight: '600',
        marginTop: 2,
    },
    floatingHud: {
        position: 'absolute',
        bottom: 12,
        left: 12,
        right: 12,
        backgroundColor: 'rgba(10, 15, 13, 0.90)',
        borderRadius: 20,
        borderWidth: 1,
        borderColor: 'rgba(255, 255, 255, 0.14)',
        padding: 14,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 6 },
        shadowOpacity: 0.35,
        shadowRadius: 10,
        elevation: 8,
    },
    hudHeaderRow: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: 8,
    },
    statusBadge: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 6,
        paddingHorizontal: 12,
        paddingVertical: 5,
        borderRadius: 14,
        borderWidth: 1,
    },
    statusBadgeGood: {
        backgroundColor: 'rgba(16, 185, 129, 0.18)',
        borderColor: '#10B981',
    },
    statusBadgeAdjust: {
        backgroundColor: 'rgba(245, 158, 11, 0.18)',
        borderColor: '#F59E0B',
    },
    statusBadgeText: {
        fontSize: 11,
        fontWeight: '800',
        letterSpacing: 0.5,
    },
    statusTextGood: {
        color: '#10B981',
    },
    statusTextAdjust: {
        color: '#F59E0B',
    },
    timerPill: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 6,
        paddingHorizontal: 12,
        paddingVertical: 5,
        borderRadius: 14,
        backgroundColor: 'rgba(255, 255, 255, 0.08)',
        borderWidth: 1,
        borderColor: 'rgba(255, 255, 255, 0.12)',
    },
    timerPillActive: {
        borderColor: '#10B981',
        backgroundColor: 'rgba(16, 185, 129, 0.15)',
    },
    timerPillText: {
        color: '#FFFFFF',
        fontSize: 12,
        fontWeight: '700',
    },
    progressBarBg: {
        height: 4,
        backgroundColor: 'rgba(255, 255, 255, 0.1)',
        borderRadius: 2,
        overflow: 'hidden',
        marginBottom: 10,
    },
    progressBarFill: {
        height: '100%',
        backgroundColor: '#10B981',
    },
    coachBubble: {
        flexDirection: 'row',
        alignItems: 'flex-start',
        backgroundColor: 'rgba(255, 255, 255, 0.06)',
        borderRadius: 12,
        padding: 10,
        marginBottom: 8,
    },
    coachMessageText: {
        color: '#F3F4F6',
        fontSize: 13,
        fontWeight: '600',
        flex: 1,
        lineHeight: 18,
    },
    telemetryRow: {
        gap: 8,
        paddingTop: 4,
    },
    angleChip: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 6,
        paddingHorizontal: 10,
        paddingVertical: 5,
        borderRadius: 10,
        borderWidth: 1,
    },
    angleChipGood: {
        backgroundColor: 'rgba(16, 185, 129, 0.12)',
        borderColor: 'rgba(16, 185, 129, 0.4)',
    },
    angleChipAdjust: {
        backgroundColor: 'rgba(245, 158, 11, 0.12)',
        borderColor: 'rgba(245, 158, 11, 0.4)',
    },
    angleChipName: {
        color: '#9CA3AF',
        fontSize: 11,
        fontWeight: '600',
    },
    angleChipValue: {
        fontSize: 11,
        fontWeight: '700',
    },
    angleValGood: {
        color: '#10B981',
    },
    angleValAdjust: {
        color: '#F59E0B',
    },
    summaryModalOverlay: {
        flex: 1,
        backgroundColor: 'rgba(0, 0, 0, 0.85)',
        justifyContent: 'center',
        alignItems: 'center',
        padding: 24,
    },
    summaryCard: {
        width: '100%',
        backgroundColor: '#111827',
        borderRadius: 24,
        padding: 24,
        alignItems: 'center',
        borderWidth: 1,
        borderColor: 'rgba(255, 255, 255, 0.15)',
    },
    trophyCircle: {
        width: 72,
        height: 72,
        borderRadius: 36,
        backgroundColor: 'rgba(16, 185, 129, 0.18)',
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: 16,
    },
    summaryTitle: {
        fontSize: 22,
        fontWeight: '800',
        color: '#FFFFFF',
        marginBottom: 4,
    },
    summarySubtitle: {
        fontSize: 14,
        color: '#9CA3AF',
        marginBottom: 20,
    },
    summaryMetricsRow: {
        flexDirection: 'row',
        justifyContent: 'space-around',
        width: '100%',
        backgroundColor: 'rgba(255, 255, 255, 0.05)',
        borderRadius: 16,
        paddingVertical: 16,
        marginBottom: 24,
    },
    summaryMetricItem: {
        alignItems: 'center',
    },
    summaryMetricVal: {
        fontSize: 22,
        fontWeight: '800',
        color: '#10B981',
    },
    summaryMetricLabel: {
        fontSize: 11,
        color: '#9CA3AF',
        marginTop: 2,
    },
    finishBtn: {
        width: '100%',
        backgroundColor: '#10B981',
        borderRadius: 16,
        paddingVertical: 14,
        alignItems: 'center',
    },
    finishBtnText: {
        color: '#FFFFFF',
        fontSize: 16,
        fontWeight: '700',
    },
});
