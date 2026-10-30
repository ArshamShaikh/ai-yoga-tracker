import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Page Margins - Standard 1 inch for university thesis with 1.25 in left binding gutter
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.0)

# Base Style
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
    run.font.color.rgb = RGBColor(0x00, 0x20, 0x60)

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

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="888888"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="888888"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

add_chapter_title('CHAPTER 2\nLITERATURE SURVEY')

add_heading_1('2.1 Introduction to Literature Review')
add_body('A literature survey is an essential prerequisite for rigorous scientific and engineering research. In the domain of intelligent computer-assisted physical fitness and biomechanical human-computer interaction (HCI), researchers have explored various methodologies to capture human bodily movement, analyze articular kinematics, and generate actionable feedback. This chapter presents an exhaustive review of historical and contemporary literature spanning: (1) the evolution of computer vision algorithms for Human Pose Estimation (HPE); (2) comparative evaluations of modern 2D versus 3D deep-learning landmark detectors; (3) classification versus geometric rule-based posture verification paradigms; (4) an evaluation of existing commercial and academic yoga systems; and (5) a critical identification of research gaps that the present work systematically addresses.')

add_heading_1('2.2 Historical Evolution of Human Pose Estimation (HPE)')
add_body('Human Pose Estimation (HPE) is a foundational problem in computer vision that seeks to determine the spatial coordinates of human anatomical joints (e.g., knees, elbows, shoulders, ankles) from monocular optical image frames or video sequences. The discipline has undergone three distinct evolutionary epochs:')

add_heading_2('2.2.1 Classical Computer Vision Epoch (Pre-2012)')
add_body('Prior to the deep learning revolution, early HPE methodologies relied on hand-crafted visual feature extractors and classical probabilistic graphical models. Notable approaches included:')
add_bullet('Silhouette and Background Subtraction Models', 'Segmenting the human foreground silhouette from a static camera background using Gaussian Mixture Models (GMM) or optical flow. These systems were notoriously brittle, degrading catastrophically under varying ambient lighting, non-static backgrounds, and loose-fitting athletic garments.')
add_bullet('Pictorial Structures and Deformable Part Models (DPM)', 'Felzenszwalb et al. (2005) modeled the human body as a tree-structured kinematic chain of spring-connected rigid limb parts, evaluated using Histogram of Oriented Gradients (HOG) filter templates. While theoretically robust for planar, canonical standing postures, DPMs suffered from exponential computational complexity and catastrophic failures under self-occluding non-planar joint configurations.')

add_heading_2('2.2.2 The Deep Learning 2D Epoch (2014 – 2020)')
add_body('The advent of Deep Convolutional Neural Networks (CNNs) fundamentally revolutionized human pose estimation by learning rich hierarchical visual representations directly from large-scale annotated datasets (such as MPII Human Pose and Microsoft COCO):')
add_bullet('DeepPose (Toshev & Szegedy, 2014)', 'The pioneering application of deep CNNs to pose estimation, formulating joint localization as a direct numerical regression problem. While vastly outperforming hand-crafted features, direct coordinate regression suffered from high spatial non-linearity and instability during edge cases.')
add_bullet('Part Affinity Fields & OpenPose (Cao et al., 2017)', 'A breakthrough multi-person bottom-up framework developed at Carnegie Mellon University (CMU). OpenPose introduced Part Affinity Fields (PAFs)—vector fields encoding the degree of association between limb joints—to solve multi-person keypoint clustering in real time. However, OpenPose required heavy desktop GPUs (e.g., NVIDIA GTX 1080Ti) and was computationally incapable of running on mobile edge hardware.')
add_bullet('MoveNet (Google, 2021)', 'A lightweight, bottom-up 17-keypoint model optimized for high-speed mobile browser execution using depthwise separable convolutions. MoveNet delivered rapid 30+ FPS edge execution for 2D coordinates; however, its flat projection remained structurally vulnerable to out-of-plane rotations.')

add_heading_2('2.2.3 The 3D Kinematic Epoch (2020 – Present)')
add_body('To address the profound limitations of 2D projections in athletic and medical domains, researchers introduced monocular 3D pose estimation architectures. Google Research unveiled MediaPipe BlazePose (Bazrev et al., 2020), a dedicated lightweight two-stage convolutional topology capable of inferring 33 3D landmarks in real time on mobile devices. BlazePose predicts not only pixel coordinates (X and Y) but also metric spatial depth (Z coordinate relative to the hips) and physical landmark visibility scores, representing the foundational computer vision architecture adopted in this project.')

add_heading_1('2.3 Comparative Analysis of Pose Estimation Frameworks')
add_body('To justify the architectural selection of MediaPipe BlazePose for the AI-Based Yoga Trainer, a comprehensive comparative analysis of leading open-source and industrial pose estimation frameworks was conducted across key operational criteria:')

