import * as tf from '@tensorflow/tfjs';
import * as poseDetection from '@tensorflow-models/pose-detection';
import '@tensorflow/tfjs-react-native';

class PoseDetectorService {
    constructor() {
        this.detector = null;
        this.isReady = false;
    }

    async initialize() {
        try {
            // Wait for TF edge backend to be ready
            await tf.ready();

            // We use MediaPipe BlazePose 'lite' for ultra-fast, smooth mobile edge execution
            const detectorConfig = {
                runtime: 'tfjs',
                modelType: 'lite', // 'lite' runs 3-4x faster than 'full' on mobile devices
                enableSmoothing: true, // Internal tracker smoothing
            };

            this.detector = await poseDetection.createDetector(
                poseDetection.SupportedModels.BlazePose,
                detectorConfig
            );

            this.isReady = true;
            console.log('✅ BlazePose (3D) loaded successfully!');
            return true;
        } catch (error) {
            console.error('Failed to initialize BlazePose:', error);
            return false;
        }
    }

    async estimatePoses(imageTensor) {
        if (!this.isReady || !this.detector) return [];

        try {
            // Runs inference
            const poses = await this.detector.estimatePoses(imageTensor);
            return poses;
        } catch (error) {
            console.warn('Inference error:', error);
            return [];
        }
    }
}

export default new PoseDetectorService();
