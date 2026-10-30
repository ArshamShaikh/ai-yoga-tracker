import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Project_Report.docx'
doc = docx.Document(doc_path)

# Ensure no blue colors anywhere in the document
for p in doc.paragraphs:
    for run in p.runs:
        if run.font.color and run.font.color.rgb:
            # Change blue colors to pure black
            if run.font.color.rgb == RGBColor(0x00, 0x20, 0x60):
                run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

for t in doc.tables:
    for row in t.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for run in p.runs:
                    if run.font.color and run.font.color.rgb:
                        if run.font.color.rgb == RGBColor(0x00, 0x20, 0x60):
                            run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

def add_title_header(text, size=20):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(22)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x00) # Pure Black
    return p

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(16) # 16pt Bold
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x00) # Pure Black
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13.5) # 13.5pt Bold Italic
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x00) # Pure Black
    return p

def add_body(text):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    return p

def add_bullet(bold_prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_bold = p.add_run(bold_prefix + ': ')
    r_bold.font.name = 'Times New Roman'
    r_bold.font.bold = True
    r_bold.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    r_text = p.add_run(text)
    r_text.font.name = 'Times New Roman'
    r_text.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    return p

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

# Add page break before Chapter 3
doc.add_page_break()

# ==========================================
# CHAPTER 3: REQUIREMENT ANALYSIS & SPECIFICATION
# ==========================================
add_title_header('CHAPTER 3\nREQUIREMENT ANALYSIS & SPECIFICATION', size=20)

add_heading_1('3.1 Introduction to Requirement Engineering')
add_body(
    'Requirement engineering is a disciplined process in software engineering that systematically determines, '
    'documents, and maintains the functional and quality requirements of an intended system. '
    'In the design of the AI-Based Yoga Trainer, requirement engineering serves as the foundational bridge connecting '
    'biomechanical athletic needs, computer vision hardware constraints, and mobile real-time human-computer interaction (HCI). '
    'This chapter provides a comprehensive specification of system feasibility, developer and deployment hardware profiles, '
    'software runtime ecosystems, detailed functional specifications, rigorous non-functional quality attributes, '
    'and formal use-case modeling accompanied by unified structural diagrams.'
)

add_heading_1('3.2 Feasibility Study')
add_body(
    'Prior to system implementation, an extensive multi-dimensional feasibility study was conducted to ascertain whether '
    'the proposed on-device 3D posture estimation and real-time coaching system could be successfully engineered and sustained '
    'within practical technical, operational, economic, and scheduling boundaries.'
)

add_heading_2('3.2.1 Technical Feasibility')
add_body(
    'Technical feasibility assesses the availability, maturity, and suitability of the underlying hardware and software technologies. '
    'The AI Yoga Trainer requires executing deep neural network inference on streaming video buffers while simultaneously computing '
    'three-dimensional vector dot products and rendering responsive user interfaces at 30+ frames per second (FPS). '
    'The technical feasibility is confirmed through three core architectural enablers:'
)
add_bullet('Hardware-Accelerated WebGL Tensor Buffers', 'Through TensorFlow.js and @tensorflow/tfjs-react-native, the camera video feed is streamed directly into GPU-bound WebGL shader pipelines, bypassing slow serial JavaScript bridge serialization.')
add_bullet('Quantized MediaPipe BlazePose Architecture', 'BlazePose achieves sub-35ms inference on modern mobile processors (Snapdragon 700/800 series and Apple A12 Bionic and newer) by employing lightweight depthwise convolutions and two-stage detector-tracker topologies.')
add_bullet('O(1) Vector Mathematics', 'Rather than running continuous neural classifications, post-inference biomechanical validation is reduced to deterministic spatial vector algebra executed in sub-millisecond time on mobile CPUs.')

add_heading_2('3.2.2 Operational Feasibility')
add_body(
    'Operational feasibility evaluates how effectively the system integrates into the daily routines of target practitioners. '
    'Key factors ensuring high operational adoption include:'
)
add_bullet('Zero-Equipment Requirement', 'Users require exclusively their personal smartphone; no external depth sensors (e.g., Microsoft Kinect), wearable IMU straps, or expensive smart mirrors are needed.')
add_bullet('Hands-Free Auditory Coaching', 'Because yoga practitioners cannot continuously stare at a phone screen while performing balance poses or inversions, synthesized acoustic biofeedback delivers immediate adjustments without interrupting physical flow.')
add_bullet('Absolute Privacy Compliance', 'All visual and kinematic telemetry is computed locally in volatile memory with zero cloud transmission, fully satisfying stringent privacy regulations and eliminating user hesitation regarding exercising in private environments.')

add_heading_2('3.2.3 Economic Feasibility')
add_body(
    'Economic feasibility evaluates financial expenditures against projected benefits. '
    'Traditional AI architectures incur substantial recurring cloud infrastructure expenses for GPU video streaming (e.g., AWS EC2 G4dn instances costing upwards of $0.526 per hour per user). '
    'By adopting an edge-exclusive computational architecture, the marginal operational hosting cost per active user is exactly zero ($0.00). '
    'Furthermore, the entire development stack—React Native, Expo SDK, TensorFlow.js, and MediaPipe—is completely open-source under Apache 2.0 and MIT licenses, '
    'eliminating proprietary licensing overhead.'
)

add_heading_2('3.2.4 Schedule and Resource Feasibility')
add_body(
    'The project was systematically scheduled across academic semester phases, encompassing initial prototype calibration, '
    'BlazePose 3D migration, expansion to a commercial 75-pose taxonomy, and full cross-platform QA testing. '
    'All deliverables were achieved within the designated academic timeline without requiring specialized external hardware.'
)

add_heading_1('3.3 Software and Hardware Specifications')
add_body('The operational requirements are divided into developer development specifications and target deployment requirements:')

# Table 3.1: Hardware Requirements
t_hw = doc.add_table(rows=1, cols=3)
t_hw.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_hw)
hw_hdrs = ['Component', 'Developer Workstation', 'Target Mobile Client (Minimum / Recommended)']
for i, h in enumerate(hw_hdrs):
    c = t_hw.rows[0].cells[i]
    c.text = h
    set_cell_shading(c, 'F0F0F0')
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

