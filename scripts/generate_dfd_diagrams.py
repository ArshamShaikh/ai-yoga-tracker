import matplotlib.pyplot as plt
import matplotlib.patches as patches

# -------------------------------------------------------------
# DFD LEVEL 0 (CONTEXT DIAGRAM)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# External Entity: User / Practitioner
user_box = patches.FancyBboxPatch((0.5, 1.8), 2.2, 1.4, boxstyle="round,pad=0.1", ec="#1D3557", fc="#EBF2FA", lw=2)
ax.add_patch(user_box)
ax.text(1.6, 2.5, "YOGA\nPRACTITIONER\n(External Entity)", fontsize=9.5, fontweight='bold', color="#1D3557", ha="center", va="center")

# Central Process: 0.0 AI-Based Yoga Trainer System
proc_circle = patches.Circle((5.0, 2.5), 1.35, ec="#2A9D8F", fc="#E8F8F5", lw=2.5)
ax.add_patch(proc_circle)
ax.text(5.0, 2.75, "0.0", fontsize=11, fontweight='bold', color="#2A9D8F", ha="center")
ax.text(5.0, 2.35, "AI-BASED\nYOGA TRAINER\nSYSTEM", fontsize=9.5, fontweight='bold', color="#1D3557", ha="center")

# External Storage: Local Storage
store_box = patches.FancyBboxPatch((7.3, 1.8), 2.2, 1.4, boxstyle="round,pad=0.1", ec="#E76F51", fc="#FDF2E9", lw=2)
ax.add_patch(store_box)
ax.text(8.4, 2.5, "LOCAL PERSISTENT\nSTORAGE\n(AsyncStorage)", fontsize=9.5, fontweight='bold', color="#E76F51", ha="center", va="center")

# Arrows: User -> Process
ax.annotate("", xy=(3.65, 2.9), xytext=(2.7, 2.9), arrowprops=dict(arrowstyle="->", lw=1.8, color="#1D3557"))
ax.text(3.18, 3.1, "Camera Stream\n& Pose Selection", fontsize=8, color="#1D3557", ha="center")

# Arrows: Process -> User
ax.annotate("", xy=(2.7, 2.1), xytext=(3.65, 2.1), arrowprops=dict(arrowstyle="->", lw=1.8, color="#2A9D8F"))
ax.text(3.18, 1.7, "Real-Time Skeletal\nOverlay & Audio Cues", fontsize=8, color="#2A9D8F", ha="center")

# Arrows: Process -> Storage
ax.annotate("", xy=(7.3, 2.9), xytext=(6.35, 2.9), arrowprops=dict(arrowstyle="->", lw=1.8, color="#E76F51"))
ax.text(6.82, 3.1, "Session Stats &\nStreak Updates", fontsize=8, color="#E76F51", ha="center")

# Arrows: Storage -> Process
ax.annotate("", xy=(6.35, 2.1), xytext=(7.3, 2.1), arrowprops=dict(arrowstyle="->", lw=1.8, color="#1D3557"))
ax.text(6.82, 1.7, "Stored Poses &\nHistorical Trends", fontsize=8, color="#1D3557", ha="center")

plt.tight_layout()
dfd0_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\dfd_level_0.png'
plt.savefig(dfd0_path, dpi=300, bbox_inches='tight')
plt.close()
print("Saved DFD Level 0 at", dfd0_path)

# -------------------------------------------------------------
# DFD LEVEL 1 (DECOMPOSED DATA FLOW)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6.0), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Process 1.0: Optical Frame Acquisition
p1 = patches.FancyBboxPatch((0.5, 5.0), 2.5, 1.2, boxstyle="round,pad=0.1", ec="#1D3557", fc="#EBF2FA", lw=2)
ax.add_patch(p1)
ax.text(1.75, 5.6, "1.0 Frame Acquisition\n& WebGL Binding", fontsize=9, fontweight='bold', color="#1D3557", ha="center", va="center")

