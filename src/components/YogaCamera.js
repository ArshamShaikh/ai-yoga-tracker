import React, { useEffect, useState } from 'react';
import { View, StyleSheet, Text, ActivityIndicator } from 'react-native';
import { Camera, CameraType } from 'expo-camera';
import { cameraWithTensors } from '@tensorflow/tfjs-react-native';

// This is the Magic WebGL Wrapper that natively hooks directly into TFJS avoiding the slow JS Bridge
const TensorCamera = cameraWithTensors(Camera);

export default function YogaCamera({ children, onPoseFrame, cameraType = CameraType.front }) {
    const [hasPermission, setHasPermission] = useState(false);

    useEffect(() => {
        (async () => {
            const { status } = await Camera.requestCameraPermissionsAsync();
            setHasPermission(status === 'granted');
        })();
    }, []);

    const handleCameraStream = (images, updatePreview, gl) => {
        let isProcessing = false;
        const loop = () => {
            const nextImageTensor = images.next().value;

            if (nextImageTensor && onPoseFrame) {
                if (isProcessing) {
                    // Forcefully drop the frame if the AI hasn't finished the last one (prevents 10-second lag buffer)
                    nextImageTensor.dispose();
                    requestAnimationFrame(loop);
                } else {
                    isProcessing = true;
                    onPoseFrame(nextImageTensor).finally(() => {
                        nextImageTensor.dispose();
                        isProcessing = false;
                        requestAnimationFrame(loop);
                    });
                }
            } else {
                requestAnimationFrame(loop);
            }
        };
        loop();
    };

    if (!hasPermission) {
        return (
            <View style={styles.center}>
                <Text style={styles.text}>Awaiting Camera Permissions...</Text>
            </View>
        );
    }

    return (
        <View style={styles.container}>
            <TensorCamera
                style={StyleSheet.absoluteFill}
                type={cameraType}
                cameraTextureHeight={1920}
                cameraTextureWidth={1080}
                resizeHeight={256}
                resizeWidth={144} // 9:16 aspect ratio exactly matches the screen! Prevents vertical stretch.
                resizeDepth={3}
                onReady={handleCameraStream}
                autorender={true}
            />
            <View style={styles.overlayContainer}>
                {children}
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    container: { flex: 1, backgroundColor: '#000' },
    center: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#111' },
    text: { color: '#00ffcc', marginTop: 10, fontSize: 16, fontWeight: '600' },
    overlayContainer: { ...StyleSheet.absoluteFillObject, zIndex: 10 }
});