hw_data = [
    ['Processor (CPU)', 'Intel Core i5 / AMD Ryzen 5 (6 Cores, 2.5+ GHz)', 'Octa-core 2.0 GHz (Snapdragon 680 min; SD 870 / A13 rec)'],
    ['Graphics (GPU)', 'Dedicated NVIDIA GTX 1050 / Integrated Iris Xe', 'Adreno 610+ / Apple GPU (OpenGL ES 3.0 / Metal support)'],
    ['Random Access Memory', '16 GB DDR4 RAM', '4 GB LPDDR4 (Min) / 6 GB+ (Recommended)'],
    ['Optical Camera Sensor', '1080p Full HD USB Webcam', '720p @ 30 FPS Wide-Angle Lens (1080p @ 60 FPS rec)'],
    ['Storage Space', '10 GB Free SSD Storage', '150 MB Free Internal Flash Storage'],
    ['Operating System', 'Windows 10/11 64-bit / macOS Ventura', 'Android 10.0 (API 29)+ / iOS 14.0+']
]

for row_data in hw_data:
    row_cells = t_hw.add_row().cells
    for i, val in enumerate(row_data):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

add_body('Table 3.1 delineates the physical hardware specifications governing the development and runtime execution environments.')

# Table 3.2: Software Requirements
t_sw = doc.add_table(rows=1, cols=3)
t_sw.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_sw)
sw_hdrs = ['Software Layer', 'Technology / Framework', 'Version / License']
for i, h in enumerate(sw_hdrs):
    c = t_sw.rows[0].cells[i]
    c.text = h
    set_cell_shading(c, 'F0F0F0')
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

