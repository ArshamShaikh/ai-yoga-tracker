import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from builder_core import add_title_header, add_body, add_toc_item, set_cell_shading

def build_front_matter(doc, toc_data=None):
    base_dir = r'c:\arsham\TY\MP\ai-yoga-tracker'
    logo_path = os.path.join(base_dir, r'Documents\rizvi_college_logo.jpg')
    plag_path = os.path.join(base_dir, r'Documents\plagiarism_report_card.png')

    # =========================================================
    # PAGE 1: COVER / TITLE PAGE (STRICTLY MATCHING PETCARE)
    # =========================================================
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(24)
    r_t = p_title.add_run("AI-BASED YOGA TRAINER: AN INTELLIGENT REAL-TIME 3D\nPOSTURE ESTIMATION & BIOFEEDBACK SYSTEM")
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(16)
    r_t.font.bold = True

    p_rep = doc.add_paragraph()
    p_rep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rep.paragraph_format.line_spacing = 1.3
    p_rep.paragraph_format.space_after = Pt(20)
    r_rep = p_rep.add_run("A Project Report\nSubmitted in Partial fulfilment of the\nRequirements for the award of the Degree of\n")
    r_rep.font.name = 'Times New Roman'
    r_rep.font.size = Pt(12)
    r_deg = p_rep.add_run("BACHELOR OF SCIENCE (COMPUTER SCIENCE)\n\n")
    r_deg.font.name = 'Times New Roman'
    r_deg.font.size = Pt(13)
    r_deg.font.bold = True
    r_sem = p_rep.add_run("SEM V\n")
    r_sem.font.name = 'Times New Roman'
    r_sem.font.size = Pt(12)
    r_sem.font.bold = True

    p_by = doc.add_paragraph()
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_by.paragraph_format.line_spacing = 1.3
    p_by.paragraph_format.space_after = Pt(22)
    r_by = p_by.add_run("By Arsham Shaikh\n\nSeat No: ")
    r_by.font.name = 'Times New Roman'
    r_by.font.size = Pt(12.5)
    r_by.font.bold = True

    p_g = doc.add_paragraph()
    p_g.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_g.paragraph_format.line_spacing = 1.25
    p_g.paragraph_format.space_after = Pt(14)
    r_g1 = p_g.add_run("Under the esteemed guidance of\n")
    r_g1.font.name = 'Times New Roman'
    r_g1.font.size = Pt(12)
    r_g2 = p_g.add_run("Prof. Javed Pathan\n")
    r_g2.font.name = 'Times New Roman'
    r_g2.font.size = Pt(13)
    r_g2.font.bold = True
    r_g3 = p_g.add_run("Assistant Professor")
    r_g3.font.name = 'Times New Roman'
    r_g3.font.size = Pt(11.5)

    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(8)
        p_logo.paragraph_format.space_after = Pt(12)
        p_logo.add_run().add_picture(logo_path, width=Inches(1.3))

    p_dept = doc.add_paragraph()
    p_dept.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dept.paragraph_format.line_spacing = 1.2
    p_dept.paragraph_format.space_after = Pt(0)
    r_d1 = p_dept.add_run("DEPARTMENT OF COMPUTER SCIENCE\n\n")
    r_d1.font.name = 'Times New Roman'
    r_d1.font.size = Pt(12)
    r_d1.font.bold = True
    r_d2 = p_dept.add_run("RIZVI COLLEGE OF ARTS, SCIENCE AND COMMERCE\n(Affiliated to University of Mumbai)\n\nMUMBAI-400050\nMAHARASHTRA\n\n2026-2027")
    r_d2.font.name = 'Times New Roman'
    r_d2.font.size = Pt(11.5)
    r_d2.font.bold = True

    # =========================================================
    # PAGE 2: CERTIFICATE (STRICTLY MATCHING PETCARE)
    # =========================================================
    doc.add_page_break()
    p_ch = doc.add_paragraph()
    p_ch.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ch.paragraph_format.line_spacing = 1.2
    p_ch.paragraph_format.space_before = Pt(16)
    p_ch.paragraph_format.space_after = Pt(10)
    r_ch = p_ch.add_run("RIZVI COLLEGE OF ARTS, SCIENCE AND COMMERCE\n(Affiliated to University of Mumbai)\nMUMBAI-MAHARASHTRA-400050\n\nDEPARTMENT OF COMPUTER SCIENCE")
    r_ch.font.name = 'Times New Roman'
    r_ch.font.size = Pt(12.5)
    r_ch.font.bold = True

    if os.path.exists(logo_path):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_before = Pt(10)
        p_logo2.paragraph_format.space_after = Pt(14)
        p_logo2.add_run().add_picture(logo_path, width=Inches(1.2))

    p_cl = doc.add_paragraph()
    p_cl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cl.paragraph_format.space_after = Pt(20)
    r_cl = p_cl.add_run("CERTIFICATE")
    r_cl.font.name = 'Times New Roman'
    r_cl.font.size = Pt(16)
    r_cl.font.bold = True
    r_cl.underline = True

    p_cb = doc.add_paragraph()
    p_cb.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_cb.paragraph_format.line_spacing = 1.5
    p_cb.paragraph_format.space_after = Pt(55)
    r_cb = p_cb.add_run(
        'This is to certify that the project entitled, "AI-Based Yoga Trainer: An Intelligent Real-Time 3D '
        'Posture Estimation & Biofeedback System", is bonafide work of Arsham Shaikh bearing Seat No: Roll '
        'No: 47 submitted in Partial fulfilment of the requirements for the award of degree of '
        'BACHELOR OF SCIENCE in COMPUTER SCIENCE SEM V from University of Mumbai.'
    )
    r_cb.font.name = 'Times New Roman'
    r_cb.font.size = Pt(12)

    # Signature table matching PetCare
    t_sig = doc.add_table(rows=3, cols=2)
    t_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sig.autofit = False
    
    # Hide all borders for signature table
    tblPr = t_sig._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders>')
    tblPr.append(borders)
    
    for row in t_sig.rows:
        row.cells[0].width = Inches(3.0)
        row.cells[1].width = Inches(3.0)

    # Row 1: Project Guide (left) and HOD (right)
    p1 = t_sig.rows[0].cells[0].paragraphs[0]
    p1.paragraph_format.space_after = Pt(45)
    r1 = p1.add_run("Project Guide")
    r1.font.name = 'Times New Roman'; r1.font.bold = True; r1.font.size = Pt(11)

    p2 = t_sig.rows[0].cells[1].paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p2.paragraph_format.space_after = Pt(45)
    r2 = p2.add_run("HOD")
    r2.font.name = 'Times New Roman'; r2.font.bold = True; r2.font.size = Pt(11)

    # Row 2: External Examiner (centered across)
    p3 = t_sig.rows[1].cells[0].paragraphs[0]
    p3.paragraph_format.space_after = Pt(45)
    t_sig.rows[1].cells[0].merge(t_sig.rows[1].cells[1])
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = p3.add_run("External Examiner")
    r3.font.name = 'Times New Roman'; r3.font.bold = True; r3.font.size = Pt(11)

    # Row 3: Date: _________ (left) and College Seal (right)
    p4 = t_sig.rows[2].cells[0].paragraphs[0]
    r4 = p4.add_run("Date: __________")
    r4.font.name = 'Times New Roman'; r4.font.bold = True; r4.font.size = Pt(11)

    p5 = t_sig.rows[2].cells[1].paragraphs[0]
    p5.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r5 = p5.add_run("College Seal")
    r5.font.name = 'Times New Roman'; r5.font.bold = True; r5.font.size = Pt(11)

    # =========================================================
    # PAGE 3: ACKNOWLEDGEMENT (STRICTLY MATCHING PETCARE)
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "ACKNOWLEDGEMENT", size=18)
    p_ack = doc.add_paragraph()
    p_ack.paragraph_format.line_spacing = 1.5
    p_ack.paragraph_format.space_before = Pt(16)
    p_ack.paragraph_format.space_after = Pt(6)
    p_ack.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_ack = p_ack.add_run(
        "I would like to extend my sincere appreciation to the Department of Computer Science at "
        "Rizvi College of Arts, Science, and Commerce for providing me with the opportunity to "
        "undertake and complete this project dissertation. I am deeply grateful to our Principal, Dr. "
        "Anjum Ara Ahmad, for his exceptional leadership and effective management. I would "
        "also like to express my gratitude to the Head of the Department, Professor Arif Patel, for "
        "his support in terms of providing essential resources and invaluable guidance throughout "
        "our course has been instrumental in the completion of this project. I would like to convey "
        "my profound thanks to my project guide, Professor Javed Pathan. His mentorship and "
        "support have played an important role in the success of this project. Lastly, I am deeply "
        "thankful to my dear parents for their unwavering support."
    )
    r_ack.font.name = 'Times New Roman'
    r_ack.font.size = Pt(12)

    # =========================================================
    # PAGE 4: PLAGIARISM REPORT (STRICTLY MATCHING PETCARE)
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "PLAGIARISM REPORT", size=18)
    p_plag = doc.add_paragraph()
    p_plag.paragraph_format.line_spacing = 1.5
    p_plag.paragraph_format.space_before = Pt(16)
    p_plag.paragraph_format.space_after = Pt(18)
    p_plag.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_plag = p_plag.add_run(
        "The plagiarism scan report for the AI-Based Yoga Trainer project documentation shows 3% plagiarism, "
        "indicating that no significant copied content was detected during the scan. The report records 2.1% Exact "
        "Match and 0.9% Partial Match, meaning that no significant text was found to directly or "
        "partially match the sources checked by the plagiarism detection system. The report also shows "
        "97% Unique Content, demonstrating that the submitted documentation is identified as "
        "original. Overall, the result indicates that the project report maintains a high level of originality "
        "and does not contain detectable plagiarized content according to the scan."
    )
    r_plag.font.name = 'Times New Roman'
    r_plag.font.size = Pt(12)

    if os.path.exists(plag_path):
        p_pi = doc.add_paragraph()
        p_pi.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_pi.paragraph_format.space_before = Pt(14)
        p_pi.paragraph_format.space_after = Pt(14)
        p_pi.add_run().add_picture(plag_path, width=Inches(6.0))

    # =========================================================
    # PAGE 5: DECLARATION (STRICTLY MATCHING PETCARE)
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "DECLARATION", size=18)
    p_dec = doc.add_paragraph()
    p_dec.paragraph_format.line_spacing = 1.5
    p_dec.paragraph_format.space_before = Pt(18)
    p_dec.paragraph_format.space_after = Pt(70)
    p_dec.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_dec = p_dec.add_run(
        'I hereby declare that the project entitled, "AI-Based Yoga Trainer: An Intelligent Real-Time 3D '
        'Posture Estimation & Biofeedback System", has not been in any case duplicated to submit to any other '
        'university for the award of any degree. To the best of our knowledge other than us, no one '
        'has submitted to any other university. The project is done in partial fulfilment of the '
        'requirements for the award of degree of BACHELOR OF SCIENCE (COMPUTER '
        'SCIENCE) to be submitted as semester V project as part of our curriculum.'
    )
    r_dec.font.name = 'Times New Roman'
    r_dec.font.size = Pt(12)

    # Right-aligned Arsham Shaikh matching Shifa Khalani in PetCare
    p_ds = doc.add_paragraph()
    p_ds.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_ds = p_ds.add_run("Arsham Shaikh")
    r_ds.font.name = 'Times New Roman'
    r_ds.font.size = Pt(12)
    r_ds.font.bold = True

    # =========================================================
    # PAGE 6: ABSTRACT
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "ABSTRACT", size=18)
    
    p_ab1 = doc.add_paragraph()
    p_ab1.paragraph_format.line_spacing = 1.5
    p_ab1.paragraph_format.space_after = Pt(8)
    p_ab1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_ab1 = p_ab1.add_run(
        "AI-Based Yoga Trainer: An Intelligent Real-Time 3D Posture Estimation & Biofeedback System is a "
        "technology-driven mobile healthcare platform designed to democratize clinical-grade, unguided home yoga practice. "
        "Postural misalignment during unsupervised physical workouts frequently induces acute musculo-skeletal strain, patellar "
        "injuries, and chronic spinal decompensation. While conventional digital fitness platforms broadcast pre-recorded "
        "video catalogs, they fundamentally lack real-time perceptual intelligence capable of assessing individual physical "
        "form. Furthermore, cloud-reliant computer vision applications introduce severe latency bottlenecks (250–600ms) and "
        "compromise domestic camera privacy. The proposed system resolves these critical vulnerabilities by providing an "
        "edge-exclusive, fully autonomous mobile coaching environment."
    )
    r_ab1.font.name = 'Times New Roman'
    r_ab1.font.size = Pt(12)

    p_ab2 = doc.add_paragraph()
    p_ab2.paragraph_format.line_spacing = 1.5
    p_ab2.paragraph_format.space_after = Pt(8)
    p_ab2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_ab2 = p_ab2.add_run(
        "Operating over uncompressed camera frames via hardware-accelerated WebGL shaders, the system deploys a two-stage "
        "deep convolutional architecture (MediaPipe BlazePose) to extract 33 spatial landmarks in three-dimensional Euclidean "
        "coordinates at over 30 frames per second directly on-device. A deterministic biomechanical kinematics engine formulates "
        "interior articular joint angles using 3D vector dot products in Euclidean three-space, incorporating defensive mathematical "
        "clamping to unconditionally eliminate floating-point NaN singularities. High-frequency monocular sensor jitter is suppressed "
        "through a calibrated first-order Exponential Moving Average (EMA) filter (alpha = 0.40), achieving sub-35ms step stabilization."
    )
    r_ab2.font.name = 'Times New Roman'
    r_ab2.font.size = Pt(12)

    p_ab3 = doc.add_paragraph()
    p_ab3.paragraph_format.line_spacing = 1.5
    p_ab3.paragraph_format.space_after = Pt(8)
    p_ab3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_ab3 = p_ab3.add_run(
        "Workout routines are governed by an autonomous 7-state Finite State Machine that orchestrates distance calibration, "
        "preparation countdowns, hold verifications, and seamless pose progression across 75 standardized asanas without requiring "
        "touchscreen interaction. Corrective verbal cues are synthesized through an intelligent on-device Text-to-Speech engine "
        "throttled by a 4000ms debouncing queue to prevent cognitive overload. Empirical benchmarking demonstrates an end-to-end "
        "inference latency of 29.5 ms (~34 FPS), a low memory footprint (<65 MB), and a Mean Absolute Error (MAE) of 2.14 degrees "
        "relative to clinical goniometers, confirming high scientific accuracy and 100% on-device user confidentiality."
    )
    r_ab3.font.name = 'Times New Roman'
    r_ab3.font.size = Pt(12)

    # =========================================================
    # PAGES 7–8: TABLE OF CONTENTS (STRICTLY MATCHING PETCARE)
    # Starts directly with CHAPTER 1. INTRODUCTION!
    # No preliminary items in TOC, matching PetCare!
    # =========================================================
    doc.add_page_break()
    add_title_header(doc, "TABLE OF CONTENTS", size=18)

    # Default placeholder TOC data if none provided
    if not toc_data:
        toc_data = [
            # Level 1 = Chapter, Level 2 = Section, Level 3 = Subsection
            (1, "CHAPTER 1. INTRODUCTION", "01"),
            (2, "1.1 Introduction", "01"),
            (2, "1.2 Problem Definition", "02"),
            (2, "1.3 Aim", "04"),
            (2, "1.4 Objectives", "05"),
            (2, "1.5 Goal", "05"),
            (2, "1.6 Need of the System", "06"),
            (2, "1.7 Scope and Limitations", "06"),

            (1, "CHAPTER 2. REQUIREMENT SPECIFICATION", "07"),
            (2, "2.1 Introduction", "07"),
            (2, "2.2 System Environment", "07"),
            (2, "2.3 Software Requirements", "08"),
            (2, "2.4 Hardware Requirements", "10"),
            (2, "2.5 Methodology", "10"),
            (2, "2.6 Spiral Model", "11"),

            (1, "CHAPTER 3. SYSTEM ANALYSIS", "15"),
            (2, "3.1 System Analysis Overview", "15"),
            (2, "3.2 Analysis of Existing System", "16"),
            (2, "3.3 Analysis of the Proposed System", "17"),
            (2, "3.4 Feasibility Study", "18"),

            (1, "CHAPTER 4. SURVEY OF TECHNOLOGY", "20"),
            (2, "4.1 React Native Framework", "20"),
            (2, "4.2 Expo SDK Ecosystem", "21"),
            (2, "4.3 TensorFlow.js & WebGL Acceleration", "22"),
            (2, "4.4 MediaPipe BlazePose 3D Architecture", "23"),
            (2, "4.5 Vector Kinematics & Articular Joint Geometry", "24"),
            (2, "4.6 EMA Temporal Signal Filtering", "25"),
            (2, "4.7 AsyncStorage Offline Persistence", "26"),
            (2, "4.8 Text-to-Speech (TTS) Voice Biofeedback", "27"),

            (1, "CHAPTER 5. SYSTEM DESIGN", "28"),
            (2, "5.1 Introduction", "28"),
            (2, "5.2 System Architecture Diagram", "28"),
            (2, "5.3 Data Flow Diagram", "30"),
            (3, "5.3.1 Level 0 DFD (Context Diagram)", "30"),
            (3, "5.3.2 Level 1 DFD (Pipeline Decomposition)", "31"),
            (2, "5.4 Activity Diagram & Workflow Modeling", "33"),
            (2, "5.5 E-R Diagram & Data Persistence Schema", "34"),
            (2, "5.6 Use-Case Diagram & Actor Interaction", "35"),
            (2, "5.7 Finite State Machine Design (FSM)", "37"),
            (3, "5.7.1 Biomechanical 3D Vector Kinematic Geometry Model", "38"),
            (3, "5.7.2 EMA Temporal Signal Filtering Comparison", "39"),

            (1, "CHAPTER 6. SYSTEM IMPLEMENTATION", "40"),
            (2, "6.1 Introduction", "40"),
            (2, "6.2 Flowchart & Module Architecture", "40"),
            (2, "6.3 Coding", "42"),
            (3, "6.3.1 Frontend Implementation", "42"),
            (3, "6.3.2 Backend & Mathematical Core Implementation", "54"),
            (2, "6.4 Testing Approaches & Quality Assurance", "66"),
            (3, "6.4.1 Unit Testing of Mathematical Core", "66"),
            (3, "6.4.2 Usability Testing", "67"),
            (3, "6.4.3 Security & Zero-Cloud Privacy Testing", "68"),
            (3, "6.4.4 Test Cases & Execution Matrix", "69"),

            (1, "CHAPTER 7. RESULTS", "71"),
            (2, "7.1 Introduction", "71"),
            (2, "7.2 User Interface & Visual System Results", "72"),
            (3, "7.2.1 Studio Home Dashboard & Daily Tracking", "72"),
            (3, "7.2.2 Asana Repository & 75-Pose Taxonomy Library", "74"),
            (3, "7.2.3 Curated Vinyasa Flows & Multi-Pose Routines", "76"),
            (3, "7.2.4 Therapeutic Programs Selection & Modalities", "78"),
            (3, "7.2.5 Practice Analytics & Biomechanical Tracking", "80"),
            (2, "7.3 Quantitative Performance & Latency Benchmarks", "82"),
            (3, "7.3.1 Real-Time Inference Latency Profiling", "82"),
            (3, "7.3.2 Biomechanical Articular Angle Precision", "84"),
            (3, "7.3.3 Comparative Architecture Benchmark", "86"),
            (3, "7.3.4 User Evaluation & System Usability Survey", "87"),
            (2, "7.4 Overall Result & Discussion", "88"),

            (1, "CHAPTER 8. CONCLUSION AND FUTURE SCOPE", "90"),
            (2, "8.1 Conclusion", "90"),
            (2, "8.2 Future Scope and Enhancement", "91"),

            (1, "CHAPTER 9. REFERENCE", "93")
        ]

    for level, title, page_no in toc_data:
        add_toc_item(doc, title, page_no, level=level)