# Process 2.0: 3D Pose Inference
p2 = patches.FancyBboxPatch((4.0, 5.0), 2.5, 1.2, boxstyle="round,pad=0.1", ec="#2A9D8F", fc="#E8F8F5", lw=2)
ax.add_patch(p2)
ax.text(5.25, 5.6, "2.0 BlazePose 3D\nLandmark Extraction", fontsize=9, fontweight='bold', color="#2A9D8F", ha="center", va="center")

# Process 3.0: Biomechanical Kinematics
p3 = patches.FancyBboxPatch((7.0, 5.0), 2.5, 1.2, boxstyle="round,pad=0.1", ec="#457B9D", fc="#EDF6F9", lw=2)
ax.add_patch(p3)
ax.text(8.25, 5.6, "3.0 Vector Kinematics\n& EMA Filtering", fontsize=9, fontweight='bold', color="#457B9D", ha="center", va="center")

# Process 4.0: FSM State Machine
p4 = patches.FancyBboxPatch((7.0, 2.0), 2.5, 1.2, boxstyle="round,pad=0.1", ec="#E76F51", fc="#FDF2E9", lw=2)
ax.add_patch(p4)
ax.text(8.25, 2.6, "4.0 Routine FSM &\nHold Timer Tracking", fontsize=9, fontweight='bold', color="#E76F51", ha="center", va="center")

# Process 5.0: Audio Biofeedback Dispatch
p5 = patches.FancyBboxPatch((4.0, 2.0), 2.5, 1.2, boxstyle="round,pad=0.1", ec="#D62828", fc="#FCE8E6", lw=2)
ax.add_patch(p5)
ax.text(5.25, 2.6, "5.0 Audio Coaching\n& Debounced Dispatch", fontsize=9, fontweight='bold', color="#D62828", ha="center", va="center")

# Process 6.0: Offline Persistence
p6 = patches.FancyBboxPatch((0.5, 2.0), 2.5, 1.2, boxstyle="round,pad=0.1", ec="#6A4C93", fc="#F3EBF7", lw=2)
ax.add_patch(p6)
ax.text(1.75, 2.6, "6.0 AsyncStorage\nHistory & Analytics", fontsize=9, fontweight='bold', color="#6A4C93", ha="center", va="center")

# Connecting Data Flow Arrows
ax.annotate("", xy=(4.0, 5.6), xytext=(3.0, 5.6), arrowprops=dict(arrowstyle="->", lw=1.8, color="#1D3557"))
ax.text(3.5, 5.85, "RGB Tensors", fontsize=7.5, color="#1D3557", ha="center")

ax.annotate("", xy=(7.0, 5.6), xytext=(6.5, 5.6), arrowprops=dict(arrowstyle="->", lw=1.8, color="#2A9D8F"))
ax.text(6.75, 5.85, "33 3D Keypoints", fontsize=7.5, color="#2A9D8F", ha="center")

ax.annotate("", xy=(8.25, 3.2), xytext=(8.25, 5.0), arrowprops=dict(arrowstyle="->", lw=1.8, color="#457B9D"))
ax.text(8.95, 4.1, "Articular Joint\nAngles & Scores", fontsize=7.5, color="#457B9D", ha="center")

ax.annotate("", xy=(6.5, 2.6), xytext=(7.0, 2.6), arrowprops=dict(arrowstyle="->", lw=1.8, color="#E76F51"))
ax.text(6.75, 2.85, "Form Alerts", fontsize=7.5, color="#E76F51", ha="center")

ax.annotate("", xy=(3.0, 2.6), xytext=(4.0, 2.6), arrowprops=dict(arrowstyle="->", lw=1.8, color="#D62828"))
ax.text(3.5, 2.85, "Session Summary", fontsize=7.5, color="#D62828", ha="center")

plt.tight_layout()
dfd1_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\dfd_level_1.png'
plt.savefig(dfd1_path, dpi=300, bbox_inches='tight')
plt.close()
print("Saved DFD Level 1 at", dfd1_path)