sw_data = [
    ['Mobile Framework', 'React Native (Managed via Expo SDK)', 'Expo SDK 51 / React Native 0.74 (MIT)'],
    ['JavaScript / Language', 'Node.js LTS Runtime & ECMAScript 2022', 'Node.js v20.x / ES6+ (OpenJS)'],
    ['Deep Learning Inference', 'TensorFlow.js & @tensorflow/tfjs-react-native', 'v4.17.0+ (Apache 2.0)'],
    ['Computer Vision Model', 'MediaPipe BlazePose 3D (33 Landmarks)', '@tensorflow-models/pose-detection v2.1.3'],
    ['Camera Hardware Hook', 'Expo Camera (cameraWithTensors WebGL Bridge)', 'expo-camera v15.0+ (MIT)'],
    ['Text-To-Speech (TTS)', 'React Native TTS / Expo Speech', 'react-native-tts v4.1.0 (MIT)'],
    ['Local Data Storage', 'AsyncStorage (Offline Key-Value / JSON Store)', '@react-native-async-storage/async-storage'],
    ['Styling & Navigation', 'Expo Router (File-based navigation)', 'expo-router v3.5+ (MIT)']
]

for row_data in sw_data:
    row_cells = t_sw.add_row().cells
    for i, val in enumerate(row_data):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

add_body('Table 3.2 lists the complete software infrastructure utilized to engineer and execute the application.')

add_heading_1('3.4 Functional Requirements')
add_body('Functional requirements define the core operational behaviors, input transformations, and outputs of the system:')

add_bullet('FR-1: 3D Real-Time Skeletal Landmark Detection', 'The system shall process live video frames captured at a minimum of 25 FPS and extract 33 anatomical keypoints with three-dimensional spatial coordinates (X, Y, and depth coordinate Z) and confidence scores.')
add_bullet('FR-2: Biomechanical Interior Angle Evaluation', 'The system shall compute interior 3D angles between adjacent limb vectors and evaluate them against pre-configured joint tolerance limits defined in the commercial 75-pose constraint schema.')
add_bullet('FR-3: Dynamic Anti-Jitter Smoothing & Tremor Detection', 'The system shall apply Exponential Moving Average (EMA) filtering (alpha = 0.40) to mitigate sensor jitter and continuously compute rolling coordinate variance across 30 frames to detect physical muscle fatigue.')
add_bullet('FR-4: Hands-Free Voice Biofeedback & Audio Throttling', 'When an angular constraint is violated, the system shall synthesize human-sounding corrective speech cues (e.g., "Straighten your back leg") throttled by a 4-second debouncing cooldown to prevent audio collisions.')
add_bullet('FR-5: 75-Pose Taxonomy & Curated Routine Progression', 'The system shall provide an indexed library of 75 calibrated yoga asanas and support multi-pose curated flows that automatically sequence postures upon successful hold completion.')
add_bullet('FR-6: Pre-Session Framing Calibration & Hold Timers', 'The system shall verify full-body visibility (head-to-ankle framing) prior to session initiation and execute an active isometric hold countdown timer (5s, 10s, 30s) when valid posture alignment is sustained.')
add_bullet('FR-7: Offline Session Persistence & Biomechanical Analytics', 'The system shall record session telemetry (total duration, completed poses, average joint precision grade, and practice streaks) completely offline using asynchronous local storage.')

add_heading_1('3.5 Non-Functional Requirements (NFRs)')
add_body('Non-functional requirements specify quality benchmarks and architectural constraints:')

