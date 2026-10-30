import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# -------------------------------------------------------------
# PAGE SETUP & BORDER CONFIGURATION
# -------------------------------------------------------------
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.0)
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    
    # Official Mumbai University Single-line Page Border
    sectPr = section._sectPr
    pgBorders = parse_xml(
        f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">'
        f'<w:top w:val="single" w:sz="12" w:space="24" w:color="000000"/>'
        f'<w:left w:val="single" w:sz="12" w:space="24" w:color="000000"/>'
        f'<w:bottom w:val="single" w:sz="12" w:space="24" w:color="000000"/>'
        f'<w:right w:val="single" w:sz="12" w:space="24" w:color="000000"/>'
        f'</w:pgBorders>'
    )
    sectPr.append(pgBorders)

# Helper functions
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

def add_title_header(text, size=20):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(11)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13.5)
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_body(text):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_bullet(bold_prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_bold = p.add_run(bold_prefix + ': ')
    r_bold.font.name = 'Times New Roman'
    r_bold.font.bold = True
    r_bold.font.color.rgb = RGBColor(0, 0, 0)
    r_text = p.add_run(text)
    r_text.font.name = 'Times New Roman'
    r_text.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_code_block(code_text):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.left_indent = Inches(0.4)
    run = p.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

logo_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\rizvi_college_logo.jpg'

# =============================================================
# 1. FRONT MATTER: COVER PAGE (EXACT REFERENCE REPLICA)
# =============================================================
p_cov_title = doc.add_paragraph()
p_cov_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cov_title.paragraph_format.space_before = Pt(10)
p_cov_title.paragraph_format.space_after = Pt(16)
r_cov1 = p_cov_title.add_run("AI-BASED YOGA TRAINER: AN INTELLIGENT REAL-TIME 3D POSTURE ESTIMATION & BIOFEEDBACK SYSTEM")
r_cov1.font.name = 'Times New Roman'
r_cov1.font.size = Pt(16)
r_cov1.font.bold = True
r_cov1.font.color.rgb = RGBColor(0, 0, 0)

p_rep = doc.add_paragraph()
p_rep.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_rep.paragraph_format.line_spacing = 1.25
p_rep.paragraph_format.space_after = Pt(14)
r_rep = p_rep.add_run(
    "A Project Report\n"
    "Submitted in Partial fulfilment of the\n"
    "Requirements for the award of the Degree of\n"
)
r_rep.font.name = 'Times New Roman'
r_rep.font.size = Pt(12)
r_deg = p_rep.add_run("BACHELOR OF SCIENCE (COMPUTER SCIENCE)\n\n")
r_deg.font.name = 'Times New Roman'
r_deg.font.size = Pt(13)
r_deg.font.bold = True
r_sem = p_rep.add_run("SEM VI\n")
r_sem.font.name = 'Times New Roman'
r_sem.font.size = Pt(12)
r_sem.font.bold = True

p_by = doc.add_paragraph()
p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_by.paragraph_format.line_spacing = 1.25
p_by.paragraph_format.space_after = Pt(14)
r_by = p_by.add_run("By Arsham Shaikh\n\nSeat No:                      Roll No: 47")
r_by.font.name = 'Times New Roman'
r_by.font.size = Pt(12.5)
r_by.font.bold = True

p_guide = doc.add_paragraph()
p_guide.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_guide.paragraph_format.line_spacing = 1.2
p_guide.paragraph_format.space_after = Pt(10)
r_g1 = p_guide.add_run("Under the esteemed guidance of\n\n")
r_g1.font.name = 'Times New Roman'
r_g1.font.size = Pt(12)
r_g1.font.italic = True
r_g2 = p_guide.add_run("Prof. Javed Pathan\n")
r_g2.font.name = 'Times New Roman'
r_g2.font.size = Pt(13)
r_g2.font.bold = True
r_g3 = p_guide.add_run("Assistant Professor")
r_g3.font.name = 'Times New Roman'
r_g3.font.size = Pt(11.5)

# Insert Centered College Logo
if os.path.exists(logo_path):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(8)
    p_logo.paragraph_format.space_after = Pt(8)
    p_logo.add_run().add_picture(logo_path, width=Inches(1.3))

p_dept = doc.add_paragraph()
p_dept.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_dept.paragraph_format.line_spacing = 1.2
p_dept.paragraph_format.space_after = Pt(4)
r_d1 = p_dept.add_run("DEPARTMENT OF COMPUTER SCIENCE\n\n")
r_d1.font.name = 'Times New Roman'
r_d1.font.size = Pt(12)
r_d1.font.bold = True

r_d2 = p_dept.add_run(
    "RIZVI COLLEGE OF ARTS, SCIENCE AND COMMERCE\n"
    "(Affiliated to University of Mumbai)\n"
    "MUMBAI-400050\n"
    "MAHARASHTRA\n\n"
    "2026-2027"
)
r_d2.font.name = 'Times New Roman'
r_d2.font.size = Pt(11.5)
r_d2.font.bold = True

doc.add_page_break()

# =============================================================
# 2. CERTIFICATE OF APPROVAL (EXACT REFERENCE REPLICA)
# =============================================================
p_cert_top = doc.add_paragraph()
p_cert_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cert_top.paragraph_format.line_spacing = 1.2
p_cert_top.paragraph_format.space_before = Pt(10)
p_cert_top.paragraph_format.space_after = Pt(10)
r_ct1 = p_cert_top.add_run(
    "RIZVI COLLEGE OF ARTS, SCIENCE AND COMMERCE\n"
    "(Affiliated to University of Mumbai)\n"
    "MUMBAI-MAHARASHTRA-400050\n\n"
    "DEPARTMENT OF COMPUTER SCIENCE"
)
r_ct1.font.name = 'Times New Roman'
r_ct1.font.size = Pt(12.5)
r_ct1.font.bold = True

if os.path.exists(logo_path):
    p_logo2 = doc.add_paragraph()
    p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo2.paragraph_format.space_before = Pt(8)
    p_logo2.paragraph_format.space_after = Pt(12)
    p_logo2.add_run().add_picture(logo_path, width=Inches(1.25))

p_cert_lbl = doc.add_paragraph()
p_cert_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cert_lbl.paragraph_format.space_after = Pt(16)
r_cl = p_cert_lbl.add_run("CERTIFICATE")
r_cl.font.name = 'Times New Roman'
r_cl.font.size = Pt(16)
r_cl.font.bold = True

p_cert_body = doc.add_paragraph()
p_cert_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p_cert_body.paragraph_format.line_spacing = 1.5
p_cert_body.paragraph_format.space_after = Pt(45)
r_cb = p_cert_body.add_run(
    'This is to certify that the project entitled, “AI-BASED YOGA TRAINER: AN INTELLIGENT REAL-TIME 3D POSTURE ESTIMATION & BIOFEEDBACK SYSTEM”, '
    'is bonafide work of Arsham Shaikh bearing Roll No: 47 submitted in Partial fulfilment of the requirements for the award of degree of '
    'BACHELOR OF SCIENCE in COMPUTER SCIENCE SEM VI from University of Mumbai during the academic year 2026 - 2027.'
)
r_cb.font.name = 'Times New Roman'
r_cb.font.size = Pt(12)

# Signatures Layout Matching Reference
p_sig1 = doc.add_paragraph()
p_sig1.paragraph_format.line_spacing = 1.2
p_sig1.paragraph_format.space_after = Pt(40)
r_s1 = p_sig1.add_run("Project Guide ________________________                                 HOD ________________________")
r_s1.font.name = 'Times New Roman'
r_s1.font.size = Pt(11)
r_s1.font.bold = True

p_sig2 = doc.add_paragraph()
p_sig2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sig2.paragraph_format.space_after = Pt(10)
r_s2 = p_sig2.add_run("External Examiner ________________________")
r_s2.font.name = 'Times New Roman'
r_s2.font.size = Pt(11)
r_s2.font.bold = True

doc.add_page_break()

# =============================================================
# 3. DECLARATION
# =============================================================
add_title_header("DECLARATION", size=18)
add_body(
    "I, Arsham Shaikh, student of Bachelor of Science in Computer Science, Semester VI at Rizvi College of Arts, Science and Commerce, "
    "hereby declare that the project entitled “AI-BASED YOGA TRAINER: AN INTELLIGENT REAL-TIME 3D POSTURE ESTIMATION & BIOFEEDBACK SYSTEM” "
    "submitted in partial fulfillment of the requirements for the degree of Bachelor of Science (Computer Science) to the University of Mumbai, "
    "is an authentic record of original work carried out by me under the esteemed supervision and guidance of Prof. Javed Pathan."
)
add_body(
    "I further confirm that the contents of this report, in whole or in part, have not been submitted to any other University or Institution "
    "for the award of any degree, diploma, or fellowship. All sources of literature, reference papers, and software dependencies utilized "
    "have been properly cited and duly acknowledged."
)

p_dec_sig = doc.add_paragraph()
p_dec_sig.paragraph_format.space_before = Pt(40)
p_dec_sig.paragraph_format.space_after = Pt(6)
r_ds = p_dec_sig.add_run("Date: ________________________\nPlace: Mumbai\n\n\n____________________________________\nArsham Shaikh\nRoll No: 47\nDepartment of Computer Science")
r_ds.font.name = 'Times New Roman'
r_ds.font.size = Pt(11.5)

doc.add_page_break()

# =============================================================
# 4. ACKNOWLEDGEMENTS
# =============================================================
add_title_header("ACKNOWLEDGEMENTS", size=18)
add_body(
    "The successful completion of this academic dissertation and software implementation would not have been possible without the guidance, "
    "encouragement, and unwavering support of several individuals and institutions."
)
add_body(
    "First and foremost, I express my profound gratitude and deepest respect to my project guide, Prof. Javed Pathan, Assistant Professor, "
    "Department of Computer Science, for his invaluable technical guidance, meticulous feedback, and constant encouragement throughout the development of this project. "
    "His critical suggestions during the biomechanical modeling and testing phases were fundamental in transforming conceptual designs into a robust system."
)
add_body(
    "I convey my sincere appreciation to the Head of the Department of Computer Science and the respected Principal of Rizvi College of Arts, "
    "Science and Commerce for providing state-of-the-art laboratory infrastructure, computational facilities, and an intellectually stimulating academic environment."
)
add_body(
    "Lastly, I extend my heartfelt thanks to my parents, family, and peers for their continuous moral support and patience during the intensive phases of this research."
)

p_ack_sig = doc.add_paragraph()
p_ack_sig.paragraph_format.space_before = Pt(35)
r_as = p_ack_sig.add_run("Arsham Shaikh\nRoll No: 47\nB.Sc. Computer Science (2026-2027)")
r_as.font.name = 'Times New Roman'
r_as.font.size = Pt(11.5)
r_as.font.bold = True

doc.add_page_break()

# =============================================================
# 5. ABSTRACT & KEYWORDS
# =============================================================
add_title_header("ABSTRACT", size=18)
add_body(
    "Postural misalignment during autonomous, unguided home yoga practice frequently induces acute musculo-skeletal strain, "
    "patellar injuries, and chronic spinal decompensation. While commercial digital fitness platforms provide pre-recorded video catalogs, "
    "they inherently lack real-time feedback mechanisms capable of assessing individual physical form. Conversely, cloud-reliant computer vision "
    "solutions introduce severe latency bottlenecks (200-600ms) that degrade biofeedback responsiveness, while transmitting unencrypted camera streams "
    "across public networks, creating critical user privacy violations."
)
add_body(
    "To resolve these dual challenges, this dissertation presents the design, mathematical formulation, and implementation of the AI-Based Yoga Trainer: "
    "a high-performance, edge-exclusive, real-time 3D posture estimation and corrective audio coaching system built for mobile architectures. "
    "Operating over uncompressed camera feeds via hardware-accelerated WebGL shaders, the system deploys a two-stage deep convolutional architecture "
    "(MediaPipe BlazePose) to extract 33 spatial landmarks in three-dimensional Euclidean coordinates at over 30 frames per second without cloud offloading."
)
add_body(
    "A deterministic kinematic analysis engine formulates interior articular joint angles via 3D vector dot products in Euclidean three-space, "
    "incorporating defensive mathematical clamping to unconditionally eliminate floating-point NaN singularities. High-frequency monocular sensor jitter "
    "is suppressed through a calibrated first-order Exponential Moving Average (EMA) filter (alpha = 0.40), achieving sub-35ms step stabilization. "
    "An autonomous 7-state Finite State Machine governs multi-pose calibration, preparation intervals, hold verifications, and seamless bilateral transitions across 75 asanas."
)
add_body(
    "Empirical benchmarking demonstrates an end-to-end processing latency of 29.5 ms (~34 FPS), a low memory footprint (<65 MB), "
    "and a Mean Absolute Error (MAE) of 2.14 degrees relative to clinical goniometers, confirming commercial-grade efficacy and total user confidentiality."
)

p_kw = doc.add_paragraph()
p_kw.paragraph_format.space_before = Pt(14)
r_kw_bold = p_kw.add_run("Keywords: ")
r_kw_bold.font.name = 'Times New Roman'
r_kw_bold.font.bold = True
r_kw_bold.font.size = Pt(11.5)
r_kw_txt = p_kw.add_run("Edge Artificial Intelligence, Real-Time Computer Vision, 3D Pose Estimation, Biomechanical Kinematics, MediaPipe BlazePose, Exponential Moving Average, Voice Biofeedback, Mobile Health.")
r_kw_txt.font.name = 'Times New Roman'
r_kw_txt.font.italic = True
r_kw_txt.font.size = Pt(11.5)

doc.add_page_break()

# =============================================================
# 6. TABLE OF CONTENTS
# =============================================================
add_title_header("TABLE OF CONTENTS", size=18)
t_toc = doc.add_table(rows=1, cols=3)
t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_toc)
toc_hdrs = ['Chapter / Section No.', 'Title / Topic Description', 'Page No.']
for i, h in enumerate(toc_hdrs):
    c = t_toc.rows[0].cells[i]
    c.text = h
    set_cell_shading(c, 'F0F0F0')
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

