import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Project_Report.docx'
doc = docx.Document(doc_path)

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

# Add page break before Chapter 4
doc.add_page_break()

# ==========================================
# CHAPTER 4: SYSTEM ARCHITECTURE & DESIGN
# ==========================================
add_title_header('CHAPTER 4\nSYSTEM ARCHITECTURE & DESIGN', size=20)

add_heading_1('4.1 Introduction to System Architecture')
add_body(
    'Software architecture serves as the blueprint for both the system and the project, '
    'defining the fundamental structure, behavioral relationships, and design constraints across components. '
    'The AI-Based Yoga Trainer operates under strict real-time performance constraints: video frames must be acquired, '
    'transferred into neural network tensors, evaluated against spatial geometric algorithms, and mapped to audio-visual biofeedback '
    'within a 33-millisecond deadline to sustain 30 frames per second on mobile hardware. '
    'To achieve this without compromising battery efficiency, memory stability, or data confidentiality, '
    'the application adopts a decoupled, event-driven, edge-exclusive three-tier architecture.'
)

add_heading_1('4.2 High-Level System Architecture')
add_body(
    'The system architecture is structured into three distinct conceptual layers, each isolated by well-defined programmatic interfaces:'
)
add_bullet('Layer 1: Presentation & Client Interaction Layer', 'Built using React Native and Expo Router, this layer encompasses the four primary app tabs (Home Dashboard, Routines & Flows, 75-Pose Library, and Activity Analytics) alongside the live Yoga Studio HUD. It is responsible for rendering high-performance 2D/3D canvas overlays, circular hold timers, and interactive anatomy modal cards.')
add_bullet('Layer 2: Computer Vision & Biomechanical Math Core', 'Operating directly over device hardware, this layer handles frame extraction via Expo Camera, passes zero-copy GPU tensors using WebGL shaders into TensorFlow.js, executes MediaPipe BlazePose 3D (33 landmarks), and executes spatial vector dot-product calculations alongside Exponential Moving Average (EMA) smoothing.')
add_bullet('Layer 3: State Management, Audio Coaching & Storage Layer', 'Comprises the finite state machine (RoutineEngine), the prioritized audio synthesizer (FeedbackEngine), the commercial 75-pose JSON rules constraint matrix, and the offline asynchronous persistence service (StorageService).')

# Insert Architecture Diagram (Figure 4.1)
p_img1 = doc.add_paragraph()
p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img1.paragraph_format.space_before = Pt(12)
p_img1.paragraph_format.space_after = Pt(6)
img1_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\architecture_diagram.png'
doc.add_picture(img1_path, width=Inches(6.0))

p_cap1 = doc.add_paragraph()
p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap1.paragraph_format.space_after = Pt(12)
r_cap1 = p_cap1.add_run('Figure 4.1: High-Level System Architecture of AI-Based Yoga Trainer')
r_cap1.font.name = 'Times New Roman'
r_cap1.font.size = Pt(11)
r_cap1.font.bold = True

add_body(
    'Figure 4.1 illustrates the structural isolation between the client presentation views, '
    'the edge computer vision inference pipeline, and the background state orchestration services.'
)

add_heading_1('4.3 Data Flow Architecture & Pipeline Modeling')
add_body(
    'The real-time data flow operates as a continuous, unidirectional circular pipeline executing once every camera frame:'
)
add_bullet('1. Optical Frame Acquisition', 'The device camera captures an uncompressed video frame and streams it into the native C++ frame buffer.')
add_bullet('2. WebGL Texture Binding', 'The TensorCamera component downsamples the frame to 256x256 RGB pixels and binds it to a WebGL texture buffer, bypassing serial JavaScript bridge memory copies.')
add_bullet('3. BlazePose 3D Landmark Inference', 'The neural network processes the tensor, returning 33 anatomical keypoints with normalized X, Y coordinates, metric depth Z relative to the hips, and visibility confidence scores.')
add_bullet('4. Anti-Jitter Temporal Smoothing', 'Keypoint coordinates are blended with the prior frame using an Exponential Moving Average filter (alpha = 0.40) to eliminate high-frequency sensor noise.')
add_bullet('5. Vector Kinematics & Constraint Validation', 'The math engine calculates spatial joint interior angles and verifies them against the target ranges in poseConstraints.json.')
add_bullet('6. Biofeedback & UI State Dispatch', 'If alignment is valid, the hold timer increments and skeletal lines illuminate green; if misaligned, corrective voice cues are queued and red guidance vectors highlight the faulty joint.')

add_heading_1('4.4 Finite State Machine (FSM) Design for Routine Management')
add_body(
    'To transition the application from a simple single-pose camera test into a commercial-grade guided fitness studio, '
    'an autonomous Finite State Machine was designed within RoutineEngine.js. '
    'The state machine governs the end-to-end lifecycle of multi-pose workout sequences without requiring physical screen interaction during practice.'
)

# Insert FSM Diagram (Figure 4.2)
p_img2 = doc.add_paragraph()
p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img2.paragraph_format.space_before = Pt(12)
p_img2.paragraph_format.space_after = Pt(6)
img2_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\fsm_state_diagram.png'
doc.add_picture(img2_path, width=Inches(6.2))

