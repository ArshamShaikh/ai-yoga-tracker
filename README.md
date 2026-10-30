# AI-Powered Cross-Platform Yoga Trainer App

An advanced, AI-driven yoga training application built using React Native Expo, providing real-time pose estimation and visual feedback to optimize user form.

## 🏗 System Architecture

The application is engineered as a cross-platform solution (iOS, Android, and Web) leveraging the following core stack:
- **Frontend Framework**: React Native Web with Expo to maintain a single unified codebase across all modalities.
- **Vision Integration**: `react-native-vision-camera` handles robust hardware-accelerated video streaming.
- **Machine Learning**: `@tensorflow/tfjs` and `@tensorflow-models/movenet` perform on-device inference for human pose estimation.
- **Feedback Mechanism**: Next-gen visual overlays combined with `react-native-tts` for audible form corrections.

By utilizing `@tensorflow/tfjs-react-native`, MoveNet runs entirely on the edge. This guarantees near-zero latency pose processing and absolute user privacy, as video data never leaves the device.

## 🧠 Keypoint Math & Rendering Pipeline

Real-time pose assessment is achieved through a multi-stage data pipeline that bridges our computer vision outputs directly to the layout drawing layer:

1. **Inference**: MoveNet outputs a continuous stream of 17 raw coordinate keypoints mapping the user's physical stance.
2. **Signal Filtering (`poseMathUtils.js`)**: 
   - Uses **`exponentialSmoothing`** on the raw stream to substantially reduce jitter and create a fluid tracking experience.
   - Computes biomechanic geometry using **`calculateJointAngle`** to derive localized 2D vertex angles (e.g., knee flexion, arm extension).
   - **`detectMicroTremors`** applies a rolling standard deviation to identify instability, indicating when a user is physically struggling to maintain a pose.
3. **Personalization (`CalibrationEngine.js`)**: Takes globally rigid constraints (defined safely in `poseConstraints.json`) and dynamically adjusts angle targeting and variances based on the user's initial mobility calibration profile.
4. **Canvas Layout Mapping**: The filtered, personalized keypoints and their angular relationships are piped into the application's drawing loop (Canvas/SVG). Form alignment is visually color-coded: bones matching the expected vectors turn green, while maladjusted limbs are highlighted in red to prompt immediate user correction.

## 🚀 Setup & Launch

To start the development environment locally, run the following commands:

```bash
# 1. Install all dependencies
npm install

# 2. Start the Expo development server
npm start
```

### Development Testing
Once the server is running, the terminal will present the Expo CLI:
- Press `w` to launch the **Web** client in your browser.
- Press `a` to test on an **Android** emulator/device.
- Press `i` to test on an **iOS** simulator.