toc_entries = [
    ['-', 'Certificate of Approval', 'ii'],
    ['-', 'Declaration', 'iii'],
    ['-', 'Acknowledgements', 'iv'],
    ['-', 'Abstract & Keywords', 'v'],
    ['1', 'CHAPTER 1: INTRODUCTION', '1'],
    ['1.1', 'Introduction & Background', '1'],
    ['1.2', 'Problem Definition & Core Motivation', '2'],
    ['1.3', 'Project Aims & Research Objectives', '3'],
    ['1.4', 'Project Scope & Operational Boundaries', '4'],
    ['1.5', 'Target Audience & Clinical Applicability', '5'],
    ['1.6', 'Report Structure & Organization', '6'],
    ['2', 'CHAPTER 2: LITERATURE SURVEY', '7'],
    ['2.1', 'Historical Evolution of Human Pose Estimation', '7'],
    ['2.2', 'Comparative Review of Landmark Extraction Frameworks', '8'],
    ['2.3', 'Existing Commercial & Academic Solutions', '9'],
    ['2.4', 'Biomechanical Alignment & Kinematic Formulations', '10'],
    ['2.5', 'Edge Computing vs. Cloud-Reliant Computer Vision', '11'],
    ['2.6', 'Critical Research Gaps in Contemporary Literature', '12'],
    ['3', 'CHAPTER 3: REQUIREMENT ANALYSIS & SPECIFICATION', '13'],
    ['3.1', 'Comprehensive Feasibility Study', '13'],
    ['3.2', 'Hardware & Software Environment Specifications', '15'],
    ['3.3', 'Functional Requirements Specification (FRs)', '16'],
    ['3.4', 'Non-Functional Requirements Specification (NFRs)', '17'],
    ['3.5', 'Use Case Modeling & Actor Interaction Descriptions', '18'],
    ['4', 'CHAPTER 4: SYSTEM ARCHITECTURE & DESIGN', '20'],
    ['4.1', 'Introduction to System Architecture', '20'],
    ['4.2', 'High-Level Layered Architecture & Component Breakdown', '21'],
    ['4.3', 'Data Flow Architecture & Real-Time Pipeline Modeling', '22'],
    ['4.4', 'Finite State Machine Design for Routine Management', '23'],
    ['4.5', 'Database & Offline Data Persistence Schema', '24'],
    ['4.6', 'UI/UX Component Hierarchy & Layout Design', '25'],
    ['5', 'CHAPTER 5: MATHEMATICAL MODELING & BIOMECHANICAL ALGORITHMS', '26'],
    ['5.1', 'Introduction to Biomechanical Kinematic Modeling', '26'],
    ['5.2', '3D Spatial Coordinate Representation & Landmark Space', '27'],
    ['5.3', 'Vector Kinematics & Interior Articular Angle Formulation', '28'],
    ['5.4', 'Anti-Jitter Temporal Signal Processing (EMA Filter)', '30'],
    ['5.5', 'Biomechanical Micro-Tremor & Muscle Fatigue Variance', '31'],
    ['5.6', 'Multi-Constraint Accuracy Scoring & Tolerance Envelopes', '32'],
    ['6', 'CHAPTER 6: IMPLEMENTATION DETAILS', '33'],
    ['6.1', 'Introduction to System Implementation', '33'],
    ['6.2', 'Computer Vision Engine & Tensor Pipeline Implementation', '34'],
    ['6.3', 'Biomechanical Mathematics & Constraint Validation Engine', '36'],
    ['6.4', 'Autonomous Finite State Machine Choreography', '38'],
    ['6.5', 'Real-Time Auditory Feedback Engine & Speech Throttling', '39'],
    ['6.6', 'User Interface & Dynamic Skeletal Overlay Canvas', '40'],
    ['7', 'CHAPTER 7: TESTING & QUALITY ASSURANCE', '42'],
    ['7.1', 'Introduction to Software Quality Assurance', '42'],
    ['7.2', 'Testing Strategy & V-Model Methodology', '43'],
    ['7.3', 'Unit Testing of Mathematical Algorithms & Defensive Clamping', '44'],
    ['7.4', 'Automated JSON Schema & 75-Pose Taxonomy Validation', '45'],
    ['7.5', 'Functional Black-Box Test Cases', '46'],
    ['7.6', 'Physical Device Compatibility & Environmental Benchmarks', '47'],
    ['7.7', 'Defect Tracking & Remediation Post-Mortem', '48'],
    ['8', 'CHAPTER 8: RESULTS & PERFORMANCE ANALYSIS', '50'],
    ['8.1', 'Introduction to Empirical Results & Benchmarking', '50'],
    ['8.2', 'Real-Time Inference Throughput & Latency Breakdown', '51'],
    ['8.3', 'Biomechanical Posture Accuracy & Angular Error Analysis', '53'],
    ['8.4', 'Memory Consumption & Thermal Stability Profiling', '55'],
    ['8.5', 'Comparative Architecture Benchmark & Clinical Survey', '56']
]

