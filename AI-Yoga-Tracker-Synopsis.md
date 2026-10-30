# RIZVI COLLEGE OF ARTS, SCIENCE AND COMMERCE
*(Affiliated to University of Mumbai)*
MUMBAI – MAHARASHTRA – 400050

**DEPARTMENT OF COMPUTER SCIENCE**

**MINI PROJECT SYNOPSIS**
On
**AI YOGA TRACKER**
*(AI-Powered Real-Time Posture Correction Application)*

Submitted in Partial Fulfilment of the Requirements for the Award of the Degree of
**BACHELOR OF SCIENCE (COMPUTER SCIENCE)**
SEM V

By
**Arsham** *(Replace with full name if needed)*
Roll No. [Your Roll No]

Under the Esteemed Guidance of
**[Guide Name]**
Assistant Professor

**2026 – 2027**

---

## AI YOGA TRACKER
**Mini Project Synopsis**

### 1. Problem Statement
Yoga is a highly effective practice for physical and mental health; however, performing poses with incorrect form can lead to severe muscle strain, joint injuries, and long-term spinal degradation. Most practitioners rely on pre-recorded videos or static images, which offer zero real-time correction. Live instructors are expensive and inaccessible to the majority of people.

Current mobile applications in the fitness market typically fall into two categories:
1. **Video/VOD Platforms**: Apps that provide follow-along videos but lack interactive visual tracking.
2. **Delayed Server-Side Trackers**: Apps that stream video frames to a cloud server for AI inference, resulting in high latency, data privacy concerns, and laggy feedback.

There is a critical need for an intelligent, offline-capable application that can parse complex human geometry in real-time, completely on-device, offering instant dynamic feedback to correct user posture safely and privately.

### 2. Proposed Solution
The **AI Yoga Tracker** is an end-to-end, mobile-first application built using **React Native (Expo)** in combination with **TensorFlow.js (MoveNet)**. It leverages native device cameras and C++ Frame Processors to perform complex skeletal geometry math directly on the user’s smartphone CPU/GPU, eliminating the need for cloud servers.

| Component | Primary Functions | Integrated Systems |
| :--- | :--- | :--- |
| **Vision Engine** | Frame extraction, Native Buffer passing | Expo Camera, WebGL Tensors |
| **AI Inference** | Live skeletal keypoint generation | TensorFlow.js, MoveNet Lightning |
| **Feedback Engine** | Math utilities, Pose variance calculations | poseMathUtils.js, React Native TTS |
| **UI/UX Layer** | Interactive selection grids, deep-linking | Expo Router (Next.js style routing) |

**Key Differentiators & Technical Pillars**
* **Local Machine Learning**: Completely bypasses the slow JavaScript bridge by using **WebGL** via TensorCamera to compute frames securely in the native layer (60+ FPS).
* **Mathematical Intelligence**: Extracts the 17-point raw skeleton and calculates internal limb flexion angles using vector dot-products to determine if a joint is overextended.
* **Dynamic TTS Engine (Text-To-Speech)**: Maps out-of-bounds joint limits to specific vocal feedback commands (e.g., *"Straighten your front knee slightly"*), effectively acting as a live intelligent coach.
* **Responsive Visual Mapping**: Synchronizes normalized strict Tensor boundaries to dynamic fluid CSS screen dimensions using custom layout tracking.

### 3. Core Features
#### 3.1 The Intelligence Engine
* **6-Pose Foundational Blueprint**: Structurally tracks highly specific joint groups across 6 strategic poses (Tree Pose, Triangle Pose, Cobra Pose, Downward Dog, Warrior I, and Meditation Calibration).
* **Trailing Jitter Reduction**: Integrates an aggressive `exponentialSmoothing()` algorithmic filter over the model's raw output to prevent the visual nodes from bouncing wildly during low-light inference.
* **Vector Mathematics Validation**: Checks real-time limb flexion against dynamically allocated variance ranges specified inside the constraint matrix memory map.

#### 3.2 The User Experience
* **Voice-Command Correction**: Real-time synthesized audio feedback dynamically alerts the user when their form dips below established safety thresholds. 
* **Dynamic UI Dashboard**: Built on `expo-router`, featuring bottom-bar navigation and highly aesthetic cards tracking the user's selected session.
* **Neon Visual Skeletons**: Paints dynamic glowing vector nodes exactly tracing the user’s physical geometry directly on the smartphone screen.

### 4. Technology Stack
The following technologies have been selected for the heavily optimized performance architecture:

| Component | Technology / Library |
| :--- | :--- |
| **Framework** | React Native (Expo SDK) |
| **Machine Learning Model** | TensorFlow.js / MoveNet (Lightning) |
| **Routing / Navigation** | Expo Router |
| **Hardware Access** | Expo Camera (WebGL Tensor Hook) |
| **Audio Core** | React Native TTS |
| **UI Assets / Icons** | FontAwesome5 (@expo/vector-icons) |
| **Native Storage** | React Native Async Storage |

### 5. Expected Outcome
Upon completion, the AI Yoga Tracker delivers a complete, production-ready solution addressing the lack of cheap, private structural coaching.
* **Performance Superiority**: Achieves real-time inference without cloud costs, validating the feasibility of deep-learning algorithms embedded in standard hardware.
* **Safety & Correction**: Significantly reduces the likelihood of yoga injuries through instantaneous audio feedback.
* **Codebase Quality**: A modular, mathematically isolated React Native codebase adhering to modern high-performance JSI / C++ Worklet standards.

### 6. Project Scope & Development Approach
The project is developed using a hardware-first approach, prioritizing the stability of the neural network inside the React Native thread before expanding the aesthetics.
* **Phase 1**: Resolving C++ Native Peer Dependencies and WebGL Expo configuration. 
* **Phase 2**: Integrating the TensorFlow Model array loops and the geometric dot-product math algorithms.
* **Phase 3**: Creating the TTS Engine mapping boundaries against constraints and creating the responsive UI scaling matrix.
* **Phase 4**: Scaffolding the `expo-router` aesthetic dashboard targeting the 6 distinct foundational poses and UX polish.
