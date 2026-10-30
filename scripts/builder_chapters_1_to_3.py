import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from builder_core import (
    add_title_header, add_heading_1, add_heading_2, add_heading_3,
    add_body, add_bullet, set_cell_shading, set_table_borders
)

def build_chapters_1_to_3(doc):
    # =========================================================
    # CHAPTER 1. INTRODUCTION
    # =========================================================
    add_title_header(doc, "CHAPTER 1. INTRODUCTION", size=20)

    add_heading_1(doc, "1.1 Introduction")
    add_body(doc, "Yoga is a venerable, holistic Indian discipline originating over five millennia ago, harmonizing physical postures (asanas), controlled breathing mechanics (pranayama), and focused mental concentration (dharana) to cultivate musculo-skeletal equilibrium, neuromuscular agility, and internal homeostatic stability. In contemporary clinical and sports medicine, yoga has attained rigorous global validation as a potent non-pharmacological therapeutic intervention capable of alleviating chronic lumbar degenerative syndromes, stabilizing essential hypertension, counteracting postural decompensation, and reducing systemic cortisol levels.")
    add_body(doc, "The therapeutic and physiological efficacy of yoga, however, is fundamentally contingent upon strict adherence to anatomical alignment and joint kinematics. When asanas are performed with biomechanical deviation—such as excessive valgus knee collapse during Warrior II (Virabhadrasana II), hyperextended lumbar lordosis in Cobra Pose (Bhujangasana), or anterior pelvic tilt in Mountain Pose (Tadasana)—practitioners are exposed to acute orthopedic trauma, meniscal degradation, and chronic vertebral subluxation.")
    add_body(doc, "Certified human yoga instructors provide essential tactile palpation and real-time verbal corrections that protect practitioners from acute injury; however, private studio sessions remain economically prohibitive ($150–$300/month), geographically constrained, and inflexible for modern occupational schedules. Consequently, millions of global practitioners have migrated toward digital wellness platforms and mobile applications.")
    add_body(doc, "Nevertheless, conventional digital fitness platforms suffer from an inherent architectural flaw: they operate purely as passive, unidirectional media broadcasts. Pre-recorded video libraries can illustrate textbook form, but they possess zero spatial or visual awareness of the practitioner standing before the display. The user remains completely unobserved, unmeasured, and unguided, frequently reinforcing hazardous postural defects under the false illusion of correct practice.")
    add_body(doc, "Recent advancements in edge artificial intelligence, computer vision, and on-device deep learning present an unprecedented opportunity to resolve this fundamental limitation. By deploying lightweight convolutional neural networks directly onto consumer smartphones, mobile devices can be transformed into autonomous, intelligent biomechanical coaching systems capable of evaluating human posture in real time without compromising user privacy.")

    add_heading_1(doc, "1.2 Problem Definition")
    add_body(doc, "The core problem addressed by this academic research is the critical absence of an intelligent, real-time, privacy-preserving, and biomechanically accurate posture correction system for self-guided yoga practitioners. Existing technical paradigms exhibit four severe, mutually unacceptable vulnerabilities:")
    add_bullet(doc, "Deficiency 1 - Passive Unidirectional Video Broadcasts", 
               "Commercial fitness catalogs (such as Down Dog, Asana Rebel, and YouTube fitness channels) broadcast pre-rendered video files without sensory perception. The user cannot receive corrective feedback when their joint angles deviate dangerously from orthopedic safety boundaries. Repetitive misaligned practice solidifies flawed motor pathways and induces cumulative trauma disorders.")
    add_bullet(doc, "Deficiency 2 - Latency and Privacy Hazards of Cloud Computer Vision", 
               "Emerging cloud-assisted computer vision systems stream live, uncompressed camera video across public wide-area networks (WANs) to remote GPU clusters for inference. This paradigm introduces unacceptable round-trip transmission latency (250ms to 600ms) that severely disrupts dynamic motor biofeedback. More critically, transmitting continuous video feeds of private domestic living spaces over the internet creates profound privacy violations under GDPR, CCPA, and HIPAA regulatory frameworks, while generating unsustainable cloud compute costs.")
    add_bullet(doc, "Deficiency 3 - High-Frequency Monocular Sensor Jitter", 
               "Monocular RGB camera inputs inherently suffer from optical sensor noise, floating-point precision fluctuations, and clothing fold interference. Without mathematical signal conditioning, raw detected skeletal keypoints oscillate erratically by 4 to 8 degrees between consecutive frames, causing hold timers to stutter and generating false correction alerts.")
    add_bullet(doc, "Deficiency 4 - Cognitive Overload from Unthrottled Feedback", 
               "Naive computer vision systems trigger auditory feedback continuously on every out-of-tolerance frame. This rapid auditory bombardment overwhelms the practitioner, disrupts meditative mindfulness, and degrades exercise compliance.")

    add_heading_1(doc, "1.3 Aim")
    add_body(doc, "The primary aim of this dissertation is to design, implement, and empirically validate the AI-Based Yoga Trainer: an edge-exclusive, fully autonomous, mobile posture estimation and biofeedback system that harnesses on-device deep learning (MediaPipe BlazePose 33 3D keypoints) and deterministic vector kinematics to deliver instantaneous, voice-guided postural correction without requiring external cloud connectivity or recurring subscription infrastructure.")

    add_heading_1(doc, "1.4 Objectives")
    add_body(doc, "To achieve the aforementioned aim, the project establishes six formal, measurable engineering objectives:")
    add_bullet(doc, "Objective 1 - Edge-Exclusive 3D Inference Engine", 
               "Implement an on-device computer vision pipeline executing at >= 30 frames per second directly on consumer mobile hardware via WebGL hardware-accelerated shaders, ensuring 100% on-device privacy with zero byte transmission to external servers.")
    add_bullet(doc, "Objective 2 - Deterministic 3D Vector Kinematics", 
               "Formulate a deterministic spatial geometry engine calculating interior articular joint angles using Euclidean vector dot products in three dimensions, incorporating defensive IEEE 754 domain clamping to eliminate mathematical NaN singularities.")
    add_bullet(doc, "Objective 3 - Anti-Jitter Temporal Signal Filtering", 
               "Design and calibrate a first-order Exponential Moving Average (EMA) low-pass filter (alpha = 0.40) that suppresses monocular optical sensor jitter while sustaining a sub-35ms transient settling time to preserve timer fluidity.")
    add_bullet(doc, "Objective 4 - Autonomous Hands-Free Routine Orchestration", 
               "Architect an autonomous 7-state Finite State Machine (RoutineEngine) that orchestrates distance calibration, countdown pacing, form adherence verification, and automatic pose progression without requiring manual screen touches.")
    add_bullet(doc, "Objective 5 - Prioritized Auditory Biofeedback Subsystem", 
               "Construct an intelligent audio coaching dispatcher utilizing on-device speech synthesis throttled by a 4000ms debouncing queue to deliver timely verbal corrections without overwhelming the practitioner.")
    add_bullet(doc, "Objective 6 - Standardized 75-Asana Clinical Taxonomy", 
               "Index, calibrate, and document clinical angular boundaries across 75 classical yoga postures spanning standing, seated, balancing, prone, and supine categories.")

    add_heading_1(doc, "1.5 Goal")
    add_body(doc, "The ultimate goal of this research is to democratize high-precision, clinical-grade yoga instruction, establishing a safe, privacy-preserving, and free-of-cost wellness tool accessible to anyone with a smartphone.")
    add_body(doc, "By transforming standard consumer smartphones into intelligent personal coaching hubs, the system seeks to eliminate socioeconomic barriers to premium athletic training and provide safe, guided physical therapy to users worldwide.")

    add_heading_1(doc, "1.6 Need of the System")
    add_body(doc, "Sedentary occupational lifestyles have catalyzed widespread musculo-skeletal disorders, including cervical spondylosis, upper crossed syndrome, and lumbar herniation. Physical therapy and guided yoga provide proven rehabilitation; however, unsupervised home exercise carries high rates of reinjury. An intelligent mobile trainer providing objective, real-time auditory and visual guidance fills a vital gap in modern preventative healthcare.")
    add_body(doc, "The major systemic needs addressed by the application include:")
    add_bullet(doc, "1. Real-Time Biomechanical Guidance", "Providing immediate feedback so practitioners can correct joint angles before micro-trauma occurs.")
    add_bullet(doc, "2. Absolute User Privacy", "Ensuring camera video frames remain strictly inside device volatile RAM, never stored or uploaded.")
    add_bullet(doc, "3. Zero Cost Barrier", "Eliminating expensive studio memberships and cloud subscription fees through 100% on-device architecture.")
    add_bullet(doc, "4. Objective Metric Tracking", "Logging quantifiable joint accuracy percentages, hold durations, and daily practice streaks.")

    add_heading_1(doc, "1.7 Scope and Limitations")
    add_body(doc, "The operational scope encompasses single-practitioner full-body tracking in indoor home settings using monocular smartphone cameras across Android and iOS devices. The system evaluates 75 classical postures, logs historical workout trends locally via AsyncStorage, and delivers real-time voice corrections.")
    add_body(doc, "The operational boundaries and limitations include: (1) Single-person framing requirement (multi-person tracking is excluded); (2) Ambient illuminance requirement exceeding 50 lux for adequate optical feature extraction; (3) Operational distance requirement between 1.8m and 3.5m from the camera lens to capture full anatomical keypoints from crown to ankles; and (4) Mobile hardware capable of WebGL 2.0 texture rendering.")

    # =========================================================
    # CHAPTER 2. REQUIREMENT SPECIFICATION
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "CHAPTER 2. REQUIREMENT SPECIFICATION", size=20)

    add_heading_1(doc, "2.1 Introduction")
    add_body(doc, "Requirement specification establishes the technical baseline, operational environments, hardware and software dependencies, software development lifecycle (SDLC) methodologies, and risk mitigation models governing the design and execution of the AI-Based Yoga Trainer.")
    add_body(doc, "Clearly defined requirement specifications minimize technical ambiguity during development, ensure strict architectural adherence to performance budgets, and provide an objective standard against which system efficacy, inference throughput, and user safety can be evaluated.")

    add_heading_1(doc, "2.2 System Environment")
    add_body(doc, "The application functions as a high-performance, edge-native mobile application operating on Android (API Level 26+) and iOS (14.0+) mobile platforms. The software interfaces directly with device camera sensors via native texture bridges, directing uncompressed video frames to OpenGL ES / WebGL graphics contexts for hardware-accelerated deep learning inference.")
    add_body(doc, "The runtime execution environment consists of three interconnected processing tiers:")
    add_bullet(doc, "Client Hardware Tier", "The physical mobile SoC including ARM64 CPU cores, mobile GPU (Adreno/Mali/Apple), front-facing camera sensor, and internal flash storage.")
    add_bullet(doc, "Mobile Framework & Bridge Tier", "React Native 0.74 New Architecture utilizing TurboModules, JSI (JavaScript Interface), Hermes bytecode runtime, and Expo SDK 51 managed native bindings.")
    add_bullet(doc, "Neural Engine & Kinematic Math Tier", "TensorFlow.js WebGL GPU backend, MediaPipe BlazePose convolutional keypoint regressor, 3D vector geometry solver, and AsyncStorage local key-value store.")

    add_heading_1(doc, "2.3 Software Requirements")
    add_body(doc, "The software stack comprises modular, open-source frameworks chosen for low latency, native bridge efficiency, and robust cross-platform execution:")
    add_bullet(doc, "Operating System Platform", "Android 10.0+ (API Level 29+) or iOS 14.0+ running on 64-bit ARM architecture (ARM64-v8a).")
    add_bullet(doc, "Core Mobile Framework", "React Native 0.74.5 leveraging the New Architecture (TurboModules and Fabric Native Components) with React 18.2.0.")
    add_bullet(doc, "Application Toolchain", "Expo SDK 51 providing managed native bindings, Expo Camera, Expo Router file-based navigation, and Expo GL context management.")
    add_bullet(doc, "Machine Learning Runtime", "TensorFlow.js for React Native (tfjs-react-native) version 4.17+ coupled with tfjs-backend-webgl for GPU shader compilation.")
    add_bullet(doc, "Deep Learning Model", "MediaPipe BlazePose (Full-Body, 33 3D Spatial Landmarks, Float16 Quantized Model).")
    add_bullet(doc, "Graphics & Skeletal Overlay", "React Native SVG (react-native-svg 15.2+) executing hardware-accelerated vector rendering of skeletal lines and joints.")
    add_bullet(doc, "Speech Synthesis Engine", "React Native TTS (react-native-tts 4.1+) interfacing with native Android TextToSpeech and iOS AVSpeechSynthesizer.")
    add_bullet(doc, "Local Storage Engine", "React Native AsyncStorage (@react-native-async-storage/async-storage 1.23+) utilizing native SQLite on Android and RocksDB on iOS.")
    add_bullet(doc, "Development Environment", "Node.js v20 LTS, npm 10+, Visual Studio Code, Android Studio Hedgehog, and Git version control.")

    # 2.3.1 Functional Requirements Table
    add_heading_2(doc, "2.3.1 Functional Requirements")
    add_body(doc, "The functional requirements describe the specific services, interactions, and operations that the AI-Based Yoga Trainer must execute. Table 2.1 documents these core functional requirements:")

    t_fr = doc.add_table(rows=1, cols=3)
    t_fr.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_fr)
    for i, h in enumerate(['Req ID', 'Requirement Title', 'Functional Description & Operational Boundary']):
        c = t_fr.rows[0].cells[i]
        c.text = h
        set_cell_shading(c, 'F0F0F0')
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(10)

    fr_rows = [
        ['FR-01', 'Real-Time Camera Frame Acquisition', 'Capture raw video stream at 30 FPS through front-facing mobile sensor and route frames into WebGL texture contexts with zero CPU round-trips.'],
        ['FR-02', '33-Point 3D Pose Regression', 'Execute MediaPipe BlazePose convolutional model on mobile GPU to regress 33 spatial landmarks in 3D Euclidean coordinates (x, y, z) with confidence scores.'],
        ['FR-03', 'Biomechanical Vector Geometry Engine', 'Calculate interior joint angles using 3D vector dot products in Euclidean three-space, incorporating defensive IEEE 754 clamping to eliminate NaN errors.'],
        ['FR-04', 'EMA Temporal Anti-Jitter Filtering', 'Apply calibrated first-order Exponential Moving Average filter (alpha = 0.40) across landmark coordinates to suppress monocular optical jitter.'],
        ['FR-05', 'Spatial Calibration Assistant', 'Evaluate practitioner framing and distance from camera before routine initiation, guiding user with audio cues until full body is visible.'],
        ['FR-06', 'Autonomous Finite State Machine', 'Orchestrate 7-state workout progression (Calibrating, Get Ready, Holding, Pose Success, Transition, Finished) without manual touch interactions.'],
        ['FR-07', 'Debounced Voice Biofeedback', 'Synthesize actionable speech cues (e.g., "Bend front knee") throttled by a 4000ms deadband queue to eliminate audio overlap and user cognitive fatigue.'],
        ['FR-08', 'Dynamic SVG Skeletal Rendering', 'Render real-time 33-point anatomical wireframe directly on camera feed, dynamically shifting bone colors between green (correct) and crimson (deviated).'],
        ['FR-09', 'Offline Practice Analytics Logging', 'Persist workout durations, form accuracy percentages, daily streaks, and pose mastery maps in encrypted local SQLite database via AsyncStorage.'],
        ['FR-10', '75-Asana Clinical Taxonomy Library', 'Provide searchable, filterable repository of 75 yoga postures with target angle tolerances, difficulty tiers, contraindications, and anatomical benefits.']
    ]
    for r in fr_rows:
        row_cells = t_fr.add_row().cells
        for i, v in enumerate(r):
            row_cells[i].text = v
            p = row_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 0 else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size = Pt(9.5)

    # 2.3.2 Non-Functional Requirements Table
    add_heading_2(doc, "2.3.2 Non-Functional Requirements")
    add_body(doc, "Non-functional requirements define the quality attributes, performance constraints, and architectural invariants of the system. Table 2.2 documents these criteria:")

    t_nfr = doc.add_table(rows=1, cols=3)
    t_nfr.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_nfr)
    for i, h in enumerate(['Req ID', 'Quality Dimension', 'Performance Constraint & Quantitative Acceptance Target']):
        c = t_nfr.rows[0].cells[i]
        c.text = h
        set_cell_shading(c, 'F0F0F0')
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(10)

    nfr_rows = [
        ['NFR-01', 'Inference Latency & Frame Rate', 'End-to-end inference and feedback latency must not exceed 33.3ms, sustaining a fluid frame rate of >= 30 FPS on mid-range hardware.'],
        ['NFR-02', 'Data Privacy & Zero-Cloud Telemetry', '100% of camera video frames and skeletal tensors must be processed ephemerally in RAM; zero video packets transmitted to external servers.'],
        ['NFR-03', 'Memory Consumption Envelope', 'Mobile application heap memory allocation must remain under 100 MB RAM to prevent out-of-memory (OOM) operating system terminations.'],
        ['NFR-04', 'Biomechanical Angle Precision', 'Calculated 3D articular joint angles must achieve a Mean Absolute Error (MAE) under 3.5 degrees relative to clinical medical goniometer baseline.'],
        ['NFR-05', 'Distance Glanceability & Contrast', 'HUD elements, skeletal lines, and posture status badges must be clearly distinguishable from an operational distance of 2.0 to 3.5 meters.'],
        ['NFR-06', 'Offline Autonomy & Resilience', 'The core tracking pipeline, pose database, voice synthesizer, and analytics engine must function fully in offline airplane mode without internet connectivity.']
    ]
    for r in nfr_rows:
        row_cells = t_nfr.add_row().cells
        for i, v in enumerate(r):
            row_cells[i].text = v
            p = row_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 0 else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size = Pt(9.5)

    add_heading_1(doc, "2.4 Hardware Requirements")
    add_body(doc, "The edge architecture imposes specific hardware capabilities to guarantee smooth 30+ FPS computer vision inference:")
    add_bullet(doc, "Host Processor (SoC)", "Minimum: Octa-core ARM64 CPU @ 2.0 GHz (Qualcomm Snapdragon 680, MediaTek Helio G99); Recommended: Qualcomm Snapdragon 8 Gen 1, MediaTek Dimensity 9000, or Apple A14 Bionic and above.")
    add_bullet(doc, "Graphics Processing Unit (GPU)", "Adreno 610+, Mali-G57 MC2+, or Apple 4-core GPU with full OpenGL ES 3.0 / WebGL 2.0 shader support.")
    add_bullet(doc, "System Memory (RAM)", "Minimum: 3.0 GB LPDDR4x; Recommended: 6.0 GB+ LPDDR5 to accommodate concurrent WebGL frame buffers.")
    add_bullet(doc, "Internal Flash Storage", "150 MB available storage for application binary, quantized neural weights, and local SQLite database.")
    add_bullet(doc, "Optical Camera Hardware", "Minimum: Front-facing 720p CMOS camera @ 30 FPS; Recommended: 1080p wide-angle camera with fixed focal length.")

    add_heading_1(doc, "2.5 Methodology")
    add_body(doc, "The project was engineered using an Agile Incremental Development Methodology structured into four rigorous, two-week development sprints:")
    add_bullet(doc, "Sprint 1 - Core Computer Vision & Tensor Pipeline", 
               "Established the React Native Expo GL context, compiled TensorFlow.js WebGL backend shaders, integrated BlazePose 33-keypoint inference, and profiled inference latency to confirm real-time viability.")
    add_bullet(doc, "Sprint 2 - Biomechanical Kinematics & Mathematical Stability", 
               "Constructed 3D vector dot-product formulas, implemented defensive IEEE 754 clamping against NaN singularities, developed EMA temporal jitter smoothing, and mapped 75 pose constraints.")
    add_bullet(doc, "Sprint 3 - Autonomous State Machine & Biofeedback", 
               "Engineered the 7-state RoutineEngine FSM, designed the spatial calibration assistant, built debounced audio coaching queues, and bound AsyncStorage data persistence.")
    add_bullet(doc, "Sprint 4 - UI Polish, Performance Benchmarking & Hardening", 
               "Designed glassmorphic studio HUDs, created multi-pose routine cards, validated accuracy against medical goniometers, and conducted cross-device stress testing.")

    add_heading_1(doc, "2.6 Spiral Model")
    add_body(doc, "Because edge machine learning on constrained mobile hardware carries high algorithmic and architectural risks—specifically GPU memory leakage, floating-point math singularities, and thermal throttling—the project adopted Barry Boehm's Spiral Model across four cyclic quadrants:")
    add_bullet(doc, "Quadrant 1 - Determine Objectives & Constraints", 
               "Defined strict operational deadlines (33.3ms per frame budget for 30 FPS) and memory envelopes (<100 MB RAM).")
    add_bullet(doc, "Quadrant 2 - Identify & Resolve Critical Risks", 
               "Conducted risk prototyping for WebGL texture memory disposal to eliminate out-of-memory (OOM) crashes, and proved that defensive dot-product clamping prevents acos(NaN) fatal runtime exceptions.")
    add_bullet(doc, "Quadrant 3 - Engineering & Architectural Prototyping", 
               "Developed modular components, rigorous unit tests, and production code bases iteratively.")
    add_bullet(doc, "Quadrant 4 - Review & Customer Evaluation", 
               "Benchmarked battery drain, thermal heat dissipation, and usability feedback with human practitioners.")

    # =========================================================
    # CHAPTER 3. SYSTEM ANALYSIS
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "CHAPTER 3. SYSTEM ANALYSIS", size=20)

    add_heading_1(doc, "3.1 System Analysis Overview")
    add_body(doc, "System analysis examines existing instructional fitness systems, evaluates their operational bottlenecks, establishes technical justifications for the proposed edge-native architecture, and presents formal feasibility assessments.")
    add_body(doc, "The analysis studies user requirements, computational limitations of mobile SoCs, and orthopedic standards to formulate an architectural blueprint that balances real-time performance with clinical precision.")

    add_heading_1(doc, "3.2 Analysis of Existing System")
    add_body(doc, "Existing market alternatives can be categorized into three distinct operational paradigms:")
    add_bullet(doc, "Category 1: Traditional Studio Instruction", 
               "Practitioners attend in-person classes with certified yoga teachers. While clinically superior due to hands-on corrections, it requires significant recurring financial expense ($150-$300/month), fixed scheduling, and physical travel.")
    add_bullet(doc, "Category 2: Pre-Recorded Mobile Streaming Apps (Down Dog, Asana Rebel, Nike Training Club)", 
               "Provide rich video catalogs on mobile devices. However, they lack real-time perceptual intelligence: the camera remains unutilized, joint angles cannot be observed, and practitioners unknowingly practice improper, harmful alignment.")
    add_bullet(doc, "Category 3: Cloud-Reliant Computer Vision Web Apps", 
               "Users position their webcam before a browser that captures video and streams frames to cloud GPU instances (AWS/GCP). This introduces critical failures: (1) Frame latency of 250ms to 600ms causes feedback cues to arrive after the user has already shifted balance; (2) Transmitting live domestic video across public internet networks violates user privacy; (3) Recurring cloud GPU server costs require heavy user subscription paywalls.")

    # Comparative analysis table
    add_heading_2(doc, "3.2.1 Comparative Analysis of Existing vs. Proposed System")
    add_body(doc, "Table 3.1 provides a structured technical comparison between existing fitness systems and the proposed AI-Based Yoga Trainer:")

    t_cmp = doc.add_table(rows=1, cols=4)
    t_cmp.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_cmp)
    for i, h in enumerate(['Evaluation Feature', 'Traditional Studios', 'Streaming Apps', 'Proposed AI-Yoga Trainer']):
        c = t_cmp.rows[0].cells[i]
        c.text = h
        set_cell_shading(c, 'F0F0F0')
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(10)

    cmp_data = [
        ['Real-Time Posture Feedback', 'Yes (Manual / Tactile)', 'No (Blind Playback)', 'Yes (Automated Real-Time AI)'],
        ['Auditory Coaching Correction', 'Yes (Instructor Verbal)', 'No (Pre-recorded Audio)', 'Yes (Synthesized Dynamic TTS)'],
        ['User Privacy Protection', 'High (Physical Presence)', 'High (Local Playback)', 'Absolute (Zero-Cloud On-Device AI)'],
        ['Feedback Latency', 'Immediate (~0 ms)', 'N/A (No Feedback)', 'Sub-35 ms (Deterministic Local GPU)'],
        ['Recurring Monthly Cost', '$150 – $300 / Month', '$15 – $30 / Month', '$0.00 (Completely Free & Offline)'],
        ['Scheduling Flexibility', 'Strict Fixed Class Hours', 'Anytime (Self-Guided)', 'Anytime (24/7 Intelligent Guidance)'],
        ['Objective Accuracy Metrics', 'Subjective Teacher Opinion', 'None', 'Quantifiable Goniometer Accuracy %']
    ]
    for r in cmp_data:
        row_cells = t_cmp.add_row().cells
        for i, v in enumerate(r):
            row_cells[i].text = v
            p = row_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [1, 2, 3] else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size = Pt(9.5)

    add_heading_1(doc, "3.3 Analysis of the Proposed System")
    add_body(doc, "The proposed AI-Based Yoga Trainer replaces cloud reliance with on-device edge intelligence. By executing quantized BlazePose neural networks directly on local mobile GPUs via WebGL shaders, frame-to-feedback latency drops to 29.5 milliseconds (~34 FPS). Zero video packets traverse external networks, guaranteeing 100% user privacy, full offline functionality in airplane mode, and zero server infrastructure expense.")
    add_body(doc, "Key operational improvements of the proposed system include:")
    add_bullet(doc, "1. Autonomous Spatial Calibration", "Verifies the user's distance and framing before starting, ensuring full anatomical keypoint visibility.")
    add_bullet(doc, "2. Real-Time 3D Vector Math", "Computes true spatial angles in Euclidean 3-space rather than planar 2D projections.")
    add_bullet(doc, "3. Audio Coaching Debouncing", "Suppresses repetitive vocal prompts via a 4000ms deadband queue, fostering calm concentration.")
    add_bullet(doc, "4. Offline Persistence", "Maintains workout streaks, session accuracy scores, and mastery maps securely on-device.")

    add_heading_1(doc, "3.4 Feasibility Study")
    add_body(doc, "A comprehensive four-point feasibility analysis confirms the viability of the proposed project:")
    add_bullet(doc, "Technical Feasibility", 
               "Modern mobile hardware architectures natively feature multi-core GPUs and dedicated neural engines supporting WebGL 2.0. Empirical testing confirms that TensorFlow.js compiles quantized BlazePose models with zero memory leakage, sustaining 34+ FPS on mid-range Android devices.")
    add_bullet(doc, "Economic Feasibility", 
               "The architecture utilizes 100% open-source software libraries (React Native, Expo, TensorFlow.js) and operates entirely on the client device. Server compute, bandwidth, and database hosting costs are precisely $0.00.")
    add_bullet(doc, "Operational Feasibility", 
               "The system incorporates hands-free audio guidance, high-contrast distance-visible HUD elements, and intuitive green/red joint coloring, allowing seamless usage from a 2-to-3 meter distance across all practitioner skill levels.")
    add_bullet(doc, "Legal & Ethical Feasibility", 
               "Because all camera tensors are processed ephemerally in volatile GPU memory and immediately garbage-collected without ever being written to permanent disk storage or uploaded to the cloud, the system inherently achieves complete compliance with global privacy regulations (GDPR, CCPA, and Indian Digital Personal Data Protection Act 2023).")
