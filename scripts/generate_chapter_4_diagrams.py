import matplotlib.pyplot as plt
import matplotlib.patches as patches

# -------------------------------------------------------------
# DIAGRAM 1: HIGH-LEVEL SYSTEM ARCHITECTURE (Figure 4.1)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Layer 1: Presentation & UI Layer
box_ui = patches.FancyBboxPatch((0.6, 5.5), 8.8, 2.0, boxstyle="round,pad=0.1", ec="#111111", fc="#F8F9FA", lw=2)
ax.add_patch(box_ui)
ax.text(5.0, 7.2, "LAYER 1: PRESENTATION & CLIENT INTERACTION (React Native & Expo Router)", fontsize=11, fontweight='bold', ha='center', color='#111111')

ui_subboxes = [
    (1.0, 5.8, 2.3, 1.0, "Studio Live HUD\n(session.js)\nGlassmorphic Overlay"),
    (3.8, 5.8, 2.3, 1.0, "Library & Flows\n(poses.js & routines.js)\nHuman Figure Anatomy"),
    (6.6, 5.8, 2.4, 1.0, "Progress & Stats\n(activity.js & index.js)\nStreaks & Accuracy HUD")
]
for x, y, w, h, txt in ui_subboxes:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", ec="#333333", fc="#FFFFFF", lw=1.2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, fontsize=9, ha='center', va='center', fontweight='bold', color='#111111')

# Layer 2: Computer Vision & Biomechanical Math Layer
box_cv = patches.FancyBboxPatch((0.6, 2.8), 8.8, 2.2, boxstyle="round,pad=0.1", ec="#111111", fc="#F1F3F5", lw=2)
ax.add_patch(box_cv)
ax.text(5.0, 4.7, "LAYER 2: COMPUTER VISION & BIOMECHANICAL MATH CORE (Edge AI)", fontsize=11, fontweight='bold', ha='center', color='#111111')

cv_subboxes = [
    (0.9, 3.1, 2.4, 1.2, "TensorCamera WebGL\nBridge (256x256 RGB)\nZero-Copy GPU Buffer"),
    (3.7, 3.1, 2.5, 1.2, "MediaPipe BlazePose 3D\n(33 Keypoints X, Y, Z)\n30+ FPS Edge Inference"),
    (6.6, 3.1, 2.5, 1.2, "3D Vector & Angle Engine\n(poseMathUtils.js)\nEMA Smoothing & Tremors")
]
for x, y, w, h, txt in cv_subboxes:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", ec="#333333", fc="#FFFFFF", lw=1.2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, fontsize=9, ha='center', va='center', fontweight='bold', color='#111111')

# Layer 3: State Management & Service Orchestration Layer
box_svc = patches.FancyBboxPatch((0.6, 0.4), 8.8, 1.9, boxstyle="round,pad=0.1", ec="#111111", fc="#E9ECEF", lw=2)
ax.add_patch(box_svc)
ax.text(5.0, 1.95, "LAYER 3: STATE MACHINE, AUDIO COACH & LOCAL STORAGE", fontsize=11, fontweight='bold', ha='center', color='#111111')

svc_subboxes = [
    (0.9, 0.7, 2.4, 0.95, "Commercial 75 Rules\nposeConstraints.json\n6 Curated Routine Flows"),
    (3.7, 0.7, 2.5, 0.95, "RoutineEngine FSM\nCalibration, Hold Timers\n& Flow Auto-Transitions"),
    (6.6, 0.7, 2.5, 0.95, "Feedback & Storage\nReact Native TTS Coach\nAsyncStorage Analytics")
]
for x, y, w, h, txt in svc_subboxes:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", ec="#333333", fc="#FFFFFF", lw=1.2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, fontsize=9, ha='center', va='center', fontweight='bold', color='#111111')

# Connecting bi-directional arrows
ax.annotate('', xy=(5.0, 5.5), xytext=(5.0, 5.0), arrowprops=dict(facecolor='#111111', edgecolor='#111111', arrowstyle='<->', lw=2))
ax.annotate('', xy=(5.0, 2.8), xytext=(5.0, 2.3), arrowprops=dict(facecolor='#111111', edgecolor='#111111', arrowstyle='<->', lw=2))

