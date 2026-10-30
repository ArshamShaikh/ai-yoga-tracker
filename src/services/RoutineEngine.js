/**
 * RoutineEngine.js
 * Comprehensive finite state machine managing guided yoga routines and single-pose sessions.
 * Manages pose transitions, hold timers, accuracy scoring, and workout progression.
 */

import routinesData from '../constants/routines.json';
import poseConstraints from '../constants/poseConstraints.json';
import CalibrationEngine from '../utils/CalibrationEngine.js';

export const SESSION_STATES = {
    CALIBRATING: 'CALIBRATING',
    GET_READY: 'GET_READY',
    HOLDING: 'HOLDING',
    POSE_SUCCESS: 'POSE_SUCCESS',
    TRANSITION: 'TRANSITION',
    FINISHED: 'FINISHED',
};

export class RoutineEngine {
    constructor() {
        this.reset();
    }

    reset() {
        this.state = SESSION_STATES.CALIBRATING;
        this.isRoutine = false;
        this.routineId = null;
        this.routineTitle = 'Single Pose Studio';
        this.posesList = [];
        this.currentPoseIndex = 0;
        this.activePoseDef = null;

        // Timing
        this.sessionStartTime = 0;
        this.stateStartTime = Date.now();
        this.currentHoldSeconds = 0;
        this.targetHoldSeconds = 10;
        this.getReadySecondsLeft = 3;
        this.transitionSecondsLeft = 3;

        // Accuracy & metrics
        this.totalFramesEvaluated = 0;
        this.correctFramesCount = 0;
        this.postureCorrectSince = 0;
        this.completedPoses = [];

        CalibrationEngine.reset();
    }

    /**
     * Initializes a session for either a multi-pose routine or a single pose.
     * @param {string} targetId - Either routine ID (e.g. 'sun_salutation_a') or pose ID (e.g. 'vrikshasana')
     */
    initSession(targetId) {
        this.reset();
        this.sessionStartTime = Date.now();
        this.stateStartTime = Date.now();

        const cleanId = (targetId || '').toLowerCase().trim();

        const ALIASES = {
            'warrior_i': 'virabhadrasana_i',
            'warrior_ii': 'virabhadrasana_ii',
            'warrior_iii': 'virabhadrasana_iii',
            'mountain': 'tadasana',
            'tree': 'vrikshasana',
            'chair': 'utkatasana',
            'plank': 'phalakasana',
            'downward_dog': 'adho_mukha_svanasana',
            'cobra': 'bhujangasana',
            'childs_pose': 'balasana',
            'bridge': 'setu_bandhasana',
            'triangle': 'trikonasana',
            'baddhakonasana': 'baddha_konasana',
        };
        const resolvedPoseId = ALIASES[cleanId] || cleanId;

        // Check if targetId is a routine
        const foundRoutine = routinesData.routines.find(r => r.id === cleanId || r.id === targetId);

        if (foundRoutine) {
            this.isRoutine = true;
            this.routineId = foundRoutine.id;
            this.routineTitle = foundRoutine.title;
            this.posesList = foundRoutine.poses.map(item => {
                const pId = ALIASES[item.poseId] || item.poseId;
                const def = poseConstraints.yoga_poses.find(p => p.id === pId) || poseConstraints.yoga_poses[0];
                return {
                    ...def,
                    targetHoldSec: item.targetHoldSec || 8
                };
            });
        } else {
            // Single pose session
            this.isRoutine = false;
            const def = poseConstraints.yoga_poses.find(p => p.id === resolvedPoseId)
                || poseConstraints.yoga_poses.find(p => p.id === cleanId)
                || poseConstraints.yoga_poses[0];
            this.routineTitle = def.name;
            this.posesList = [{ ...def, targetHoldSec: 10 }];
        }

        this.currentPoseIndex = 0;
        this.loadCurrentPose();
    }

    loadCurrentPose() {
        if (this.currentPoseIndex >= this.posesList.length) {
            this.state = SESSION_STATES.FINISHED;
            return;
        }

        this.activePoseDef = this.posesList[this.currentPoseIndex];
        this.targetHoldSeconds = this.activePoseDef.targetHoldSec || 10;
        this.currentHoldSeconds = 0;
        this.postureCorrectSince = 0;
        this.getReadySecondsLeft = 3;
        this.transitionSecondsLeft = 3;
    }

