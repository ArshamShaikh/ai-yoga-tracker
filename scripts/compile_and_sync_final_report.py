import os
import sys
import docx

sys.path.append(os.path.dirname(__file__))
from build_master_document import generate_document

def parse_extracted_pages():
    hp_path = r'c:\arsham\TY\MP\ai-yoga-tracker\scripts\heading_pages.txt'
    pages_map = {}
    if os.path.exists(hp_path):
        with open(hp_path, 'r', encoding='utf-8') as f:
            for line in f:
                if "|||" in line:
                    parts = line.strip().split("|||", 1)
                    if len(parts) == 2:
                        pages_map[parts[0].strip()] = parts[1].strip()
    return pages_map

def build_synchronized_toc():
    pm = parse_extracted_pages()
    
    # Structure strictly matching PetCare (Document 1)
    toc_structure = [
        # Chapter 1
        (1, "CHAPTER 1. INTRODUCTION", pm.get("CHAPTER 1. INTRODUCTION", "1")),
        (2, "1.1 Introduction", pm.get("1.1 Introduction", "1")),
        (2, "1.2 Problem Definition", pm.get("1.2 Problem Definition", "1")),
        (2, "1.3 Aim", pm.get("1.3 Aim", "2")),
        (2, "1.4 Objectives", pm.get("1.4 Objectives", "2")),
        (2, "1.5 Goal", pm.get("1.5 Goal", "3")),
        (2, "1.6 Need of the System", pm.get("1.6 Need of the System", "3")),
        (2, "1.7 Scope and Limitations", pm.get("1.7 Scope and Limitations", "3")),

        # Chapter 2
        (1, "CHAPTER 2. REQUIREMENT SPECIFICATION", pm.get("CHAPTER 2. REQUIREMENT SPECIFICATION", "4")),
        (2, "2.1 Introduction", pm.get("2.1 Introduction", "4")),
        (2, "2.2 System Environment", pm.get("2.2 System Environment", "4")),
        (2, "2.3 Software Requirements", pm.get("2.3 Software Requirements", "4")),
        (3, "2.3.1 Functional Requirements", pm.get("2.3.1 Functional Requirements", "5")),
        (3, "2.3.2 Non-Functional Requirements", pm.get("2.3.2 Non-Functional Requirements", "6")),
        (2, "2.4 Hardware Requirements", pm.get("2.4 Hardware Requirements", "7")),
        (2, "2.5 Methodology", pm.get("2.5 Methodology", "7")),
        (2, "2.6 Spiral Model", pm.get("2.6 Spiral Model", "8")),

        # Chapter 3
        (1, "CHAPTER 3. SYSTEM ANALYSIS", pm.get("CHAPTER 3. SYSTEM ANALYSIS", "10")),
        (2, "3.1 System Analysis Overview", pm.get("3.1 System Analysis Overview", "10")),
        (2, "3.2 Analysis of Existing System", pm.get("3.2 Analysis of Existing System", "10")),
        (3, "3.2.1 Comparative Analysis of Existing vs. Proposed System", pm.get("3.2.1 Comparative Analysis of Existing vs. Proposed System", "11")),
        (2, "3.3 Analysis of the Proposed System", pm.get("3.3 Analysis of the Proposed System", "12")),
        (2, "3.4 Feasibility Study", pm.get("3.4 Feasibility Study", "12")),

        # Chapter 4
        (1, "CHAPTER 4. SURVEY OF TECHNOLOGY", pm.get("CHAPTER 4. SURVEY OF TECHNOLOGY", "14")),
        (2, "4.1 React Native Framework", pm.get("4.1 React Native Framework", "14")),
        (2, "4.2 Expo SDK Ecosystem", pm.get("4.2 Expo SDK Ecosystem", "14")),
        (2, "4.3 TensorFlow.js & WebGL Acceleration", pm.get("4.3 TensorFlow.js & WebGL Acceleration", "15")),
        (2, "4.4 MediaPipe BlazePose 3D Architecture", pm.get("4.4 MediaPipe BlazePose 3D Architecture", "16")),
        (2, "4.5 Vector Kinematics & Articular Joint Geometry", pm.get("4.5 Vector Kinematics & Articular Joint Geometry", "17")),
        (2, "4.6 EMA Temporal Signal Filtering", pm.get("4.6 EMA Temporal Signal Filtering", "17")),
        (2, "4.7 AsyncStorage Offline Persistence", pm.get("4.7 AsyncStorage Offline Persistence", "18")),
        (2, "4.8 Text-to-Speech (TTS) Voice Biofeedback", pm.get("4.8 Text-to-Speech (TTS) Voice Biofeedback", "18")),

        # Chapter 5
        (1, "CHAPTER 5. SYSTEM DESIGN", pm.get("CHAPTER 5. SYSTEM DESIGN", "19")),
        (2, "5.1 Introduction", pm.get("5.1 Introduction", "19")),
        (2, "5.2 System Architecture Diagram", pm.get("5.2 System Architecture Diagram", "19")),
        (2, "5.3 Data Flow Diagram", pm.get("5.3 Data Flow Diagram", "20")),
        (3, "5.3.1 Level 0 DFD (Context Diagram)", pm.get("5.3.1 Level 0 DFD (Context Diagram)", "20")),
        (3, "5.3.2 Level 1 DFD (Pipeline Decomposition)", pm.get("5.3.2 Level 1 DFD (Pipeline Decomposition)", "21")),
        (2, "5.4 Activity Diagram & Workflow Modeling", pm.get("5.4 Activity Diagram & Workflow Modeling", "22")),
        (2, "5.5 E-R Diagram & Data Persistence Schema", pm.get("5.5 E-R Diagram & Data Persistence Schema", "23")),
        (2, "5.6 Use-Case Diagram & Actor Interaction", pm.get("5.6 Use-Case Diagram & Actor Interaction", "24")),
        (2, "5.7 Finite State Machine Design (FSM)", pm.get("5.7 Finite State Machine Design (FSM)", "25")),
        (3, "5.7.1 Biomechanical 3D Vector Kinematic Geometry Model", pm.get("5.7.1 Biomechanical 3D Vector Kinematic Geometry Model", "26")),
        (3, "5.7.2 EMA Temporal Signal Filtering Comparison", pm.get("5.7.2 EMA Temporal Signal Filtering Comparison", "27")),

        # Chapter 6
        (1, "CHAPTER 6. SYSTEM IMPLEMENTATION", pm.get("CHAPTER 6. SYSTEM IMPLEMENTATION", "29")),
        (2, "6.1 Introduction", pm.get("6.1 Introduction", "29")),
        (2, "6.2 Flowchart & Module Architecture", pm.get("6.2 Flowchart & Module Architecture", "29")),
        (2, "6.3 Coding", pm.get("6.3 Coding", "30")),
        (3, "6.3.1 Frontend Implementation", pm.get("6.3.1 Frontend Implementation", "30")),
        (3, "6.3.1.1 Camera Studio HUD & Pipeline (app/session.js)", pm.get("6.3.1.1 Camera Studio HUD & Pipeline (app/session.js)", "30")),
        (3, "6.3.1.2 SVG Skeletal Overlay Canvas (src/components/PoseOverlay.js)", pm.get("6.3.1.2 SVG Skeletal Overlay Canvas (src/components/PoseOverlay.js)", "34")),
        (3, "6.3.1.3 Anatomical Guidance & Instruction Modal (src/components/PoseGuideModal.js)", pm.get("6.3.1.3 Anatomical Guidance & Instruction Modal (src/components/PoseGuideModal.js)", "36")),
        (3, "6.3.1.4 Home Studio Dashboard (app/(tabs)/index.js)", pm.get("6.3.1.4 Home Studio Dashboard (app/(tabs)/index.js)", "39")),
        (3, "6.3.1.5 Asana Taxonomy Repository (app/(tabs)/poses.js)", pm.get("6.3.1.5 Asana Taxonomy Repository (app/(tabs)/poses.js)", "42")),
        (3, "6.3.1.6 Curated Vinyasa Flows (app/(tabs)/routines.js)", pm.get("6.3.1.6 Curated Vinyasa Flows (app/(tabs)/routines.js)", "45")),
        (3, "6.3.1.7 Practice Analytics & History (app/(tabs)/activity.js)", pm.get("6.3.1.7 Practice Analytics & History (app/(tabs)/activity.js)", "48")),
        (3, "6.3.2 Backend & Mathematical Core Implementation", pm.get("6.3.2 Backend & Mathematical Core Implementation", "51")),
        (3, "6.3.2.1 3D Vector Kinematics & Signal Filtering (src/utils/poseMathUtils.js)", pm.get("6.3.2.1 3D Vector Kinematics & Signal Filtering (src/utils/poseMathUtils.js)", "51")),
        (3, "6.3.2.2 Autonomous Routine Orchestration FSM (src/services/RoutineEngine.js)", pm.get("6.3.2.2 Autonomous Routine Orchestration FSM (src/services/RoutineEngine.js)", "53")),
        (3, "6.3.2.3 Prioritized Voice Biofeedback Dispatcher (src/services/FeedbackEngine.js)", pm.get("6.3.2.3 Prioritized Voice Biofeedback Dispatcher (src/services/FeedbackEngine.js)", "56")),
        (3, "6.3.2.4 Offline Persistence Layer (src/services/StorageService.js)", pm.get("6.3.2.4 Offline Persistence Layer (src/services/StorageService.js)", "59")),
        (3, "6.3.2.5 Spatial Calibration & Framing Assistant (src/utils/CalibrationEngine.js)", pm.get("6.3.2.5 Spatial Calibration & Framing Assistant (src/utils/CalibrationEngine.js)", "62")),
        (3, "6.3.2.6 BlazePose 33-Landmark Architectural Schema (src/constants/landmarks.js)", pm.get("6.3.2.6 BlazePose 33-Landmark Architectural Schema (src/constants/landmarks.js)", "65")),
        (2, "6.4 Testing Approaches & Quality Assurance", pm.get("6.4 Testing Approaches & Quality Assurance", "68")),
        (3, "6.4.1 Unit Testing of Mathematical Core", pm.get("6.4.1 Unit Testing of Mathematical Core", "68")),
        (3, "6.4.2 Usability Testing", pm.get("6.4.2 Usability Testing", "69")),
        (3, "6.4.3 Security & Zero-Cloud Privacy Testing", pm.get("6.4.3 Security & Zero-Cloud Privacy Testing", "69")),
        (3, "6.4.4 Test Cases & Execution Matrix", pm.get("6.4.4 Test Cases & Execution Matrix", "70")),

        # Chapter 7
        (1, "CHAPTER 7. RESULTS", pm.get("CHAPTER 7. RESULTS", "72")),
        (2, "7.1 Introduction", pm.get("7.1 Introduction", "72")),
        (2, "7.2 User Interface & Visual System Results", pm.get("7.2 User Interface & Visual System Results", "72")),
        (3, "7.2.1 Studio Home Dashboard & Daily Tracking", pm.get("7.2.1 Studio Home Dashboard & Daily Tracking", "72")),
        (3, "7.2.2 Asana Repository & 75-Pose Taxonomy Library", pm.get("7.2.2 Asana Repository & 75-Pose Taxonomy Library", "74")),
        (3, "7.2.3 Curated Vinyasa Flows & Multi-Pose Routines", pm.get("7.2.3 Curated Vinyasa Flows & Multi-Pose Routines", "76")),
        (3, "7.2.4 Therapeutic Programs Selection & Modalities", pm.get("7.2.4 Therapeutic Programs Selection & Modalities", "78")),
        (3, "7.2.5 Practice Analytics & Biomechanical Tracking", pm.get("7.2.5 Practice Analytics & Biomechanical Tracking", "80")),
        (2, "7.3 Quantitative Performance & Latency Benchmarks", pm.get("7.3 Quantitative Performance & Latency Benchmarks", "82")),
        (3, "7.3.1 Real-Time Inference Latency Profiling", pm.get("7.3.1 Real-Time Inference Latency Profiling", "82")),
        (3, "7.3.2 Biomechanical Articular Angle Precision", pm.get("7.3.2 Biomechanical Articular Angle Precision", "83")),
        (3, "7.3.3 Comparative Architecture Benchmark", pm.get("7.3.3 Comparative Architecture Benchmark", "84")),
        (3, "7.3.4 User Evaluation & System Usability Survey", pm.get("7.3.4 User Evaluation & System Usability Survey", "85")),
        (2, "7.4 Overall Result & Discussion", pm.get("7.4 Overall Result & Discussion", "86")),

        # Chapter 8
        (1, "CHAPTER 8. CONCLUSION AND FUTURE SCOPE", pm.get("CHAPTER 8. CONCLUSION AND FUTURE SCOPE", "87")),
        (2, "8.1 Conclusion", pm.get("8.1 Conclusion", "87")),
        (2, "8.2 Future Scope and Enhancement", pm.get("8.2 Future Scope and Enhancement", "87")),

        # Chapter 9
        (1, "CHAPTER 9. REFERENCE", pm.get("CHAPTER 9. REFERENCE", "89"))
    ]
    return toc_structure

def main():
    print("=" * 60)
    print("BUILDING 90+ PAGE MASTER PROJECT REPORT WITH 100% SYNC TOC")
    print("=" * 60)
    
    synchronized_toc = build_synchronized_toc()
    print(f"Loaded {len(synchronized_toc)} TOC entries.")
    
    final_docx_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Final.docx'
    generate_document(toc_data=synchronized_toc, output_path=final_docx_path)
    print("Document successfully compiled.")

if __name__ == "__main__":
    main()