plt.tight_layout()
out_arch = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\architecture_diagram.png'
plt.savefig(out_arch, dpi=300, bbox_inches='tight')
plt.close()
print('Architecture diagram saved at', out_arch)

# -------------------------------------------------------------
# DIAGRAM 2: FINITE STATE MACHINE (Figure 4.2)
# -------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(10, 5.5), dpi=300)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 5.5)
ax2.axis('off')

# States in RoutineEngine
states = [
    (1.1, 4.0, "IDLE\nSelect Flow"),
    (3.5, 4.0, "CALIBRATING\nCheck Framing"),
    (6.3, 4.0, "PREPARING\nCountdown (3s)"),
    (8.9, 4.0, "HOLDING\nTimer Active"),
    (8.9, 1.5, "POSE_COMPLETE\nChime Sounded"),
    (5.0, 1.5, "TRANSITION\nSwitch Pose / Side"),
    (1.1, 1.5, "SESSION_FINISH\nStore Analytics")
]

for x, y, txt in states:
    b = patches.FancyBboxPatch((x - 0.8, y - 0.45), 1.6, 0.9, boxstyle="round,pad=0.08", ec="#111111", fc="#FFFFFF", lw=1.8)
    ax2.add_patch(b)
    ax2.text(x, y, txt, fontsize=9, ha='center', va='center', fontweight='bold', color='#111111')

# State Transitions Arrows
# 1 -> 2
ax2.annotate('', xy=(2.7, 4.0), xytext=(1.9, 4.0), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.8))
ax2.text(2.3, 4.25, "Start", fontsize=8.5, ha='center', fontweight='bold')

# 2 -> 3
ax2.annotate('', xy=(5.5, 4.0), xytext=(4.3, 4.0), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.8))
ax2.text(4.9, 4.25, "Body Framed", fontsize=8.5, ha='center', fontweight='bold')

# 3 -> 4
ax2.annotate('', xy=(8.1, 4.0), xytext=(7.1, 4.0), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.8))
ax2.text(7.6, 4.25, "Countdown End", fontsize=8.5, ha='center', fontweight='bold')

# 4 -> 4 (Loop: Inaccurate)
arc = patches.Arc((8.9, 4.8), 1.2, 0.8, angle=0, theta1=20, theta2=200, ec="#555555", lw=1.5, ls='--')
ax2.add_patch(arc)
ax2.text(8.9, 5.25, "Pose Out of Bounds\n(Pause / Voice Correction)", fontsize=8, ha='center', color='#333333')

# 4 -> 5
ax2.annotate('', xy=(8.9, 1.95), xytext=(8.9, 3.55), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.8))
ax2.text(9.05, 2.75, "Hold Time\nReached", fontsize=8.5, ha='left', fontweight='bold')

# 5 -> 6
ax2.annotate('', xy=(5.8, 1.5), xytext=(8.1, 1.5), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.8))
ax2.text(7.0, 1.75, "More Poses in Flow", fontsize=8.5, ha='center', fontweight='bold')

# 6 -> 3
ax2.annotate('', xy=(6.3, 3.55), xytext=(5.0, 1.95), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.8))
ax2.text(5.2, 2.8, "Next Pose Loaded", fontsize=8.5, ha='center', fontweight='bold')

# 5 -> 7
ax2.annotate('', xy=(1.9, 1.5), xytext=(4.2, 1.5), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.8))
ax2.text(3.0, 1.75, "Flow Finished", fontsize=8.5, ha='center', fontweight='bold')

# 7 -> 1
ax2.annotate('', xy=(1.1, 3.55), xytext=(1.1, 1.95), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.8))
ax2.text(0.95, 2.75, "Reset Session", fontsize=8.5, ha='right', fontweight='bold')

plt.tight_layout()
out_fsm = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\fsm_state_diagram.png'
plt.savefig(out_fsm, dpi=300, bbox_inches='tight')
plt.close()
print('FSM state diagram saved at', out_fsm)
