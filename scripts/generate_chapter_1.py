import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = docx.Document()

# Page Margins - Standard for University of Mumbai thesis
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25) # 1.25 in for left gutter binding
    section.right_margin = Inches(1.0)

# Set base style font to Times New Roman
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
font.color.rgb = RGBColor(0x22, 0x22, 0x22)
style.paragraph_format.line_spacing = 1.5
style.paragraph_format.space_after = Pt(6)

def add_chapter_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(24)
    p.paragraph_format.space_after = Pt(18)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x00, 0x20, 0x60) # Deep academic navy

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x11, 0x11, 0x11)

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

def add_body(text):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

def add_bullet(bold_prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_bold = p.add_run(bold_prefix + ': ')
    r_bold.font.name = 'Times New Roman'
    r_bold.font.bold = True
    r_text = p.add_run(text)
    r_text.font.name = 'Times New Roman'

add_chapter_title('CHAPTER 1\nINTRODUCTION')

add_heading_1('1.1 Background and Context of the Study')
add_body('Yoga is an ancient mind-body discipline that originated over five thousand years ago in northern India, characterized by a holistic synthesis of physical postures (asanas), controlled pranayama breathing, and focused mental meditation. In the twenty-first century, the global wellness landscape has witnessed an unprecedented resurgence in yoga practice, propelled by pervasive public health awareness, clinical validations of stress alleviation, and the modern transition toward sedentary digital lifestyles. Millions of practitioners worldwide participate in daily yoga routines to counteract musculoskeletal disorders, enhance cardiovascular endurance, correct postural misalignments, and cultivate emotional equanimity.')

add_body('Despite its profound therapeutic and athletic benefits, yoga is intrinsically an isometric and biomechanically demanding practice. Each posture requires precise articular joint alignment, balanced torque distribution across spinal vertebrae, and coordinated engagement of stabilizing muscle groups. When an asana is executed with flawed spatial orientation—such as knee valgus in standing lunges, hyperextension of lumbar discs in backbends, or improper scapular retraction in arm balances—the positive physiological benefits transform into severe clinical risks. Repetitive strain injuries (RSIs), torn meniscus ligaments, chronic cervical spondylosis, and sacroiliac joint dysfunctions represent frequent clinical outcomes among practitioners attempting unsupervised home regimens.')

add_body('Traditionally, safe mastery of yoga necessitated an in-person, master-apprentice paradigm where a certified human guru or instructor maintained continuous visual surveillance, providing verbal guidance and physical touch adjustments. However, in the modern socio-economic environment, personalized one-on-one yoga instruction is financially cost-prohibitive for the vast majority of practitioners and geographically constrained by urban commuting logistics. Consequently, over eighty percent of modern home practitioners rely on pre-recorded Video-on-Demand (VOD) channels, mobile video libraries, or static fitness charts. While visually informative, these passive modalities suffer from a critical systemic flaw: they offer zero feedback. A practitioner staring at a video screen cannot accurately assess their own spatial geometry in three dimensions, fostering a dangerous illusion of competence while reinforcing biomechanical defects.')

add_body('Recent paradigm shifts in Edge Artificial Intelligence (Edge AI), embedded Computer Vision (CV), and high-throughput mobile neural processing units (NPUs) present a transformative opportunity to bridge this divide. By harnessing deep-learning landmark detectors operating directly on consumer smartphones, it is now computationally feasible to convert an ordinary mobile camera into an intelligent, real-time biomechanical analysis engine capable of tracking human kinematics and synthesizing instantaneous audio-visual corrective coaching.')

add_heading_1('1.2 Problem Statement')
add_body('The prevailing methodologies for digital yoga learning and computer-vision-assisted physical fitness exhibit severe functional deficiencies that limit their clinical safety and commercial practicality. Specifically, modern approaches suffer from the following fundamental bottlenecks:')

add_bullet('Lack of Real-Time Biofeedback in VOD Platforms', 'Conventional digital fitness platforms (such as YouTube, pre-recorded subscription apps, and instructional fitness portals) are fundamentally broadcast mediums. They possess no spatial perception of the learner. The user is forced to divide their visual attention between executing complex physical contortions and glancing sideways at a display, often severely compromising cervical spine alignment and exacerbating injury hazards.')

add_bullet('Severe Latency and Privacy Degradation in Cloud-Based AI Architectures', 'Early attempts at AI-assisted fitness coaching predominantly employed a client-server architecture, streaming raw video feeds over HTTP or WebSockets to cloud-hosted GPU clusters for deep learning inference. This architectural paradigm introduces prohibitive round-trip network latency (often exceeding 600 to 1200 milliseconds), completely shattering the sub-100-millisecond threshold required for instantaneous muscle-memory feedback. Furthermore, continuously broadcasting live unencrypted video feeds of private living rooms and personal bodies to remote corporate servers presents unacceptable privacy hazards and violates stringent contemporary data protection mandates (such as GDPR, CCPA, and HIPAA).')

add_bullet('Inherent Failures of Monocular 2D Pose Estimation Models', 'Legacy fitness applications predominantly utilize 2D keypoint estimators (such as OpenPose or baseline MoveNet) which project human landmarks onto a flat Cartesian coordinate system (X and Y coordinates only). While adequate for simple planar motions, 2D estimators catastrophically fail in yoga. Yoga poses frequently require complex spatial rotations, lateral twists, seated binds, and physical self-occlusion (for example, in Marichyasana, Virabhadrasana III, or Ardha Matsyendrasana where limbs cross behind the torso or project directly toward the camera axis). In flat 2D projection, occluded joints disappear or produce chaotic visual jitter, causing erroneous evaluation scores and inaccurate coaching feedback.')

add_body('Consequently, there exists an acute academic and technological imperative to engineer an intelligent, offline-first mobile application that operates strictly on-device, reconstructs full 3D skeletal topology, calculates rigorous biomechanical flexion vectors in real time, and synthesizes low-latency verbal and visual coaching.')

add_heading_1('1.3 Motivation & Rationale')
add_body('The motivation behind the AI-Based Yoga Trainer originates from three primary dimensions: technological feasibility, social democratisation of health, and preventative biomechanical safety.')

add_bullet('Democratization of Elite Wellness Coaching', 'Personal certified yoga trainers charge upwards of $50 to $100 per hour, rendering individualized guidance an elite luxury inaccessible to students, desk-bound workers, and budget-conscious demographics. An on-device AI coach provides unlimited, on-demand, personalized posture auditing at zero marginal operational cost, democratizing preventative wellness globally.')

add_bullet('Absolute Guarantee of User Privacy (Edge Computing)', 'Physical exercise within one’s private living quarters constitutes sensitive, intimate personal data. By designing an edge-exclusive computational pipeline that executes MediaPipe BlazePose and vector mathematical engines strictly inside local smartphone memory and WebGL hardware buffers—with zero byte transmission over the public internet—the application guarantees inviolable user confidentiality by design.')

add_bullet('Preventative Healthcare and Musculoskeletal Longevity', 'Musculoskeletal disorders resulting from poor physical posture and repetitive sedentary strain represent one of the leading global causes of chronic pain and workplace absenteeism. By providing millisecond-accurate acoustic coaching cues (e.g., prompting a user to engage the quadriceps or decompress the lumbar spine), the application prevents acute joint hyperextensions while systematically educating practitioners on functional anatomy.')

add_heading_1('1.4 Objectives of the Project')
add_body('The central objective of this research and engineering initiative is to develop, evaluate, and deploy a production-grade, on-device mobile AI application capable of real-time 3D pose estimation, mathematical posture constraint evaluation, multi-pose routine management, and intelligent acoustic-visual biofeedback.')

add_heading_2('1.4.1 Primary Objectives')
add_bullet('1. Real-Time 3D Spatial Landmark Tracking', 'Integrate MediaPipe BlazePose via TensorFlow.js on mobile hardware to continuously extract 33 distinct anatomical landmarks in three dimensions (X, Y, and depth coordinate Z), achieving stable 25+ FPS edge inference on commodity smartphone CPUs/GPUs without external cloud dependencies.')

add_bullet('2. Deterministic Biomechanical Rules Engine', 'Develop an O(1) computational geometric pipeline capable of calculating 3D spatial joint interior angles using vector dot products in Euclidean 3-space (R^3), comparing observed angles against calibrated medical tolerance envelopes.')

add_bullet('3. Zero-Latency Acoustic Biofeedback Engine', 'Engineer a non-blocking voice synthesis pipeline leveraging React Native TTS with intelligent cooldown throttling (4-second debouncing) to deliver instantaneous verbal cues without inducing sensory overload.')

add_heading_2('1.4.2 Secondary Objectives')
add_bullet('1. Comprehensive Commercial 75-Pose Taxonomy', 'Architect and calibrate a complete commercial taxonomy comprising 75 asanas categorized across 3 developmental tiers: Foundation Core, Therapy & Recovery, and Power & Peak Inversions.')

add_bullet('2. Finite State Machine for Multi-Pose Guided Routines', 'Implement an autonomous session manager (RoutineEngine) that orchestrates pre-workout framing calibration, preparation countdowns, active hold timers, automated pose progressions, and celebratory audio transitions.')

add_bullet('3. Offline Persistence & Biomechanical Analytics', 'Establish an asynchronous offline storage layer (StorageService) to record session duration, pose completion tallies, joint accuracy grades, and workout consistency streaks.')

add_heading_1('1.5 Scope and Limitations of the Project')
add_heading_2('1.5.1 In-Scope Capabilities')
add_bullet('High-Throughput Edge Inference', 'Execution of full 33-point BlazePose neural networks directly on consumer smartphones utilizing hardware-accelerated WebGL shader buffers.')
add_bullet('Full 75-Pose Biomechanical Constraint Matrix', 'Pre-configured JSON constraint schema defining angular thresholds, directional variance tolerances, and multi-lingual naming conventions for 75 distinct asanas.')
add_bullet('Curated Flow Routines', 'Six specialized therapeutic and athletic multi-pose workout sequences (e.g., Morning Energizing Vinyasa, Desk Worker Spine Rehab, Peak Power & Inversions).')
add_bullet('Adaptive Noise Filtering', 'Exponential Moving Average (EMA) mathematical smoothing to mitigate low-light camera jitter and rolling standard deviation variance algorithms for tremor detection.')
add_bullet('Modern Glassmorphic Mobile UX', 'Production-ready four-tab mobile client featuring aesthetic dark-mode dashboards, interactive pose search, human figure anatomy cards, and live HUD camera studio.')

add_heading_2('1.5.2 Operational Limitations and Out-of-Scope Elements')
add_bullet('Single-Subject Restriction', 'The computer vision pipeline is optimized for individual practice; the presence of multiple overlapping bodies in the camera frame may degrade keypoint assignment accuracy.')
add_bullet('Extreme Low-Light and High-Contrast Occlusions', 'Performance relies on optical camera sensors; environments with severe under-exposure (< 20 lux) or intense backlighting may degrade confidence scores below the 0.40 detection threshold.')
add_bullet('External Biometric Sensor Fusion', 'Heart rate tracking, electromyography (EMG) muscle voltage sensing, and wearable IMU integration are outside the current project scope and reserved for future research iterations.')

add_heading_1('1.6 Target Audience & Demographic Applicability')
add_body('The AI-Based Yoga Trainer is specifically designed to accommodate a diverse spectrum of demographic segments with varying physical capabilities:')
add_bullet('Independent Home Yogis & Beginners', 'Individuals requiring continuous form validation to cultivate safe alignment habits without incurring the financial cost of private personal trainers.')
add_bullet('Sedentary Office Workers & Students', 'Demographics suffering from forward head posture, lumbar compression, and tight hip flexors who benefit from targeted therapeutic sequences.')
add_bullet('Prenatal & Geriatric Practitioners', 'Vulnerable demographics requiring low-impact, modified restorative flows with gentle, real-time safety threshold monitoring.')
add_bullet('Advanced Athletes & Calisthenics Enthusiasts', 'Practitioners mastering complex balance poses and inversions (such as Bakasana Crow Pose or Sirsasana Headstand) who require isometric hold timers and precision angle verification.')

add_heading_1('1.7 Organization of the Project Report')
add_body('This academic project report is organized systematically into nine comprehensive chapters, reflecting the end-to-end lifecycle of requirement analysis, mathematical design, implementation, and empirical validation:')

add_bullet('Chapter 1: Introduction', 'Establishes the research background, problem statement, core motivations, project objectives, operational scope, target demographics, and report organization.')
add_bullet('Chapter 2: Literature Survey', 'Examines existing academic literature, comparative analysis of 2D vs. 3D pose estimators, traditional commercial fitness applications, and theoretical principles of computer vision in biomechanics.')
add_bullet('Chapter 3: Requirement Analysis & System Specification', 'Details software and hardware specifications, functional and non-functional requirements, use-case modeling, and feasibility studies.')
add_bullet('Chapter 4: System Architecture & Design', 'Presents the high-level system architecture, client-side data flows, component interaction diagrams, finite state machine designs, and database/storage schema.')
add_bullet('Chapter 5: Mathematical Modeling & Biomechanical Algorithms', 'Explains the 3D spatial vector mathematics, joint interior angle formulas, EMA jitter attenuation, micro-tremor variance calculations, and rule-based evaluation logic.')
add_bullet('Chapter 6: Implementation Details', 'Discusses the concrete codebase implementation, React Native Expo ecosystem, TensorFlow.js WebGL tensor bridging, FeedbackEngine voice queuing, and HUD UI components.')
add_bullet('Chapter 7: Testing & Quality Assurance', 'Presents the verification strategy, unit testing of vector algorithms, JSON schema automated validations, stress testing, and physical device test matrices.')
add_bullet('Chapter 8: Results & Performance Analysis', 'Evaluates FPS throughput, memory consumption, thermal impact, pose evaluation accuracy benchmarks, and user experience telemetry.')
add_bullet('Chapter 9: Conclusion & Future Scope', 'Summarizes key project deliverables, academic contributions, commercial viability, and outlines future enhancements including multi-person tracking and AR avatar integration.')

output_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\Chapter_1_Introduction.docx'
doc.save(output_path)
print('Successfully generated Chapter_1_Introduction.docx at', output_path)