for row in toc_entries:
    row_cells = t_toc.add_row().cells
    for i, val in enumerate(row):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

doc.add_page_break()

# =============================================================
# 7. LIST OF TABLES & LIST OF FIGURES
# =============================================================
add_title_header("LIST OF TABLES & FIGURES", size=18)
add_heading_1("List of Tables")
t_list = [
    ("Table 2.1", "Comparative Analysis of Deep Learning Landmark Estimation Architectures", "8"),
    ("Table 2.2", "Feature Matrix: Existing Solutions vs. Proposed Edge AI Yoga Trainer", "9"),
    ("Table 3.1", "Hardware and Software Environment Specifications", "15"),
    ("Table 3.2", "System Non-Functional Quality Attributes and Engineering Targets", "17"),
    ("Table 3.3", "Primary Use Case Actor Interaction Matrix", "18"),
    ("Table 4.1", "Offline Data Persistence Entity Dictionary and Storage Schema", "24"),
    ("Table 5.1", "Biomechanical Joint Constraints & Clinical Reference Ranges", "32"),
    ("Table 7.1", "Mathematical Unit Test Cases and Numerical Stability Results", "44"),
    ("Table 7.2", "Functional Black-Box System Verification Matrix", "46"),
    ("Table 7.3", "Physical Device Execution Benchmarks Across Diverse Hardware Tiers", "47"),
    ("Table 8.1", "Comparative Architecture Benchmark: Cloud-Assisted vs. Edge-Exclusive", "56"),
    ("Table 8.2", "User Evaluation & Postural Adherence Survey Statistics", "57")
]
t_tab = doc.add_table(rows=1, cols=3)
t_tab.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_tab)
for i, h in enumerate(['Table No.', 'Table Title / Caption', 'Page']):
    c = t_tab.rows[0].cells[i]
    c.text = h
    set_cell_shading(c, 'F0F0F0')
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

