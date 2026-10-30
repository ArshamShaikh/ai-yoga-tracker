import Tts from 'react-native-tts';
import { calculateJointAngle, exponentialSmoothing } from '../utils/poseMathUtils';
import { resolveLandmarkTrio, resolveKeypoint } from '../utils/landmarkResolver';
import { BLAZEPOSE_LANDMARKS, MOVENET_LANDMARKS } from '../constants/landmarks';
import poseConstraints from '../constants/poseConstraints.json';

class FeedbackEngine {
    constructor() {
        this.lastSpokenTime = 0;
        this.smoothedKeypoints = null;
        this.isMuted = false;
        this.lastFeedbackText = '';

        try {
            Tts.setDefaultLanguage('en-US');
            Tts.setDefaultRate(0.35); // Calm matching pace for yoga
            Tts.setDefaultPitch(1.0);
        } catch (e) {
            console.warn("TTS Hardware Warning Setup", e);
        }
    }

    /**
     * Evaluates the smoothed skeleton math against the constraint file and triggers dynamic audio limits
     * @returns {Object} result - Contains { keypoints, isCorrect, invalidIndices, angleReadings }
     */
    process(pose, targetPoseId) {
        if (!pose || !pose.keypoints) return { keypoints: [], isCorrect: false, invalidIndices: [], angleReadings: [] };

        this.smoothedKeypoints = exponentialSmoothing(pose.keypoints, this.smoothedKeypoints, 0.35);
        pose.keypoints = this.smoothedKeypoints;

        // Support both common English IDs and authentic Sanskrit IDs
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
        };
        const resolvedId = ALIASES[targetPoseId] || targetPoseId;
        const targetPoseDef = poseConstraints.yoga_poses.find(p => p.id === resolvedId || p.id === targetPoseId);
        if (!targetPoseDef) return { keypoints: pose.keypoints, isCorrect: false, invalidIndices: [], angleReadings: [] };

        const isBlazePose = pose.keypoints.length >= 33;
        const landmarkMap = isBlazePose ? BLAZEPOSE_LANDMARKS : MOVENET_LANDMARKS;

        let isCorrect = true;
        let invalidIndices = [];
        let angleReadings = [];

        for (let jointDef of targetPoseDef.joints) {
            let pA, pB, pC;
            let jointIndices = [];

            if (jointDef.landmarks && jointDef.landmarks.length === 3) {
                const trio = resolveLandmarkTrio(pose.keypoints, jointDef.landmarks);
                if (!trio) {
                    isCorrect = false;
                    continue;
                }
                [pA, pB, pC] = trio;
                jointIndices = jointDef.landmarks.map(name => landmarkMap[name.toUpperCase()] ?? -1).filter(idx => idx >= 0);
            } else if (jointDef.indices && jointDef.indices.length === 3) {
                // Fallback for legacy numerical index definitions
                pA = pose.keypoints[jointDef.indices[0]];
                pB = pose.keypoints[jointDef.indices[1]];
                pC = pose.keypoints[jointDef.indices[2]];
                jointIndices = jointDef.indices;
            } else {
                continue;
            }

            // Ensure all 3 joint landmarks meet confidence threshold
            if (!pA || !pB || !pC || (pA.score ?? 1) < 0.4 || (pB.score ?? 1) < 0.4 || (pC.score ?? 1) < 0.4) {
                isCorrect = false;
                continue;
            }

            const angle = calculateJointAngle(pA, pB, pC);
            angleReadings.push({ name: jointDef.name, angle: Math.round(angle), target: jointDef.target });

            const variance = jointDef.variance ?? 12;
            const minAllowed = jointDef.target.min - variance;
            const maxAllowed = jointDef.target.max + variance;

            if (angle < minAllowed) {
                isCorrect = false;
                invalidIndices.push(...jointIndices);
                if (jointDef.feedback?.low) this.speak(jointDef.feedback.low);
            } else if (angle > maxAllowed) {
                isCorrect = false;
                invalidIndices.push(...jointIndices);
                if (jointDef.feedback?.high) this.speak(jointDef.feedback.high);
            }
        }

        const feedbackMessage = isCorrect
            ? "Form locked! Hold steady."
            : (this.lastFeedbackText || "Adjust your joint angles");

        return { keypoints: pose.keypoints, isCorrect, invalidIndices, angleReadings, feedbackMessage };
    }

    setMuted(muted) {
        this.isMuted = muted;
    }

    toggleMute() {
        this.isMuted = !this.isMuted;
        return this.isMuted;
    }

    speak(message) {
        this.lastFeedbackText = message;
        if (this.isMuted) return;

        const now = Date.now();
        // Fire speech commands only sparsely to not abuse CPU block / sensory overload
        if (now - this.lastSpokenTime > 4000) {
            try {
                Tts.speak(message);
            } catch (err) {
                console.warn("[TTS Audio Warning]", err?.message || err);
            }
            console.log(`[🗣 AUDIO OUT]: ${message}`);
            this.lastSpokenTime = now;
        }
    }

    stop() {
        try {
            Tts.stop();
        } catch (err) {
            // Safe ignore on simulators/unsupported hardware
        }
    }
}

export default new FeedbackEngine();
