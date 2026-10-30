import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from builder_core import (
    add_title_header, add_heading_1, add_heading_2, add_heading_3,
    add_body, add_bullet, add_figure, set_cell_shading, set_table_borders
)

def build_chapter_5_design(doc):
    base_dir = r'c:\arsham\TY\MP\ai-yoga-tracker'

    doc.add_page_break()
    add_title_header(doc, "CHAPTER 5. SYSTEM DESIGN", size=20)

    add_heading_1(doc, "5.1 Introduction")
    add_body(doc, "System design translates analytical user requirements and performance constraints into rigorous engineering blueprints, modular architectural diagrams, mathematical kinematics equations, data flow representations, and deterministic state machines that guide the implementation of the AI-Based Yoga Trainer.")

    add_heading_1(doc, "5.2 System Architecture Diagram")
    add_body(doc, "The software architecture employs a decoupled, edge-exclusive three-tier framework engineered for high throughput and zero cloud dependency. Figure 5.1 illustrates the three architectural tiers:")
    add_bullet(doc, "Tier 1: Presentation & User Experience Layer", 
               "Comprises the React Native Studio HUD, responsive safe-area layout containers, glassmorphic metric cards, and a hardware-accelerated SVG Skeletal Overlay Canvas that paints green and crimson joint vectors directly over the live camera preview.")
    add_bullet(doc, "Tier 2: Computer Vision & Biomechanical Kinematics Core", 
               "Hosts the zero-copy WebGL texture bridge (YogaCamera.js), the quantized MediaPipe BlazePose 33-point 3D landmark inference engine (PoseDetector.js), the 3D vector dot-product calculation library (poseMathUtils.js), and the Exponential Moving Average low-pass signal filter.")
    add_bullet(doc, "Tier 3: State Orchestration & Offline Persistence Layer", 
               "Encompasses the 7-state Finite State Machine (RoutineEngine.js), the debounced Text-to-Speech coaching dispatcher (FeedbackEngine.js), the spatial framing assistant (CalibrationEngine.js), and the local SQLite database abstraction (StorageService.js via AsyncStorage).")
    add_figure(doc, os.path.join(base_dir, r'Documents\architecture_diagram.png'), 'Figure 5.1: High-Level System Architecture Diagram of 3-Tier Edge Mobile Framework', width_in=5.4)

    add_heading_1(doc, "5.3 Data Flow Diagram")
    add_heading_2(doc, "5.3.1 Level 0 DFD (Context Diagram)")
    add_body(doc, "The Level 0 Context Diagram (Figure 5.2) defines the system boundary. The external entity (the Yoga Practitioner) provides real-time optical camera frames and pose/routine selections. The central process (0.0 AI-Based Yoga Trainer System) computes pose metrics on-device, returning real-time graphical skeletal overlays and voice coaching cues, while storing historical records in local AsyncStorage.")
    add_figure(doc, os.path.join(base_dir, r'Documents\dfd_level_0.png'), 'Figure 5.2: Data Flow Diagram Level 0 (Context Diagram)', width_in=5.4)

    add_heading_2(doc, "5.3.2 Level 1 DFD (Pipeline Decomposition)")
    add_body(doc, "The Level 1 Data Flow Diagram (Figure 5.3) decomposes system data pipelines into six sequential processes: (1.0) Frame Acquisition & WebGL Binding; (2.0) BlazePose 3D Landmark Extraction; (3.0) Vector Kinematics & EMA Filtering; (4.0) Routine FSM & Hold Timer Tracking; (5.0) Audio Coaching & Debounced Dispatch; and (6.0) AsyncStorage History & Analytics Persistence.")
    add_figure(doc, os.path.join(base_dir, r'Documents\dfd_level_1.png'), 'Figure 5.3: Data Flow Diagram Level 1 (Decomposed Processing Pipeline)', width_in=5.4)

    add_heading_1(doc, "5.4 Activity Diagram & Workflow Modeling")
    add_body(doc, "The UML Activity Diagram (Figure 5.4) documents the execution workflow of an autonomous yoga session: from routine selection, camera mounting, spatial calibration framing check (prompting the user to step back into the mat if partially occluded), 3-2-1 countdown initiation, continuous joint angle evaluation, feedback cue dispatch, hold timer advancement, to workout persistence upon session completion.")
    add_figure(doc, os.path.join(base_dir, r'Documents\activity_diagram.png'), 'Figure 5.4: UML Activity Diagram Modeling Autonomous Workout Session Flow', width_in=4.4)

    add_heading_1(doc, "5.5 E-R Diagram & Data Persistence Schema")
    add_body(doc, "Although the edge architecture avoids relational database servers in favor of local key-value storage (AsyncStorage), internal entities are formally normalized to ensure zero data redundancy. Figure 5.5 presents the visual persistence schema diagram and Table 5.1 details the attributes:")
    
    # Add visual schema diagram matching PetCare!
    add_figure(doc, os.path.join(base_dir, r'Documents\persistence_schema_diagram.png'), 'Figure 5.5: Entity-Relationship & Offline Data Persistence Schema Diagram', width_in=5.4)

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
        ['USER_PROFILE', 'JSON Object', 'userName, experienceLevel, audioCoachEnabled, targetDailyMins', 'Stores user identity, skill tier, and audio preferences.'],
        ['WORKOUT_HISTORY', 'JSON Array', 'sessionId, timestamp, routineId, durationSecs, accuracyScore', 'Chronological log powering weekly consistency charts.'],
        ['POSE_MASTERY_MAP', 'Dictionary', 'poseId, totalPracticed, bestHoldSecs, isMastered, lastPracticed', 'Tracks individual mastery progress across 75 poses.'],
        ['STREAK_METRICS', 'JSON Object', 'currentStreakDays, longestStreakDays, lastCompletedDate', 'Calculates consecutive daily exercise adherence streak.'],
        ['ROUTINE_PRESETS', 'JSON Array', 'routineId, title, poses: [poseId, holdDuration], difficulty', 'Static curated vinyasa flow definitions and sequences.']
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
    add_body(doc, "Figure 5.6 presents the primary use case interactions between the Yoga Practitioner, the Core CV Engine, and the Local Storage subsystem, illustrating workflows for pose selection, calibration framing, real-time posture correction, workout logging, and statistical analytics exploration.")
    add_figure(doc, os.path.join(base_dir, r'Documents\use_case_diagram.png'), 'Figure 5.6: Comprehensive Use Case Diagram for AI-Based Yoga Trainer', width_in=5.4)

    add_heading_1(doc, "5.7 Finite State Machine Design (FSM)")
    add_body(doc, "Workout routines are governed by an autonomous 7-state Finite State Machine (Figure 5.7): (1) IDLE; (2) CALIBRATING; (3) PREPARING; (4) HOLDING_ACCURATE; (5) POSE_COMPLETE; (6) TRANSITION; and (7) SESSION_FINISHED. This deterministic design eliminates manual touchscreen interaction while exercising.")
    add_figure(doc, os.path.join(base_dir, r'Documents\fsm_state_diagram.png'), 'Figure 5.7: Finite State Machine (FSM) State Transition Diagram', width_in=5.4)

    add_heading_2(doc, "5.7.1 Biomechanical 3D Vector Kinematic Geometry Model")
    add_body(doc, "Figure 5.8 illustrates the spatial vector geometry model used to compute interior articular joint angles. Vectors u and v extend from joint pivot B to adjacent landmarks A and C in R^3. The angle theta is derived via the dot product with defensive domain clamping.")
    add_figure(doc, os.path.join(base_dir, r'Documents\vector_angle_geometry.png'), 'Figure 5.8: 3D Euclidean Vector Kinematics Geometry Model', width_in=4.8)

    add_heading_2(doc, "5.7.2 EMA Temporal Signal Filtering Comparison")
    add_body(doc, "Figure 5.9 compares raw optical keypoint trajectories against the calibrated Exponential Moving Average (alpha = 0.40) output, showing how high-frequency sensor noise is eliminated without introducing perceptual lag.")
    add_figure(doc, os.path.join(base_dir, r'Documents\ema_signal_smoothing.png'), 'Figure 5.9: Temporal Signal Processing: Raw Sensor Jitter vs. Calibrated EMA Smoothing', width_in=5.4)
