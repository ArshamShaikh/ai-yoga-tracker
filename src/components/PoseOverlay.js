import React, { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import { BLAZEPOSE_CONNECTIONS, MOVENET_CONNECTIONS } from '../constants/landmarks';

const KEYPOINT_SIZE = 12;
const TENSOR_WIDTH = 144;
const TENSOR_HEIGHT = 256;

export default function PoseOverlay({ pose, invalidJoints = [], isMirrored = true }) {
    const [layout, setLayout] = useState({ width: 0, height: 0 });

    if (!pose || !pose.keypoints || pose.keypoints.length === 0) {
        return (
            <View
                style={StyleSheet.absoluteFill}
                onLayout={(event) => setLayout(event.nativeEvent.layout)}
                pointerEvents="none"
            />
        );
    }

    // Dynamic topology selection: auto-detect BlazePose (33) vs MoveNet (17)
    const connections = pose.keypoints.length >= 33 ? BLAZEPOSE_CONNECTIONS : MOVENET_CONNECTIONS;

    // Scale coordinates to the component's rendered layout (auto-detect normalized [0, 1] vs pixel coords)
    const sampleKp = pose.keypoints.find(k => k && (k.score ?? 1) >= 0.35) || pose.keypoints[0];
    const isNormalized = sampleKp && sampleKp.x <= 1.0 && sampleKp.y <= 1.0;
    const scaleX = isNormalized ? layout.width : (layout.width / TENSOR_WIDTH);
    const scaleY = isNormalized ? layout.height : (layout.height / TENSOR_HEIGHT);

    return (
        <View
            style={StyleSheet.absoluteFill}
            onLayout={(event) => setLayout(event.nativeEvent.layout)}
            pointerEvents="none"
        >
            {/* Render 3D Skeletal Bone Connections */}
            {connections.map(([p1, p2], i) => {
                const kp1 = pose.keypoints[p1];
                const kp2 = pose.keypoints[p2];
                if (!kp1 || !kp2 || kp1.score < 0.4 || kp2.score < 0.4) return null;

                const isBoneInvalid = invalidJoints.includes(p1) || invalidJoints.includes(p2);

                const ax = isMirrored ? (layout.width - (kp1.x * scaleX)) : (kp1.x * scaleX);
                const ay = kp1.y * scaleY;
                const bx = isMirrored ? (layout.width - (kp2.x * scaleX)) : (kp2.x * scaleX);
                const by = kp2.y * scaleY;

                const length = Math.hypot(bx - ax, by - ay);
                const angle = Math.atan2(by - ay, bx - ax) * (180 / Math.PI);

                return (
                    <View
                        key={`bone-${i}`}
                        style={{
                            position: 'absolute',
                            left: ax,
                            top: ay,
                            width: length,
                            height: 3.5,
                            backgroundColor: isBoneInvalid ? 'rgba(255, 87, 34, 0.75)' : 'rgba(76, 175, 80, 0.65)',
                            transformOrigin: '0% 50%',
                            transform: [{ rotate: `${angle}deg` }],
                            zIndex: 1,
                        }}
                    />
                );
            })}

            {/* Render Joint Keypoints */}
            {pose.keypoints.map((keypoint, index) => {
                if (keypoint.score < 0.4) return null;

                const isInvalid = invalidJoints && invalidJoints.includes(index);
                const renderLeft = isMirrored ? (layout.width - (keypoint.x * scaleX) - KEYPOINT_SIZE / 2) : ((keypoint.x * scaleX) - KEYPOINT_SIZE / 2);
                const renderTop = (keypoint.y * scaleY) - KEYPOINT_SIZE / 2;

                return (
                    <View
                        key={`kp-${index}`}
                        style={[
                            styles.keypoint,
                            {
                                left: renderLeft,
                                top: renderTop,
                                backgroundColor: isInvalid ? '#FF3D00' : '#4CAF50',
                                borderColor: isInvalid ? '#FF8A65' : '#FFFFFF',
                                shadowColor: isInvalid ? '#FF3D00' : '#4CAF50',
                                zIndex: 5,
                            },
                        ]}
                    />
                );
            })}
        </View>
    );
}

const styles = StyleSheet.create({
    keypoint: {
        position: 'absolute',
        width: KEYPOINT_SIZE,
        height: KEYPOINT_SIZE,
        borderRadius: KEYPOINT_SIZE / 2,
        backgroundColor: '#4CAF50',
        borderWidth: 2,
        borderColor: '#FFFFFF',
        shadowColor: '#4CAF50',
        shadowOffset: { width: 0, height: 0 },
        shadowOpacity: 0.9,
        shadowRadius: 5,
        elevation: 4,
    },
});
