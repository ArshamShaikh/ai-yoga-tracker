/**
 * CalibrationEngine.js
 * Evaluates whether the user is properly framed and positioned before or during a workout.
 * Provides real-time biomechanical framing guidance (e.g., "Step back", "Center yourself").
 */

import { BLAZEPOSE_LANDMARKS, MOVENET_LANDMARKS } from '../constants/landmarks.js';

export class CalibrationEngine {
  constructor() {
    this.steadyStartTimestamp = 0;
    this.REQUIRED_STEADY_DURATION_MS = 1500; // Must hold good framing for 1.5s
    this.isCalibrated = false;
    this.lastGuidance = 'Step into the camera view';
  }

  reset() {
    this.steadyStartTimestamp = 0;
    this.isCalibrated = false;
    this.lastGuidance = 'Step into the camera view';
  }

  /**
   * Evaluates camera framing from detected keypoints.
   * @param {Array} keypoints - 2D/3D landmarks array with x, y, score
   * @param {Object} [poseDef] - Optional pose definition to inspect orientation (standing vs seated)
   * @returns {Object} { isCalibrated, isWellFramed, progress, guidance, statusCode }
   */
  evaluate(keypoints, poseDef = null) {
    if (!keypoints || keypoints.length === 0) {
      this.steadyStartTimestamp = 0;
      this.lastGuidance = 'Position yourself in front of the camera';
      return {
        isCalibrated: false,
        isWellFramed: false,
        progress: 0,
        guidance: this.lastGuidance,
        statusCode: 'NO_PERSON'
      };
    }

    const isBlazePose = keypoints.length >= 33;
    const L = isBlazePose ? BLAZEPOSE_LANDMARKS : MOVENET_LANDMARKS;

    const getPt = (name) => {
      const idx = L[name];
      if (idx === undefined || !keypoints[idx]) return null;
      const pt = keypoints[idx];
      return (pt.score ?? 1) >= 0.35 ? pt : null;
    };

    const nose = getPt('NOSE');
    const leftShoulder = getPt('LEFT_SHOULDER');
    const rightShoulder = getPt('RIGHT_SHOULDER');
    const leftHip = getPt('LEFT_HIP');
    const rightHip = getPt('RIGHT_HIP');
    const leftKnee = getPt('LEFT_KNEE');
    const rightKnee = getPt('RIGHT_KNEE');
    const leftAnkle = getPt('LEFT_ANKLE');
    const rightAnkle = getPt('RIGHT_ANKLE');

    // Check if primary torso anchors exist
    const hasTorso = (leftShoulder || rightShoulder) && (leftHip || rightHip);
    if (!hasTorso) {
      this.steadyStartTimestamp = 0;
      this.lastGuidance = 'Step back so your body is visible';
      return {
        isCalibrated: false,
        isWellFramed: false,
        progress: 0,
        guidance: this.lastGuidance,
        statusCode: 'TORSO_OCCLUDED'
      };
    }

    // Horizontal centering check (0.0 to 1.0 or pixel scaled)
    // Normalize coordinates if not normalized
    const samplePt = leftShoulder || rightShoulder;
    const isNormalized = samplePt.x <= 1.0 && samplePt.y <= 1.0;

    let torsoCenterX = 0.5;
    if (leftHip && rightHip) {
      torsoCenterX = (leftHip.x + rightHip.x) / 2;
    } else if (leftShoulder && rightShoulder) {
      torsoCenterX = (leftShoulder.x + rightShoulder.x) / 2;
    }

    // If coordinates are in pixels (e.g. 144x256), normalize
    const normCenterX = isNormalized ? torsoCenterX : torsoCenterX / 144;

    if (normCenterX < 0.12) {
      this.steadyStartTimestamp = 0;
      this.lastGuidance = 'Move slightly to the right';
      return { isCalibrated: false, isWellFramed: false, progress: 0, guidance: this.lastGuidance, statusCode: 'OFF_CENTER_LEFT' };
    }
    if (normCenterX > 0.88) {
      this.steadyStartTimestamp = 0;
      this.lastGuidance = 'Move slightly to the left';
      return { isCalibrated: false, isWellFramed: false, progress: 0, guidance: this.lastGuidance, statusCode: 'OFF_CENTER_RIGHT' };
    }

    // Lower body visibility check
    const hasLegs = (leftKnee || rightKnee);
    const hasFeet = (leftAnkle || rightAnkle);

    if (!hasLegs && !hasFeet) {
      this.steadyStartTimestamp = 0;
      this.lastGuidance = 'Step back so your full legs are in frame';
      return { isCalibrated: false, isWellFramed: false, progress: 0, guidance: this.lastGuidance, statusCode: 'FEET_CUT_OFF' };
    }

    // Head bounds check
    if (nose) {
      const normNoseY = isNormalized ? nose.y : nose.y / 256;
      if (normNoseY < 0.04) {
        this.steadyStartTimestamp = 0;
        this.lastGuidance = 'Tilt camera up or step back slightly';
        return { isCalibrated: false, isWellFramed: false, progress: 0, guidance: this.lastGuidance, statusCode: 'HEAD_CUT_OFF' };
      }
    }

    // Framing is good! Track steady timer
    const now = Date.now();
    if (this.steadyStartTimestamp === 0) {
      this.steadyStartTimestamp = now;
    }

    const elapsed = now - this.steadyStartTimestamp;
    const progress = Math.min(1.0, elapsed / this.REQUIRED_STEADY_DURATION_MS);

    if (progress >= 1.0) {
      this.isCalibrated = true;
      this.lastGuidance = 'Full body detected! Form ready.';
      return {
        isCalibrated: true,
        isWellFramed: true,
        progress: 1.0,
        guidance: this.lastGuidance,
        statusCode: 'READY'
      };
    } else {
      this.lastGuidance = 'Hold steady... calibrating';
      return {
        isCalibrated: false,
        isWellFramed: true,
        progress,
        guidance: this.lastGuidance,
        statusCode: 'CALIBRATING'
      };
    }
  }
}

export default new CalibrationEngine();