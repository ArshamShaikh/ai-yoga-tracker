/**
 * Computes internal angle between three points A, B, C where B is the vertex.
 * Points are expected as objects {x, y}.
 */
export const calculateJointAngle = (A, B, C) => {
  if (!A || !B || !C) return 0;

  const aX = typeof A.x === 'number' ? A.x : 0;
  const aY = typeof A.y === 'number' ? A.y : 0;
  const aZ = typeof A.z === 'number' ? A.z : 0;

  const bX = typeof B.x === 'number' ? B.x : 0;
  const bY = typeof B.y === 'number' ? B.y : 0;
  const bZ = typeof B.z === 'number' ? B.z : 0;

  const cX = typeof C.x === 'number' ? C.x : 0;
  const cY = typeof C.y === 'number' ? C.y : 0;
  const cZ = typeof C.z === 'number' ? C.z : 0;

  const vectorBA = { x: aX - bX, y: aY - bY, z: aZ - bZ };
  const vectorBC = { x: cX - bX, y: cY - bY, z: cZ - bZ };

  const dotProduct = vectorBA.x * vectorBC.x + vectorBA.y * vectorBC.y + vectorBA.z * vectorBC.z;
  const magnitudeBA = Math.sqrt(vectorBA.x ** 2 + vectorBA.y ** 2 + vectorBA.z ** 2);
  const magnitudeBC = Math.sqrt(vectorBC.x ** 2 + vectorBC.y ** 2 + vectorBC.z ** 2);

  if (!magnitudeBA || !magnitudeBC || magnitudeBA * magnitudeBC === 0) return 0;

  const cosTheta = dotProduct / (magnitudeBA * magnitudeBC);
  if (isNaN(cosTheta)) return 0;

  // Clamp for precision errors to [-1, 1] range
  const clampedCos = Math.max(-1, Math.min(1, cosTheta));
  const angleRad = Math.acos(clampedCos);

  const angleDeg = (angleRad * 180) / Math.PI;
  return isNaN(angleDeg) ? 0 : angleDeg;
};

/**
 * Standard EMA to reduce jitter in keypoint streams.
 * Alpha (0.1 - 0.5) controls smoothing intensity.
 */
export const exponentialSmoothing = (currentFrame, previousFrame, alpha = 0.25) => {
  if (!currentFrame || !Array.isArray(currentFrame)) return currentFrame || [];
  if (!previousFrame || !Array.isArray(previousFrame) || previousFrame.length !== currentFrame.length) {
    return currentFrame;
  }

  return currentFrame.map((kp, idx) => {
    const prev = previousFrame[idx];
    if (!prev) return kp;
    return {
      ...kp,
      x: alpha * kp.x + (1 - alpha) * prev.x,
      y: alpha * kp.y + (1 - alpha) * prev.y,
      z: alpha * (kp.z || 0) + (1 - alpha) * (prev.z || 0),
      score: kp.score
    };
  });
};

/**
 * Calculates rolling standard deviation for a joint over a 30-frame window.
 * High variance (> threshold) indicates physical instability/tremors.
 */
export const detectMicroTremors = (coordinateHistoryWindow) => {
  if (!coordinateHistoryWindow || !Array.isArray(coordinateHistoryWindow) || coordinateHistoryWindow.length < 2) {
    return 0;
  }

  const n = coordinateHistoryWindow.length;
  const meanX = coordinateHistoryWindow.reduce((acc, p) => acc + (p.x || 0), 0) / n;
  const meanY = coordinateHistoryWindow.reduce((acc, p) => acc + (p.y || 0), 0) / n;
  const meanZ = coordinateHistoryWindow.reduce((acc, p) => acc + (p.z || 0), 0) / n;

  const variance = coordinateHistoryWindow.reduce((acc, p) => {
    return acc + ((p.x || 0) - meanX) ** 2 + ((p.y || 0) - meanY) ** 2 + ((p.z || 0) - meanZ) ** 2;
  }, 0) / n;

  return isNaN(variance) || variance < 0 ? 0 : Math.sqrt(variance); // Standard Deviation
};