import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 7.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.5)
ax.axis('off')

# Title
ax.text(5.0, 7.1, "AI-Based Yoga Trainer: Module & Component Interaction Architecture", 
        fontsize=12, fontweight='bold', ha='center', color='#111111')

# UI Module: session.js
b_session = patches.FancyBboxPatch((3.5, 5.4), 3.0, 1.2, boxstyle="round,pad=0.08", ec="#111111", fc="#FFFFFF", lw=2)
ax.add_patch(b_session)
ax.text(5.0, 6.0, "SessionStudio (session.js)\nMain Coordinator & HUD", fontsize=10, fontweight='bold', ha='center', va='center')

# Left Branch: Camera & Pose Detection
b_camera = patches.FancyBboxPatch((0.6, 3.6), 2.5, 1.1, boxstyle="round,pad=0.08", ec="#111111", fc="#F8F9FA", lw=1.5)
ax.add_patch(b_camera)
ax.text(1.85, 4.15, "YogaCamera.js\nTensorCamera WebGL Bridge", fontsize=9, fontweight='bold', ha='center', va='center')

b_detector = patches.FancyBboxPatch((0.6, 1.8), 2.5, 1.1, boxstyle="round,pad=0.08", ec="#111111", fc="#F8F9FA", lw=1.5)
ax.add_patch(b_detector)
ax.text(1.85, 2.35, "PoseDetector.js\nMediaPipe BlazePose 3D", fontsize=9, fontweight='bold', ha='center', va='center')

# Center Branch: Math & Overlay
b_math = patches.FancyBboxPatch((3.7, 3.6), 2.6, 1.1, boxstyle="round,pad=0.08", ec="#111111", fc="#F8F9FA", lw=1.5)
ax.add_patch(b_math)
ax.text(5.0, 4.15, "poseMathUtils.js\n3D Vector Math & EMA Filter", fontsize=9, fontweight='bold', ha='center', va='center')

b_overlay = patches.FancyBboxPatch((3.7, 1.8), 2.6, 1.1, boxstyle="round,pad=0.08", ec="#111111", fc="#F8F9FA", lw=1.5)
ax.add_patch(b_overlay)
ax.text(5.0, 2.35, "PoseOverlay.js\nSVG Skeleton & Joint Colors", fontsize=9, fontweight='bold', ha='center', va='center')

# Right Branch: Routine, Audio, Storage
b_routine = patches.FancyBboxPatch((6.9, 3.6), 2.6, 1.1, boxstyle="round,pad=0.08", ec="#111111", fc="#F8F9FA", lw=1.5)
ax.add_patch(b_routine)
ax.text(8.2, 4.15, "RoutineEngine.js\nFinite State Machine", fontsize=9, fontweight='bold', ha='center', va='center')

b_audio = patches.FancyBboxPatch((6.9, 1.8), 2.6, 1.1, boxstyle="round,pad=0.08", ec="#111111", fc="#F8F9FA", lw=1.5)
ax.add_patch(b_audio)
ax.text(8.2, 2.35, "FeedbackEngine.js\nTTS Audio Coaching & Queue", fontsize=9, fontweight='bold', ha='center', va='center')

# Bottom Center: Storage Service
b_store = patches.FancyBboxPatch((3.7, 0.4), 2.6, 0.9, boxstyle="round,pad=0.08", ec="#111111", fc="#E9ECEF", lw=1.5)
ax.add_patch(b_store)
ax.text(5.0, 0.85, "StorageService.js\nAsyncStorage Offline DB", fontsize=9, fontweight='bold', ha='center', va='center')

# Arrows
# session -> camera
ax.annotate('', xy=(2.0, 4.7), xytext=(3.7, 5.4), arrowprops=dict(facecolor='#111111', arrowstyle='<->', lw=1.5))
# camera -> detector
ax.annotate('', xy=(1.85, 2.9), xytext=(1.85, 3.6), arrowprops=dict(facecolor='#111111', arrowstyle='<->', lw=1.5))
# detector -> session (landmarks)
ax.annotate('', xy=(3.5, 5.7), xytext=(2.5, 2.9), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5, ls='--'))
# session -> math
ax.annotate('', xy=(5.0, 4.7), xytext=(5.0, 5.4), arrowprops=dict(facecolor='#111111', arrowstyle='<->', lw=1.5))
# session -> overlay
ax.annotate('', xy=(4.4, 2.9), xytext=(4.4, 5.4), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))
# session -> routine
ax.annotate('', xy=(7.6, 4.7), xytext=(6.2, 5.4), arrowprops=dict(facecolor='#111111', arrowstyle='<->', lw=1.5))
# routine -> audio
ax.annotate('', xy=(8.2, 2.9), xytext=(8.2, 3.6), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))
# routine -> storage
ax.annotate('', xy=(6.0, 1.3), xytext=(7.4, 3.6), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))
# session -> storage
ax.annotate('', xy=(5.0, 1.3), xytext=(5.0, 1.8), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))

plt.tight_layout()
out_mod = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\module_interaction_diagram.png'
plt.savefig(out_mod, dpi=300, bbox_inches='tight')
plt.close()
print('Module interaction diagram saved at', out_mod)