add_bullet('NFR-1: Real-Time Performance & Low Latency', 'The end-to-end processing pipeline—from camera frame acquisition to skeletal overlay rendering and angle computation—shall execute within 33.3 milliseconds (sustaining 30 FPS) with inference latency not exceeding 40ms on target hardware.')
add_bullet('NFR-2: Inviolable Data Privacy (Edge AI Mandate)', 'Zero bytes of optical imagery, video recordings, or facial keypoints shall be transmitted outside the physical device. All memory buffers shall be flushed upon session termination.')
add_bullet('NFR-3: Mathematical Robustness & Error Resilience', 'Vector dot-product calculations shall enforce defensive mathematical clamping within [-1.0, 1.0] to prevent NaN propagation in inverse trigonometric functions during parallel or degenerate vector orientations.')
add_bullet('NFR-4: Usability & Ergonomic Accessibility', 'The user interface shall implement high-contrast glassmorphic dark-mode HUD styling with large visual alignment rings visible to practitioners standing 2 to 3 meters away from the smartphone.')
add_bullet('NFR-5: Cross-Platform Portability', 'The codebase shall compile and operate identically across Android and iOS mobile platforms without modifying core computer vision or mathematical business logic.')

add_heading_1('3.6 Use Case Modeling & System Actors')
add_body(
    'Use case modeling identifies the interaction boundaries between external actors and internal system operations. '
    'The system defines three primary actors: (1) The Yoga Practitioner (Primary User); (2) The Edge AI & Audio Coaching Engine (Internal System Actor); '
    'and (3) The Offline Storage Service (Secondary Supporting Actor).'
)

# Insert Use Case Diagram Figure
p_img = doc.add_paragraph()
p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img.paragraph_format.space_before = Pt(12)
p_img.paragraph_format.space_after = Pt(6)
img_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\use_case_diagram.png'
doc.add_picture(img_path, width=Inches(6.0))

p_cap = doc.add_paragraph()
p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap.paragraph_format.space_after = Pt(12)
r_cap = p_cap.add_run('Figure 3.1: Use Case Diagram for AI-Based Yoga Trainer System')
r_cap.font.name = 'Times New Roman'
r_cap.font.size = Pt(11)
r_cap.font.bold = True

add_body(
    'As illustrated in Figure 3.1, the Yoga Practitioner initiates practice by selecting an individual pose or curated sequence, '
    'undergoes pre-session framing calibration, and receives real-time 3D tracking and vocal biofeedback. '
    'The Edge AI Vision Engine continuously processes camera tensor frames, computes vector angles, and triggers the audio coach, '
    'while the Offline Storage Service records session completion metrics.'
)

# Table 3.3: Use Case Specifications
t_uc = doc.add_table(rows=1, cols=4)
t_uc.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_uc)
uc_hdrs = ['Use Case ID', 'Use Case Name', 'Primary Actor', 'Operational Description']
for i, h in enumerate(uc_hdrs):
    c = t_uc.rows[0].cells[i]
    c.text = h
    set_cell_shading(c, 'F0F0F0')
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

uc_data = [
    ['UC-01', 'Select Pose / Flow', 'Practitioner', 'Browse 75 poses or 6 curated flows; filter by difficulty and launch studio.'],
    ['UC-02', 'Calibrate Body Framing', 'Practitioner / Engine', 'Verify head-to-toe distance; receive verbal guidance ("Step back").'],
    ['UC-03', 'Execute 3D Tracking', 'Edge AI Vision Engine', 'Extract 33 3D spatial landmarks at 30+ FPS via BlazePose WebGL tensors.'],
    ['UC-04', 'Evaluate Joint Angles', 'Biomechanical Rules Engine', 'Compute 3D vector dot products and verify against medical tolerance ranges.'],
    ['UC-05', 'Deliver Audio Biofeedback', 'Dynamic Audio Coach', 'Synthesize real-time corrective voice prompts with 4-second debouncing.'],
    ['UC-06', 'Manage Hold Timers', 'Routine State Machine', 'Track isometric posture duration; auto-transition to next flow pose.'],
    ['UC-07', 'Persist Session Analytics', 'Offline Storage Service', 'Record completed poses, total minutes, accuracy grade, and streak counts.']
]

for row_data in uc_data:
    row_cells = t_uc.add_row().cells
    for i, val in enumerate(row_data):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

add_body('Table 3.3 summarizes the formal specifications and primary actors associated with each core system use case.')

# Save updated master report
doc.save(doc_path)
print('Successfully appended Chapter 3 and embedded Figure 3.1 into', doc_path)
