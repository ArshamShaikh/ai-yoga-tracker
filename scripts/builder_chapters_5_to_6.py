import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from builder_core import (
    add_title_header, add_heading_1, add_heading_2, 
    add_body, add_bullet, add_figure, add_code_block,
    set_cell_shading, set_table_borders
)

def build_chapters_5_to_6(doc):
    # =========================================================
    # CHAPTER 5. SYSTEM DESIGN
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "CHAPTER 5. SYSTEM DESIGN", size=20)

    add_heading_1(doc, "5.1 Introduction")
    add_body(doc, "System design translates analytical requirements into architectural blueprints, data flow models, state transition machines, and mathematical formulations that define the operational structure of the AI-Based Yoga Trainer.")

    add_heading_1(doc, "5.2 System Architecture Diagram")
    add_body(doc, "The software architecture employs a decoupled, edge-exclusive three-tier framework: (1) Presentation Tier (Studio HUD, camera viewport, dynamic SVG skeleton canvas); (2) Computer Vision & Biomechanical Math Tier (WebGL tensor camera bridge, BlazePose 3D inference, vector dot-product engine, EMA signal filter); and (3) State Orchestration & Persistence Tier (RoutineEngine FSM, FeedbackEngine TTS, AsyncStorage).")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\architecture_diagram.png', 'Figure 5.1: High-Level System Architecture Diagram of 3-Tier Edge Mobile Framework')

    add_heading_1(doc, "5.3 Data Flow Diagram")
    add_heading_2(doc, "5.3.1 Level 0 DFD (Context Diagram)")
    add_body(doc, "Figure 5.2 models the fundamental boundary: the Yoga Practitioner provides an optical camera stream and pose selection inputs; the System processes all frames locally and emits real-time visual skeletal overlays and audio cues, while logging session history and streaks to local storage.")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\dfd_level_0.png', 'Figure 5.2: Data Flow Diagram Level 0 (Context Diagram)')

    add_heading_2(doc, "5.3.2 Level 1 DFD (Pipeline Decomposition)")
    add_body(doc, "Figure 5.3 decomposes internal data pipelines across six discrete processes: 1.0 Frame Acquisition -> 2.0 3D BlazePose Landmark Extraction -> 3.0 Vector Kinematics & EMA Filtering -> 4.0 Routine FSM & Hold Timer Tracking -> 5.0 Debounced Audio Coaching -> 6.0 AsyncStorage Persistence.")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\dfd_level_1.png', 'Figure 5.3: Data Flow Diagram Level 1 (Decomposed Processing Pipeline)')

    add_heading_1(doc, "5.4 Activity Diagram & Workflow Modeling")
    add_body(doc, "The UML Activity Diagram illustrates the execution flow: from pose selection, mounting the WebGL camera context, verifying full-body calibration framing, playing the 3-2-1 countdown, computing joint angles, evaluating tolerance bounds, to incrementing hold timers and updating daily streaks.")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\activity_diagram.png', 'Figure 5.4: UML Activity Diagram Modeling Autonomous Workout Session Flow')

    add_heading_1(doc, "5.5 E-R Diagram & Data Persistence Schema")
    add_body(doc, "Data persistence is managed locally through AsyncStorage. Table 5.1 details the relational entities, attributes, and data structures utilized for offline performance tracking.")
    
    # Table 5.1
    t_db = doc.add_table(rows=1, cols=4)
    t_db.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_db)
    for i, h in enumerate(['Entity / Storage Key', 'Data Type', 'Primary Attributes', 'Description']):
        c = t_db.rows[0].cells[i]
        c.text = h
        set_cell_shading(c, 'F0F0F0')
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(10)

    db_rows = [
        ['USER_PROFILE', 'JSON Object', 'userName, experienceLevel, audioCoachEnabled', 'User settings and coaching preferences.'],
        ['WORKOUT_HISTORY', 'JSON Array', 'sessionId, timestamp, duration, accuracyScore', 'Historical log for weekly consistency charts.'],
        ['POSE_MASTERY_MAP', 'Dictionary', 'poseId, totalPracticed, bestHold, isMastered', 'Individual proficiency across 75 poses.'],
        ['STREAK_METRICS', 'JSON Object', 'currentStreakDays, longestStreakDays, lastDate', 'Consecutive daily workout adherence counter.']
    ]
    for r in db_rows:
        row_cells = t_db.add_row().cells
        for i, v in enumerate(r):
            row_cells[i].text = v
            p = row_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [1] else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size = Pt(9.5)

    add_heading_1(doc, "5.6 Use-Case Diagram & Actor Interaction")
    add_body(doc, "Figure 5.5 presents the comprehensive use-case interactions between the Yoga Practitioner, the Core CV Engine, and the Local Storage subsystem.")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\use_case_diagram.png', 'Figure 5.5: Comprehensive Use Case Diagram for AI-Based Yoga Trainer')

    add_heading_1(doc, "5.7 Finite State Machine Design (FSM)")
    add_body(doc, "Workout routines are choreographed by an autonomous 7-state Finite State Machine: IDLE -> CALIBRATING -> PREPARING -> HOLDING_ACCURATE -> POSE_COMPLETE -> TRANSITION -> SESSION_FINISHED.")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\fsm_state_diagram.png', 'Figure 5.6: Finite State Machine (FSM) State Transition Diagram')

    add_heading_2(doc, "5.7.1 Biomechanical Articular Joint Formulations")
    add_body(doc, "For joint vertex B with adjacent limbs A and C: u = A - B and v = C - B. Cosine is calculated via 3D vector dot product: cos(theta) = (u . v) / (||u|| * ||v||), bounded by defensive clamping [-1.0, 1.0] to prevent NaN singularities.")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\vector_angle_geometry.png', 'Figure 5.7: 3D Euclidean Vector Kinematics Geometry Model')
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\ema_signal_smoothing.png', 'Figure 5.8: Temporal Signal Processing: Raw Sensor Jitter vs. Calibrated EMA Smoothing')

    # =========================================================
    # CHAPTER 6. SYSTEM IMPLEMENTATION
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "CHAPTER 6. SYSTEM IMPLEMENTATION", size=20)

    add_heading_1(doc, "6.1 Introduction")
    add_body(doc, "System implementation translates theoretical designs into high-performance source code, combining React Native UI components, WebGL tensor shaders, 3D vector geometry, and robust automated quality assurance.")

    add_heading_1(doc, "6.2 System Execution Flowchart")
    add_body(doc, "Figure 6.1 illustrates the modular interactions: Camera frames flow to YogaCamera, landmarks stream to PoseDetector, angles evaluate against poseConstraints.json, RoutineEngine advances timers, and FeedbackEngine triggers spoken audio.")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\module_interaction_diagram.png', 'Figure 6.1: Module Interaction & Component Dependency Architecture')

    add_heading_1(doc, "6.3 Coding & Core Module Implementation")
    add_heading_2(doc, "6.3.1 Frontend Studio & Dynamic Skeletal Canvas")
    add_body(doc, "PoseOverlay.js renders 33 SVG keypoints and connecting bones. Joints compliant with target angle ranges illuminate in peaceful emerald green (#2ECC71); misaligned joints illuminate in warning crimson (#E74C3C).")
    add_code_block(doc,
        '// src/components/PoseOverlay.js: SVG Landmark Rendering with Adaptive Autoscaling\n'
        'export const PoseOverlay = ({ keypoints, targetPose, currentAngles }) => {\n'
        '    return (\n'
        '        <Svg style={StyleSheet.absoluteFill}>\n'
        '            {CONNECTIONS.map(([i, j], idx) => (\n'
        '                <Line key={idx} x1={keypoints[i].x} y1={keypoints[i].y}\n'
        '                      x2={keypoints[j].x} y2={keypoints[j].y}\n'
        '                      stroke="#2ECC71" strokeWidth={3} />\n'
        '            ))}\n'
        '            {keypoints.map((pt, idx) => (\n'
        '                <Circle key={idx} cx={pt.x} cy={pt.y} r={5} fill="#FFFFFF" />\n'
        '            ))}\n'
        '        </Svg>\n'
        '    );\n'
        '};'
    )

    add_heading_2(doc, "6.3.2 Computer Vision & WebGL Tensor Pipeline")
    add_body(doc, "YogaCamera.js binds live camera buffers directly to WebGL textures at 256x256 RGB resolution, eliminating serial data transfer overhead across the asynchronous JavaScript bridge.")

    add_heading_2(doc, "6.3.3 3D Vector Angle Mathematics & Clamping")
    add_body(doc, "poseMathUtils.js implements vector angle calculations with epsilon norm checks and defensive cosine clamping:")
    add_code_block(doc,
        '// src/utils/poseMathUtils.js: 3D Vector Interior Angle Formulation\n'
        'export function calculateAngle3D(A, B, C) {\n'
        '    if (!A || !B || !C) return null;\n'
        '    const u = [A.x - B.x, A.y - B.y, (A.z || 0) - (B.z || 0)];\n'
        '    const v = [C.x - B.x, C.y - B.y, (C.z || 0) - (B.z || 0)];\n'
        '    const magU = Math.sqrt(u[0]*u[0] + u[1]*u[1] + u[2]*u[2]);\n'
        '    const magV = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);\n'
        '    if (magU < 1e-6 || magV < 1e-6) return null;\n'
        '    const dot = u[0]*v[0] + u[1]*v[1] + u[2]*v[2];\n'
        '    const clampedCos = Math.max(-1.0, Math.min(1.0, dot / (magU * magV)));\n'
        '    return (Math.acos(clampedCos) * 180) / Math.PI;\n'
        '}'
    )

    add_heading_2(doc, "6.3.4 EMA Temporal Anti-Jitter Filtering")
    add_code_block(doc,
        '// First-Order Exponential Moving Average (alpha = 0.40)\n'
        'export function smoothLandmarksEMA(current, previous, alpha = 0.40) {\n'
        '    if (!previous) return current;\n'
        '    return current.map((pt, i) => ({\n'
        '        x: alpha * pt.x + (1 - alpha) * previous[i].x,\n'
        '        y: alpha * pt.y + (1 - alpha) * previous[i].y,\n'
        '        z: alpha * (pt.z || 0) + (1 - alpha) * (previous[i].z || 0),\n'
        '        score: pt.score\n'
        '    }));\n'
        '}'
    )

    add_heading_2(doc, "6.3.5 RoutineEngine Autonomous State Machine")
    add_body(doc, "RoutineEngine orchestrates calibration checks, hold countdowns, form verification, and automatic transitions across sequences without touching the screen.")

    add_heading_2(doc, "6.3.6 FeedbackEngine & Speech Queue Throttling")
    add_code_block(doc,
        '// src/services/FeedbackEngine.js: 4-Second Debouncing & Safe Resource Disposal\n'
        'class FeedbackEngine {\n'
        '    speak(message) {\n'
        '        const now = Date.now();\n'
        '        if (now - this.lastSpokenTime > 4000) {\n'
        '            try { Tts.speak(message); } catch (err) {}\n'
        '            this.lastSpokenTime = now;\n'
        '        }\n'
        '    }\n'
        '    stop() { try { Tts.stop(); } catch (e) {} }\n'
        '}'
    )

    add_heading_1(doc, "6.4 Testing Approaches & Quality Assurance")
    add_body(doc, "Quality assurance followed a formal V-Model lifecycle combining unit tests, cross-platform UI tests, zero-cloud privacy tests, and stress tests.")
    add_figure(doc, r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\testing_v_model.png', 'Figure 6.2: Software Quality Assurance V-Model Lifecycle')

    add_heading_2(doc, "6.4.1 Unit Testing of Mathematical Core")
    # Table 6.1
    t_ut = doc.add_table(rows=1, cols=5)
    t_ut.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_ut)
    for i, h in enumerate(['Test ID', 'Test Scenario', 'Expected Angle', 'Calculated Angle', 'Status']):
        c = t_ut.rows[0].cells[i]
        c.text = h
        set_cell_shading(c, 'F0F0F0')
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(10)

    ut_rows = [
        ['UT-01', 'Orthogonal 2D vectors: A(0,1,0), B(0,0,0), C(1,0,0)', '90.00 deg', '90.00 deg', 'PASSED'],
        ['UT-02', 'Straight collinear extension: A(0,1,0), B(0,0,0), C(0,-1,0)', '180.00 deg', '180.00 deg', 'PASSED'],
        ['UT-03', 'Acute angle test: A(1,1,0), B(0,0,0), C(1,0,0)', '45.00 deg', '45.00 deg', 'PASSED'],
        ['UT-04', '3D spatial depth tilt: A(0,1,1), B(0,0,0), C(0,1,-1)', '90.00 deg', '90.00 deg', 'PASSED'],
        ['UT-05', 'Floating-point rounding overflow (dot/mag = 1.000000002)', '0.00 deg (No NaN)', '0.00 deg', 'PASSED (Clamped)'],
        ['UT-06', 'Degenerate zero-magnitude vector: A(0,0,0), B(0,0,0), C(1,0,0)', 'null (No Crash)', 'null', 'PASSED (Handled)']
    ]
    for r in ut_rows:
        row_cells = t_ut.add_row().cells
        for i, v in enumerate(r):
            row_cells[i].text = v
            p = row_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 2, 3, 4] else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size = Pt(9.5)

    add_heading_2(doc, "6.4.2 Usability & Cross-Platform UI Testing")
    add_body(doc, "Verified safe area inset padding and responsive glassmorphism across Android and iOS viewports.")

    add_heading_2(doc, "6.4.3 Security & Zero-Cloud Privacy Testing")
    add_body(doc, "Wireshark packet sniffing confirmed 0 bytes of camera or tensor data transmitted over external networks.")

    add_heading_2(doc, "6.4.4 Test Cases & Execution Matrix")
    # Table 6.2
    t_tc = doc.add_table(rows=1, cols=5)
    t_tc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_tc)
    for i, h in enumerate(['Test ID', 'Test Description', 'Input Condition', 'Expected System Behavior', 'Result']):
        c = t_tc.rows[0].cells[i]
        c.text = h
        set_cell_shading(c, 'F0F0F0')
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(10)

    tc_rows = [
        ['TC-01', 'Pose Selection', 'User clicks Warrior II in Pose Library', 'Loads Studio HUD with warrior_ii constraints', 'PASSED'],
        ['TC-02', 'Calibration Detection', 'User steps back to 2.5m; full body visible', 'Announces "Calibrated! Get ready in 3.. 2.. 1.."', 'PASSED'],
        ['TC-03', 'Accurate Hold', 'User assumes 90 deg knee bend for Warrior II', 'Overlay turns green; hold timer increments smoothly', 'PASSED'],
        ['TC-04', 'Deviation Feedback', 'User straightens front knee to 140 deg', 'Timer pauses; voice prompts "Bend your front knee"', 'PASSED'],
        ['TC-05', 'Audio Debounce Throttle', 'User rapidly fluctuates knee across 3s', 'Voice speaks once; suppresses speech for 4 seconds', 'PASSED'],
        ['TC-06', 'Offline Persistence', 'User finishes workout and exits app', 'Session duration, accuracy & streak saved in AsyncStorage', 'PASSED']
    ]
    for r in tc_rows:
        row_cells = t_tc.add_row().cells
        for i, v in enumerate(r):
            row_cells[i].text = v
            p = row_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 4] else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size = Pt(9.5)