p_cap2 = doc.add_paragraph()
p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap2.paragraph_format.space_after = Pt(12)
r_cap2 = p_cap2.add_run('Figure 4.2: Finite State Machine (FSM) Transition Diagram in RoutineEngine')
r_cap2.font.name = 'Times New Roman'
r_cap2.font.size = Pt(11)
r_cap2.font.bold = True

add_body(
    'As depicted in Figure 4.2, the state machine transitions deterministically across seven discrete operational phases:'
)
add_bullet('State 1: IDLE', 'The practitioner browses the catalog and selects a single asana or curated multi-pose flow.')
add_bullet('State 2: CALIBRATING', 'The optical sensor verifies that the practitioner is positioned at an appropriate distance (head to ankles fully framed). If uncalibrated, voice prompts advise the user to step back or adjust device tilt.')
add_bullet('State 3: PREPARING', 'Once framing is confirmed, a visual and acoustic 3-second preparation countdown initiates, allowing the user to enter the target starting stance.')
add_bullet('State 4: HOLDING_ACCURATE', 'When the observed joint angles satisfy the pose constraint matrix, the active hold timer increments. If posture breaks, the timer pauses and the audio coach provides corrective verbal cues.')
add_bullet('State 5: POSE_COMPLETE', 'Upon reaching the target hold duration (e.g., 10s or 30s), a celebratory chime triggers, recording mastery metrics.')
add_bullet('State 6: TRANSITION', 'If the routine contains subsequent postures (or requires bilateral left/right limb switching), the system announces the upcoming pose and loops back to PREPARING.')
add_bullet('State 7: SESSION_FINISHED', 'Upon completion of all poses in the sequence, workout analytics are flushed to local storage and the celebratory summary modal displays overall session performance.')

add_heading_1('4.5 Database & Data Persistence Design')
add_body(
    'In strict accordance with the edge-exclusive privacy mandate, all user statistics, practice history, '
    'and customization preferences are stored locally on the device using @react-native-async-storage/async-storage. '
    'The local data schema is organized into four primary entity domains:'
)

# Table 4.1: Database Schema Dictionary
t_db = doc.add_table(rows=1, cols=4)
t_db.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_db)
db_hdrs = ['Entity / Storage Key', 'Data Type', 'Primary Attributes', 'Description & Purpose']
for i, h in enumerate(db_hdrs):
    c = t_db.rows[0].cells[i]
    c.text = h
    set_cell_shading(c, 'F0F0F0')
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

db_data = [
    ['USER_PROFILE', 'JSON Object', 'userName, experienceLevel, audioCoachEnabled, speechRate, preferredDuration', 'Maintains user customization and audio coaching preferences.'],
    ['WORKOUT_HISTORY', 'JSON Array of Objects', 'sessionId, routineId, timestamp, durationSeconds, accuracyScore, posesCount', 'Historical log of completed sessions for weekly consistency charts.'],
    ['POSE_MASTERY_MAP', 'Dictionary {poseId: Object}', 'poseId, totalPracticed, bestHoldSeconds, avgAccuracy, isMastered', 'Tracks individualized proficiency and identifies problematic joints across 75 poses.'],
    ['STREAK_METRICS', 'JSON Object', 'currentStreakDays, longestStreakDays, lastPracticeDate', 'Calculates daily consecutive workout adherence to foster gamified habit retention.']
]

for row_data in db_data:
    row_cells = t_db.add_row().cells
    for i, val in enumerate(row_data):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [1] else WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

add_body('Table 4.1 defines the structure of the offline key-value storage entities powering the activity analytics engine.')

add_heading_1('4.6 User Interface (UI/UX) Component Hierarchy & Layout Design')
add_body(
    'The mobile application interface is structured using Expo Router file-based navigation, '
    'adopting a sleek, modern glassmorphic design aesthetic engineered for readability from a distance:'
)
add_bullet('Root Layout (app/(tabs)/_layout.js)', 'Configures the translucent floating bottom navigation bar providing seamless routing across Home (index), Flows (routines), Library (poses), and Progress (activity).')
add_bullet('Studio Session Screen (app/session.js)', 'Full-screen camera viewport embedded with PoseOverlay, displaying real-time 33-point skeletal bones, circular alignment countdown rings, and dynamic floating coaching chips.')
add_bullet('Visual Anatomy Guide (PoseGuideModal.js)', 'Presents high-resolution human pose illustrations, target muscle group callouts, Sanskrit naming, and clinical precautions before starting practice.')
add_bullet('Workout Summary Screen (app/summary.js)', 'Post-workout celebratory view presenting overall session accuracy percentage, streak increments, and pose-by-pose joint breakdown.')

# Save updated master report with lock fallback if Word is open
try:
    doc.save(doc_path)
    print("Successfully appended Chapter 4 with Figure 4.1 and Figure 4.2 into", doc_path)
except PermissionError:
    v2_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Project_Report_v2.docx'
    doc.save(v2_path)
    print("Original file is currently open in Microsoft Word. Successfully saved Chapter 4 with Figure 4.1 and Figure 4.2 into:", v2_path)
