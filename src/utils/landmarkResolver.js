/**
 * landmarkResolver.js
 * Resolves semantic body landmark names (e.g., 'LEFT_KNEE', 'RIGHT_SHOULDER')
 * to actual keypoint objects in both BlazePose (33 landmarks) and MoveNet (17 keypoints).
 */

import { BLAZEPOSE_LANDMARKS } from '../constants/landmarks.js';

// MoveNet COCO 17 Keypoint Index Mapping
export const MOVENET_LANDMARKS = {
    NOSE: 0,
    LEFT_EYE: 1,
    RIGHT_EYE: 2,
    LEFT_EAR: 3,
    RIGHT_EAR: 4,
    LEFT_SHOULDER: 5,
    RIGHT_SHOULDER: 6,
    LEFT_ELBOW: 7,
    RIGHT_ELBOW: 8,
    LEFT_WRIST: 9,
    RIGHT_WRIST: 10,
    LEFT_HIP: 11,
    RIGHT_HIP: 12,
    LEFT_KNEE: 13,
    RIGHT_KNEE: 14,
    LEFT_ANKLE: 15,
    RIGHT_ANKLE: 16,
};

/**
 * Resolves a landmark identifier (string name or numerical index) into the keypoint object.
 * @param {Array} keypoints - Array of keypoint objects { x, y, z, score }
 * @param {string|number} identifier - e.g., 'LEFT_KNEE', 'LEFT_HIP' or index 25
 * @returns {Object|null} Keypoint object or null if not found
 */
export function resolveKeypoint(keypoints, identifier) {
    if (!keypoints || keypoints.length === 0) return null;

    const isBlazePose = keypoints.length >= 33;
    let index = -1;

    if (typeof identifier === 'number') {
        index = identifier;
    } else if (typeof identifier === 'string') {
        const normalized = identifier.toUpperCase().trim();
        if (isBlazePose) {
            index = BLAZEPOSE_LANDMARKS[normalized] ?? -1;
        } else {
            index = MOVENET_LANDMARKS[normalized] ?? -1;
        }
    }

    if (index >= 0 && index < keypoints.length) {
        return keypoints[index];
    }

    return null;
}

/**
 * Resolves a trio of landmark identifiers [A, B, C] where B is vertex.
 * @param {Array} keypoints - Array of keypoints
 * @param {Array<string|number>} landmarkTrio - [pointA, vertexB, pointC]
 * @returns {Array<Object>|null} [pA, pB, pC] or null if any missing
 */
export function resolveLandmarkTrio(keypoints, landmarkTrio) {
    if (!landmarkTrio || landmarkTrio.length !== 3) return null;

    const pA = resolveKeypoint(keypoints, landmarkTrio[0]);
    const pB = resolveKeypoint(keypoints, landmarkTrio[1]);
    const pC = resolveKeypoint(keypoints, landmarkTrio[2]);

    if (!pA || !pB || !pC) return null;
    return [pA, pB, pC];
}