    /**
     * Main per-frame state machine update.
     * @param {Array} keypoints - Detected landmarks
     * @param {Object} evaluation - Result from FeedbackEngine.process()
     * @returns {Object} status - Current session telemetry for the UI
     */
    update(keypoints, evaluation) {
        const now = Date.now();

        // 1. CALIBRATING STATE
        if (this.state === SESSION_STATES.CALIBRATING) {
            const calib = CalibrationEngine.evaluate(keypoints, this.activePoseDef);
            if (calib.isCalibrated) {
                this.state = SESSION_STATES.GET_READY;
                this.stateStartTime = now;
            }
            return this.getTelemetry(calib.guidance, 0, false);
        }

        // 2. GET_READY COUNTDOWN (3s prep)
        if (this.state === SESSION_STATES.GET_READY) {
            const elapsed = Math.floor((now - this.stateStartTime) / 1000);
            const remaining = Math.max(0, 3 - elapsed);
            this.getReadySecondsLeft = remaining;

            if (remaining <= 0) {
                this.state = SESSION_STATES.HOLDING;
                this.stateStartTime = now;
            }
            return this.getTelemetry(`Get ready: ${this.activePoseDef.name}`, 0, false);
        }

        // 3. HOLDING STATE
        if (this.state === SESSION_STATES.HOLDING) {
            this.totalFramesEvaluated++;
            if (evaluation?.isCorrect) {
                this.correctFramesCount++;

                if (this.postureCorrectSince === 0) {
                    this.postureCorrectSince = now;
                } else {
                    const elapsed = Math.floor((now - this.postureCorrectSince) / 1000);
                    this.currentHoldSeconds = Math.min(this.targetHoldSeconds, elapsed);
                }

                // Check if target hold duration is reached!
                if (this.currentHoldSeconds >= this.targetHoldSeconds) {
                    this.state = SESSION_STATES.POSE_SUCCESS;
                    this.stateStartTime = now;
                    this.completedPoses.push({
                        poseId: this.activePoseDef.id,
                        name: this.activePoseDef.name,
                        holdSec: this.currentHoldSeconds,
                    });
                }
            } else {
                // Posture broke: reset active hold counter
                if (this.postureCorrectSince !== 0) {
                    this.postureCorrectSince = 0;
                    this.currentHoldSeconds = 0;
                }
            }

            const guidance = evaluation?.feedbackMessage || 'Hold steady and breathe';
            return this.getTelemetry(guidance, this.currentHoldSeconds, evaluation?.isCorrect || false);
        }

        // 4. POSE_SUCCESS (Celebratory hold)
        if (this.state === SESSION_STATES.POSE_SUCCESS) {
            const elapsed = Math.floor((now - this.stateStartTime) / 1000);
            if (elapsed >= 1) { // 1.5s celebratory pause
                if (this.currentPoseIndex + 1 < this.posesList.length) {
                    this.state = SESSION_STATES.TRANSITION;
                    this.stateStartTime = now;
                } else {
                    this.state = SESSION_STATES.FINISHED;
                }
            }
            return this.getTelemetry('Pose Completed! Wonderful form.', this.targetHoldSeconds, true);
        }

        // 5. TRANSITION (Brief rest between poses)
        if (this.state === SESSION_STATES.TRANSITION) {
            const elapsed = Math.floor((now - this.stateStartTime) / 1000);
            const remaining = Math.max(0, 3 - elapsed);
            this.transitionSecondsLeft = remaining;

            if (remaining <= 0) {
                this.currentPoseIndex++;
                this.loadCurrentPose();
                this.state = SESSION_STATES.GET_READY;
                this.stateStartTime = now;
            }

            const nextPose = this.posesList[this.currentPoseIndex + 1]?.name || 'Next Pose';
            return this.getTelemetry(`Rest & Transition: Next up is ${nextPose}`, 0, false);
        }

        // 6. FINISHED
        return this.getTelemetry('Session Complete! Namaste.', this.targetHoldSeconds, true);
    }

    /**
     * Skip to next pose manually.
     */
    skipPose() {
        if (this.currentPoseIndex + 1 < this.posesList.length) {
            this.currentPoseIndex++;
            this.loadCurrentPose();
            this.state = SESSION_STATES.GET_READY;
            this.stateStartTime = Date.now();
        } else {
            this.state = SESSION_STATES.FINISHED;
        }
    }

    getAccuracyScore() {
        if (this.totalFramesEvaluated === 0) return 100;
        return Math.round((this.correctFramesCount / this.totalFramesEvaluated) * 100);
    }

    getTelemetry(guidance, holdSeconds, isCorrect) {
        const totalDurationSec = Math.floor((Date.now() - (this.sessionStartTime || Date.now())) / 1000);
        return {
            state: this.state,
            isRoutine: this.isRoutine,
            routineTitle: this.routineTitle,
            activePoseDef: this.activePoseDef,
            currentPoseIndex: this.currentPoseIndex,
            totalPoses: this.posesList.length,
            holdSeconds,
            targetHoldSeconds: this.targetHoldSeconds,
            holdProgress: this.targetHoldSeconds > 0 ? Math.min(1.0, holdSeconds / this.targetHoldSeconds) : 0,
            isCorrect,
            guidance,
            getReadySecondsLeft: this.getReadySecondsLeft,
            transitionSecondsLeft: this.transitionSecondsLeft,
            accuracyScore: this.getAccuracyScore(),
            totalDurationSec,
            completedCount: this.completedPoses.length,
        };
    }
}

export default new RoutineEngine();
