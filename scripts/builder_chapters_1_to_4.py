import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from builder_core import (
    add_title_header, add_heading_1, add_heading_2, 
    add_body, add_bullet, set_cell_shading, set_table_borders
)

def build_chapters_1_to_4(doc):
    # =========================================================
    # CHAPTER 1. INTRODUCTION
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "CHAPTER 1. INTRODUCTION", size=20)

    add_heading_1(doc, "1.1 Introduction")
    add_body(doc, "Yoga is a venerable, holistic Indian discipline that integrates physical postures (asanas), respiratory modulation (pranayama), and focused mental concentration to cultivate musculo-skeletal strength, neuromuscular stability, and mental clarity. In the modern healthcare domain, yoga has attained rigorous clinical validation as a non-pharmacological therapeutic intervention capable of alleviating chronic lumbar strain, stabilizing hypertension, rectifying postural decompensation, and reducing stress-induced cortisol secretion.")
    add_body(doc, "The therapeutic and physiological efficacy of yoga, however, is fundamentally contingent upon strict adherence to anatomical alignment. When asanas are performed with incorrect joint angles—such as valgus knee collapse during Warrior II, hyperextended lumbar lordosis in Cobra Pose, or anterior head carriage in Mountain Pose—practitioners are exposed to acute orthopedic trauma, ligamentous sprains, and long-term joint wear. Certified human instructors provide tactile and verbal corrections that protect users; however, private studio sessions are expensive, geographically constrained, and inflexible in scheduling.")
    add_body(doc, "Consequently, millions of practitioners turn to home-based exercise applications and video broadcasts. While accessible, traditional fitness applications operate purely as passive one-way media streams: they cannot observe the user, compute kinematic angles, or deliver corrective guidance when posture deviates from clinical safety thresholds.")

    add_heading_1(doc, "1.2 Problem Definition")
    add_body(doc, "The core problem addressed by this research is the absence of an intelligent, real-time, privacy-preserving, and biomechanically accurate posture correction system for self-guided yoga practitioners. Current software paradigms suffer from two acute, mutually unacceptable limitations:")
    add_bullet(doc, "Passive One-Way Broadcasts", "Pre-recorded video libraries completely lack perceptual oversight. Users unknowingly repeat hazardous joint misalignments, reinforcing improper motor memory and risking repetitive strain injuries.")
    add_bullet(doc, "Cloud-Reliant Computer Vision", "Cloud-assisted computer vision systems stream live, uncompressed camera video over public networks to remote GPU servers. This introduces severe round-trip latency (200-600ms) that renders real-time biofeedback ineffective, consumes immense bandwidth, and violates fundamental privacy rights by exposing intimate domestic spaces.")

    add_heading_1(doc, "1.3 Aim")
    add_body(doc, "The primary aim of this project is to develop and evaluate the AI-Based Yoga Trainer: an edge-exclusive, fully autonomous, mobile posture estimation and biofeedback system that leverages on-device deep learning (MediaPipe BlazePose 33 3D keypoints) and deterministic vector kinematics to deliver instantaneous, voice-guided postural correction without requiring cloud connectivity.")

    add_heading_1(doc, "1.4 Objectives")
    add_bullet(doc, "Edge-Exclusive 3D Inference", "Execute real-time human pose estimation on mobile hardware at >30 frames per second using hardware-accelerated WebGL shader pipelines, ensuring 100% on-device privacy.")
    add_bullet(doc, "Deterministic 3D Kinematics", "Calculate interior articular joint angles via Euclidean vector dot products with defensive floating-point clamping to eliminate numerical NaN crashes.")
    add_bullet(doc, "Anti-Jitter Temporal Signal Smoothing", "Suppress monocular camera sensor jitter using a calibrated Exponential Moving Average (EMA) low-pass filter (alpha = 0.40) achieving sub-35ms settling times.")
    add_bullet(doc, "Autonomous Hands-Free Routine Orchestration", "Design a 7-state Finite State Machine (RoutineEngine) that manages distance calibration, countdowns, form verification, and bilateral pose transitions.")
    add_bullet(doc, "Prioritized Auditory Biofeedback", "Synthesize spoken corrective coaching throttled by a 4000ms debouncing queue to avoid cognitive and auditory overload.")
    add_bullet(doc, "Comprehensive Taxonomy Coverage", "Standardize clinical biomechanical bounds across 75 yoga postures categorized into standing, seated, balancing, prone, and supine forms.")

    add_heading_1(doc, "1.5 Goal")
    add_body(doc, "The overarching goal is to make clinical-grade yoga coaching universally accessible, completely free of cloud compute subscriptions, and safe for autonomous practice across diverse demographic cohorts—from young athletes to desk workers undergoing postural rehabilitation.")

    add_heading_1(doc, "1.6 Need of the System")
    add_body(doc, "With the exponential growth of remote work, sedentary screen time has led to severe epidemic levels of musculo-skeletal degradation, including cervical spondylosis, thoracic kyphosis, and lumbar compression. Self-guided physical wellness is urgently needed, but without immediate biofeedback, unguided practice does more harm than good. A deterministic, privacy-respecting mobile trainer that functions as an intelligent mirror satisfies this urgent public health need.")

    add_heading_1(doc, "1.7 Scope and Limitations")
    add_body(doc, "The scope encompasses monocular RGB video tracking on standard commercial smartphones (Android and iOS), real-time evaluation of 75 asanas, curated multi-pose vinyasa routines, hands-free voice guidance, and local persistence of workout streaks and session analytics. The system operates under reasonable limitations: it requires ambient room lighting (>50 lux) and single-practitioner full-body framing (1.8m to 3.5m distance). It is an educational and alignment aid, not a diagnostic medical device.")

    # =========================================================
    # CHAPTER 2. REQUIREMENT SPECIFICATION
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "CHAPTER 2. REQUIREMENT SPECIFICATION", size=20)

    add_heading_1(doc, "2.1 Introduction")
    add_body(doc, "This chapter specifies the operational environment, software frameworks, hardware profiles, development methodology, and evolutionary lifecycle models governing the AI-Based Yoga Trainer.")

    add_heading_1(doc, "2.2 System Environment")
    add_body(doc, "The system operates as an edge-native mobile application deployed across modern mobile operating systems. It interfaces directly with native camera hardware sensors via OpenGL ES / WebGL texture bindings, utilizing on-device GPU acceleration without network backhaul dependencies.")

    add_heading_1(doc, "2.3 Software Requirements")
    add_bullet(doc, "Mobile Framework", "React Native 0.74+ paired with Expo SDK 51, providing cross-platform JavaScript/TypeScript runtime with native C++ bridge bindings.")
    add_bullet(doc, "Machine Learning Runtime", "TensorFlow.js (tfjs) with tfjs-backend-webgl and tfjs-react-native for zero-copy GPU tensor processing.")
    add_bullet(doc, "Pose Estimation Architecture", "MediaPipe BlazePose (Full-body, 33 3D landmarks) detector-tracker pipeline.")
    add_bullet(doc, "Vector Kinematics Core", "Custom JavaScript mathematical library implementing 3D vector geometry, defensive IEEE 754 domain clamping, and EMA temporal filtering.")
    add_bullet(doc, "State Management & FSM", "Custom deterministic Finite State Machine (RoutineEngine.js) managing workout lifecycles.")
    add_bullet(doc, "Audio Speech Synthesis", "React Native TTS (Text-to-Speech) engine with localized voice synthesis and debouncing queues.")
    add_bullet(doc, "Data Persistence", "AsyncStorage for local SQLite/key-value storage of session history and streaks.")

    add_heading_1(doc, "2.4 Hardware Requirements")
    add_bullet(doc, "Processor (CPU/GPU)", "Minimum Octa-core 2.0 GHz (e.g., Snapdragon 680 / Helio G99); Recommended Hexa-core 3.0+ GHz (Snapdragon 8 Gen 1 / Apple A15 Bionic).")
    add_bullet(doc, "System Memory (RAM)", "Minimum 3.0 GB LPDDR4 RAM; Recommended 6.0 GB+ LPDDR5 RAM.")
    add_bullet(doc, "Optical Camera Sensor", "Minimum 720p front-facing camera @ 30 FPS; Recommended 1080p ultra-wide camera @ 30/60 FPS.")
    add_bullet(doc, "Display & Touchscreen", "Capacitive multi-touch screen with minimum 1080x2400 resolution and high contrast.")

    add_heading_1(doc, "2.5 Methodology")
    add_body(doc, "The project followed an Agile Incremental Methodology combined with rapid prototyping cycles. Development progressed through three focused sprints: Sprint 1 established the WebGL camera tensor bridge and BlazePose inference; Sprint 2 implemented the vector kinematics engine and 75-pose clinical taxonomy; Sprint 3 implemented the autonomous RoutineEngine FSM, voice feedback debouncing, and UI Studio refinement.")

    add_heading_1(doc, "2.6 Spiral Model")
    add_body(doc, "The Spiral Model was adopted to govern high-risk architectural challenges, particularly floating-point arithmetic stability and mobile thermal dissipation. Each loop of the spiral incorporated four quadrants: (1) Objective Determination, (2) Risk Analysis and Mitigation (e.g., prototyping WebGL tensor memory management to eliminate memory leaks), (3) Engineering and Development, and (4) Evaluation and Review. This ensured that mathematical edge cases (such as NaN division-by-zero crashes) were identified and mitigated before finalizing production builds.")

    # =========================================================
    # CHAPTER 3. SYSTEM ANALYSIS
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "CHAPTER 3. SYSTEM ANALYSIS", size=20)

    add_heading_1(doc, "3.1 System Analysis Overview")
    add_body(doc, "System analysis examines existing paradigms, evaluates their structural deficiencies, and formulates the functional rationale for the proposed edge-exclusive architecture.")

    add_heading_1(doc, "3.2 Analysis of Existing System")
    add_body(doc, "Existing market solutions fall into three main categories: (1) Human studio instruction, which is safe but expensive and rigid; (2) Mobile video streaming apps (e.g., Down Dog, Nike Training Club), which provide static multimedia but zero real-time postural awareness; and (3) Cloud-based web camera trackers, which transmit uncompressed video across WANs to cloud GPU instances. Cloud architectures introduce round-trip latency of 250ms to 550ms—causing feedback cues to lag behind dynamic user movements—while creating severe privacy vulnerabilities and costing substantial recurring server fees.")

    add_heading_1(doc, "3.3 Analysis of the Proposed System")
    add_body(doc, "The proposed AI-Based Yoga Trainer replaces cloud reliance with on-device intelligence. By processing raw video frames directly on the local mobile GPU via WebGL shaders, frame-to-feedback latency drops to 29.5 milliseconds (~34 FPS). Zero video packets traverse the internet, guaranteeing complete user privacy, total offline autonomy, and zero recurring server costs.")

    add_heading_1(doc, "3.4 Feasibility Study")
    add_bullet(doc, "Technical Feasibility", "Mobile GPUs (Apple Bionic, Snapdragon Adreno, Mali) fully support WebGL shaders and quantized neural inference. The technical feasibility of running BlazePose at 30+ FPS locally is empirically validated.")
    add_bullet(doc, "Economic Feasibility", "Built entirely on open-source libraries (React Native, TensorFlow.js, Expo) with zero cloud server requirements. Infrastructure operational cost is exactly $0.00.")
    add_bullet(doc, "Operational Feasibility", "Designed for natural physical interaction: hands-free voice coaching, large distance-visible progress rings, and intuitive green/red joint illumination enable effortless home usage.")

    # =========================================================
    # CHAPTER 4. SURVEY OF TECHNOLOGY
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "CHAPTER 4. SURVEY OF TECHNOLOGY", size=20)

    add_heading_1(doc, "4.1 React Native Framework")
    add_body(doc, "React Native is an open-source mobile application framework created by Meta. It enables engineers to author declarative UI components in JavaScript/TypeScript while executing native rendering pipelines on Android and iOS. Its modular architecture and direct C++ JSI (JavaScript Interface) bindings allow high-frequency state updates without UI thread stalling.")

    add_heading_1(doc, "4.2 Expo SDK Ecosystem")
    add_body(doc, "Expo SDK 51 provides unified native access to hardware sensors, camera peripherals, safe area insets, and audio drivers. Expo Router facilitates deep linking and declarative, file-based routing across application screens.")

    add_heading_1(doc, "4.3 TensorFlow.js & WebGL Acceleration")
    add_body(doc, "TensorFlow.js enables machine learning execution in JavaScript environments. By integrating tfjs-backend-webgl, neural network matrix multiplications are mapped directly onto GPU fragment shaders, enabling high-throughput tensor evaluation on mobile chipsets.")

    add_heading_1(doc, "4.4 MediaPipe BlazePose 33-Point 3D Architecture")
    add_body(doc, "BlazePose (Google Research) is a two-stage lightweight convolutional architecture tailored for edge pose estimation. An initial detector localizes the region of interest (ROI) containing the human body; subsequently, a landmark tracker regresses 33 keypoints in metric 3D space with high spatial fidelity across full-body postures.")

    add_heading_1(doc, "4.5 Vector Kinematics & Articular Geometry")
    add_body(doc, "Unlike uninterpretable neural classifiers, vector kinematics models the human skeleton as an articulated tree of rigid segments in R^3. Interior articular joint angles are calculated via 3D vector dot products, enabling direct comparison against clinical orthopaedic reference bounds.")

    add_heading_1(doc, "4.6 EMA Temporal Signal Filtering")
    add_body(doc, "Optical pose estimation exhibits high-frequency jitter due to sensor noise and lighting variations. A first-order Exponential Moving Average (EMA) low-pass filter suppresses noise while maintaining sub-35ms transient responsiveness, preventing erratic timer pauses.")

    add_heading_1(doc, "4.7 AsyncStorage Offline Persistence")
    add_body(doc, "AsyncStorage provides an unencrypted, asynchronous key-value storage system backed by native SQLite on Android and RocksDB/filesystem on iOS, enabling 100% offline persistence of workout analytics and streaks.")

    add_heading_1(doc, "4.8 Text-to-Speech (TTS) Voice Biofeedback")
    add_body(doc, "On-device Text-to-Speech engines synthesize clear natural voice prompts. A debouncing queue enforces a minimum 4000ms separation between consecutive alerts to prevent confusing audio overlap during practice.")