# Table 2.1: Comparison of HPE Frameworks
table1 = doc.add_table(rows=1, cols=6)
table1.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table1)

headers = ['Framework', 'Keypoint Count', 'Spatial Dimensions', 'Inference Target', 'Edge / Mobile FPS', 'Occlusion Resilience']
hdr_cells = table1.rows[0].cells
for i, h in enumerate(headers):
    hdr_cells[i].text = h
    set_cell_shading(hdr_cells[i], 'E0E8F0')
    p = hdr_cells[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

data = [
    ['OpenPose (CMU)', '25 keypoints', '2D (X, Y)', 'Server / Heavy GPU', '< 5 FPS on Mobile', 'Low (2D projection ambiguity)'],
    ['MoveNet Lightning', '17 keypoints', '2D (X, Y)', 'Mobile Web / Edge', '30 - 45 FPS', 'Low (Limb crossing loss)'],
    ['MoveNet Thunder', '17 keypoints', '2D (X, Y)', 'Desktop / Edge', '15 - 20 FPS', 'Moderate (Flat planes only)'],
    ['MediaPipe Pose (BlazePose)', '33 keypoints', '3D (X, Y, Z Depth)', 'Mobile / WebGL Edge', '30+ FPS on Mobile', 'High (True 3D Spatial Depth)'],
    ['DensePose (Meta AI)', 'Dense Surface Mesh', '3D Surface UV', 'Server GPU Cluster', '< 1 FPS on Mobile', 'Very High (High Compute Cost)']
]

for row_data in data:
    row_cells = table1.add_row().cells
    for i, val in enumerate(row_data):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [1, 2, 4] else WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

add_body('As demonstrated in Table 2.1, MediaPipe BlazePose provides the optimal Pareto frontier: delivering true 3D spatial depth coordinates and 33 comprehensive anatomical keypoints (including full hands, ankles, and heels essential for balance poses) while maintaining smooth 30+ FPS edge execution on mobile processors.')

add_heading_1('2.4 Biomechanical Analysis & Geometric Posture Evaluation Techniques')
add_body('In the academic literature concerning AI-driven exercise evaluation, two competing paradigms exist for judging the correctness of an observed human posture:')

add_heading_2('2.4.1 End-to-End Black-Box Deep Neural Classifiers')
add_body('Numerous researchers (e.g., Islam et al., 2020; Yadav et al., 2019) have trained multi-class Convolutional Neural Networks (CNNs) or Support Vector Machines (SVMs) directly on labelled datasets of yoga pose images (such as the Yoga-82 dataset) to output a discrete label (e.g., "Warrior II - Correct" vs. "Warrior II - Incorrect"). While conceptually straightforward, this black-box approach exhibits critical academic and clinical deficiencies:')
add_bullet('Lack of Granular Explainability', 'A neural classifier outputs an opaque probability score (e.g., 0.78 confidence). It cannot explain why the posture is incorrect, nor can it identify which specific articular joint requires modification.')
add_bullet('Zero Actionable Biofeedback', 'A user cannot act upon a generic classification failure. In contrast, an athletic trainer must provide concrete physical cues (e.g., "Bend front knee by 15 degrees").')
add_bullet('Dataset Overfitting and Lighting Sensitivity', 'Image-level classifiers overfit to background decor, skin tones, and clothing textures present in training photos rather than isolating purely kinematic human angles.')

add_heading_2('2.4.2 Deterministic Geometric Rules Engines (Vector Kinematics)')
add_body('The alternative paradigm—adopted in this project—separates visual perception from biomechanical evaluation. An edge neural network is employed exclusively to extract spatial keypoints, while an independent, deterministic geometric rules engine calculates articular joint angles using vector algebra in Euclidean 3-space (R^3). For three adjacent keypoints A, B, and C (where B denotes the vertex joint):')
add_body('Vector BA = A - B\nVector BC = C - B\ncos(theta) = (Vector BA . Vector BC) / (||Vector BA|| * ||Vector BC||)')
add_body('This approach provides decisive advantages: (1) O(1) computational complexity executed in sub-millisecond time; (2) absolute mathematical explainability; (3) independent tolerance buffers for beginners versus advanced yogis; and (4) direct mapping of angular discrepancies to actionable vocal coaching commands.')

add_heading_1('2.5 Existing Commercial and Academic Yoga Coaching Systems')
add_body('To contextualize the contributions of this research, existing commercial mobile applications and academic prototypes were thoroughly examined:')

# Table 2.2: Existing Systems Review
table2 = doc.add_table(rows=1, cols=5)
table2.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table2)