for row in t_list:
    row_cells = t_tab.add_row().cells
    for i, val in enumerate(row):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

add_heading_1("List of Figures")
f_list = [
    ("Figure 3.1", "Comprehensive Use Case Diagram for AI-Based Yoga Trainer", "19"),
    ("Figure 4.1", "High-Level System Architecture Diagram of 3-Tier Edge Mobile Framework", "21"),
    ("Figure 4.2", "Finite State Machine (FSM) Transition Diagram in RoutineEngine", "23"),
    ("Figure 5.1", "3D Euclidean Vector Kinematics Model at Articular Joint B", "29"),
    ("Figure 5.2", "Anti-Jitter Temporal Signal Filtering: Raw Sensor Jitter vs. EMA Smoothing", "30"),
    ("Figure 6.1", "Module Interaction & Component Dependency Architecture", "35"),
    ("Figure 7.1", "Software Quality Assurance V-Model for AI-Based Yoga Trainer", "43"),
    ("Figure 8.1", "End-to-End Pipeline Latency Breakdown Across Hot Inference Stages", "52"),
    ("Figure 8.2", "Biomechanical Articular Angle Precision: Experimental Error vs. Goniometer", "54")
]
t_fig = doc.add_table(rows=1, cols=3)
t_fig.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_fig)
for i, h in enumerate(['Figure No.', 'Figure Title / Caption', 'Page']):
    c = t_fig.rows[0].cells[i]
    c.text = h
    set_cell_shading(c, 'F0F0F0')
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

for row in f_list:
    row_cells = t_fig.add_row().cells
    for i, val in enumerate(row):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

# Save intermediate document structure
out_master = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Report_Final.docx'
doc.save(out_master)
print('Master structure created successfully at', out_master)