headers2 = ['System Name', 'Nature of System', 'Tracking Technology', 'Real-Time Audio Coaching', 'Major Limitation']
hdr2_cells = table2.rows[0].cells
for i, h in enumerate(headers2):
    hdr2_cells[i].text = h
    set_cell_shading(hdr2_cells[i], 'E0E8F0')
    p = hdr2_cells[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.bold = True
        run.font.size = Pt(10)

data2 = [
    ['Down Dog', 'Commercial App', 'Pre-rendered VOD loops', 'Generic timer voiceover only', 'Zero optical tracking; no feedback.'],
    ['Asana Rebel', 'Commercial App', 'Follow-along video clips', 'Paced interval cues only', 'Completely passive broadcast medium.'],
    ['Zenia Yoga AI', 'Commercial App', 'Monocular 2D CV (Proprietary)', 'Basic voice prompts', 'Limited free poses; cloud analytics; 2D occlusion.'],
    ['Yoga-82 Benchmark (Verma et al., 2020)', 'Academic Research', 'Hierarchical DenseNet CNN', 'None (Offline classification)', 'Image-only classification; no angle math or live coaching.'],
    ['YogaPose-OpenPose (Santosh et al., 2021)', 'Academic Prototype', 'OpenPose 2D Keypoints', 'Text overlay on desktop GUI', 'Requires tethered desktop GPU; 2D projection jitter.'],
    ['Proposed AI Yoga Trainer', 'Production Mobile System', 'MediaPipe BlazePose 3D', 'Real-Time React Native TTS (4s cooldown)', 'Edge-only, 75 poses, zero cloud latency, full 3D spatial depth.']
]

for row_data in data2:
    row_cells = table2.add_row().cells
    for i, val in enumerate(row_data):
        row_cells[i].text = val
        p = row_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [1] else WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.size = Pt(9.5)

add_body('As evidenced by Table 2.2, existing commercial applications remain overwhelmingly passive video repositories, while prior academic prototypes are constrained to desktop environments evaluating narrow sets of 5 to 10 isolated poses without multi-pose routine state machines.')

add_heading_1('2.6 Research Gaps and Limitations in Existing Literature')
add_body('A systematic synthesis of the literature reveals four critical research and engineering gaps:')

add_bullet('Research Gap 1: Inability of 2D Estimators to Resolve Complex Spatial Binds and Twists', 'The vast majority of published academic systems rely on 2D estimators (OpenPose or MoveNet 17). In authentic yoga practice, poses such as Ardha Matsyendrasana (Half Lord of the Fishes) or Marichyasana require twisting the spine across the camera viewing axis. In 2D, the torso occludes the rear arm, collapsing coordinate estimation and triggering erroneous biofeedback.')

add_bullet('Research Gap 2: High Latency and Data Privacy Risks in Cloud Architectures', 'Commercial systems that incorporate machine learning often stream video frames over network sockets to cloud GPU backends. This introduces transmission latencies exceeding 800 milliseconds and violates home privacy. Literature lacks comprehensive edge-only architectures executing 3D keypoint inference and real-time audio synthesis wholly within the mobile client.')

add_bullet('Research Gap 3: Severely Restricted Taxonomy and Pose Coverage', 'Extant academic prototypes evaluate only 3 to 10 trivial, flat standing poses (e.g., Tree Pose, Mountain Pose, Warrior II). There is a conspicuous absence in literature of production-grade, mathematically calibrated taxonomies supporting 70+ poses encompassing therapy, prenatal, arm balances, and peak inversions.')

add_bullet('Research Gap 4: Absence of Autonomous Multi-Pose Session Choreography', 'Prior systems evaluate static snapshots in isolation. They lack a unified Finite State Machine (FSM) capable of choreographing pre-workout body framing calibration, transition countdowns, continuous isometric hold timers, and bilateral (left/right limb) progression.')

add_heading_1('2.7 Summary and Conceptual Positioning of the Proposed Work')
add_body('The literature survey conclusively demonstrates that while computer vision and deep learning have achieved remarkable strides in general human pose estimation, their clinical application to real-time yoga instruction has been crippled by 2D projection occlusion, cloud network latency, opaque black-box neural classifications, and narrow pose vocabularies.')

add_body('The proposed AI-Based Yoga Trainer strategically bridges these research gaps by synthesizing: (1) MediaPipe BlazePose 3D on-device inference; (2) an explainable O(1) geometric rules engine operating on 3D spatial vectors; (3) a comprehensive 75-pose commercial taxonomy spanning three clinical milestones; and (4) an autonomous finite state machine delivering low-latency audio-visual biofeedback completely offline.')

output_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\Chapter_2_Literature_Survey.docx'
doc.save(output_path)
print('Successfully generated Chapter_2_Literature_Survey.docx at', output_path)
