import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8.5, 9.0), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 11)
ax.axis('off')

# Start Node
start_node = patches.Circle((5.0, 10.3), 0.25, facecolor="#1D3557", edgecolor="#1D3557")
ax.add_patch(start_node)
ax.text(5.0, 10.65, "Start Session", fontsize=8.5, fontweight='bold', ha='center')

# Action 1: Select Pose or Routine
act1 = patches.FancyBboxPatch((3.2, 9.2), 3.6, 0.7, boxstyle="round,pad=0.08", ec="#1D3557", fc="#EBF2FA", lw=1.5)
ax.add_patch(act1)
ax.text(5.0, 9.55, "User Selects Pose / Flow from Library", fontsize=8.5, ha='center', va='center')

# Action 2: Initialize WebGL TensorCamera
act2 = patches.FancyBboxPatch((3.0, 8.1), 4.0, 0.7, boxstyle="round,pad=0.08", ec="#2A9D8F", fc="#E8F8F5", lw=1.5)
ax.add_patch(act2)
ax.text(5.0, 8.45, "Mount Camera & Bind WebGL GLContext", fontsize=8.5, ha='center', va='center')

# Decision 1: Calibration Framing Check
d1 = patches.Polygon([[5.0, 7.6], [6.5, 7.0], [5.0, 6.4], [3.5, 7.0]], closed=True, ec="#E76F51", fc="#FDF2E9", lw=1.5)
ax.add_patch(d1)
ax.text(5.0, 7.0, "Is Full Body\nIn Frame?", fontsize=8, fontweight='bold', ha='center', va='center')

# Action 3: Prompt step back
act_back = patches.FancyBboxPatch((0.5, 6.65), 2.4, 0.7, boxstyle="round,pad=0.08", ec="#E76F51", fc="#FDF2E9", lw=1.5)
ax.add_patch(act_back)
ax.text(1.7, 7.0, "Voice: 'Step back into mat'", fontsize=8, ha='center', va='center')

# Action 4: Calibration countdown
act3 = patches.FancyBboxPatch((3.2, 5.3), 3.6, 0.7, boxstyle="round,pad=0.08", ec="#2A9D8F", fc="#E8F8F5", lw=1.5)
ax.add_patch(act3)
ax.text(5.0, 5.65, "Play 3-2-1 Audio Countdown", fontsize=8.5, ha='center', va='center')

# Action 5: Extract 33 Keypoints & Compute EMA Angles
act4 = patches.FancyBboxPatch((2.8, 4.2), 4.4, 0.7, boxstyle="round,pad=0.08", ec="#457B9D", fc="#EDF6F9", lw=1.5)
ax.add_patch(act4)
ax.text(5.0, 4.55, "Extract 33 3D Joints & Compute Clamped Angles", fontsize=8.5, ha='center', va='center')

# Decision 2: Posture Accuracy Evaluation
d2 = patches.Polygon([[5.0, 3.7], [6.6, 3.1], [5.0, 2.5], [3.4, 3.1]], closed=True, ec="#2A9D8F", fc="#E8F8F5", lw=1.5)
ax.add_patch(d2)
ax.text(5.0, 3.1, "Angle within\nTolerance?", fontsize=8, fontweight='bold', ha='center', va='center')

# Branch: No -> Audio Correction Cue
act_cue = patches.FancyBboxPatch((0.5, 2.75), 2.4, 0.7, boxstyle="round,pad=0.08", ec="#D62828", fc="#FCE8E6", lw=1.5)
ax.add_patch(act_cue)
ax.text(1.7, 3.1, "Audio Cue: 'Adjust joint'\n(Throttled 4s)", fontsize=7.5, ha='center', va='center')

# Branch: Yes -> Increment Hold Timer
act_hold = patches.FancyBboxPatch((7.2, 2.75), 2.5, 0.7, boxstyle="round,pad=0.08", ec="#2A9D8F", fc="#E8F8F5", lw=1.5)
ax.add_patch(act_hold)
ax.text(8.45, 3.1, "Timer++ & Green Skeletal Mesh", fontsize=7.5, ha='center', va='center')

# Action 6: Complete Pose & Persist Analytics
act5 = patches.FancyBboxPatch((3.0, 1.4), 4.0, 0.7, boxstyle="round,pad=0.08", ec="#6A4C93", fc="#F3EBF7", lw=1.5)
ax.add_patch(act5)
ax.text(5.0, 1.75, "Save Stats & Update Daily Streak in Storage", fontsize=8.5, ha='center', va='center')

# End Node
end_outer = patches.Circle((5.0, 0.45), 0.28, facecolor="none", edgecolor="#1D3557", lw=2)
end_inner = patches.Circle((5.0, 0.45), 0.18, facecolor="#1D3557", edgecolor="#1D3557")
ax.add_patch(end_outer)
ax.add_patch(end_inner)
ax.text(5.0, 0.05, "Session Concluded", fontsize=8.5, fontweight='bold', ha='center')

# Connective Flow Arrows
ax.annotate("", xy=(5.0, 9.9), xytext=(5.0, 10.05), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(5.0, 8.8), xytext=(5.0, 9.2), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(5.0, 7.6), xytext=(5.0, 8.1), arrowprops=dict(arrowstyle="->", lw=1.5))

# Calibration Decision Arrows
ax.annotate("", xy=(2.9, 7.0), xytext=(3.5, 7.0), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(3.1, 7.15, "No", fontsize=8, fontweight='bold', color="#E76F51")
ax.annotate("", xy=(5.0, 8.8), xytext=(1.7, 7.35), arrowprops=dict(arrowstyle="->", lw=1.2, connectionstyle="arc3,rad=-0.4"))

ax.annotate("", xy=(5.0, 6.0), xytext=(5.0, 6.4), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(5.2, 6.2, "Yes", fontsize=8, fontweight='bold', color="#2A9D8F")
ax.annotate("", xy=(5.0, 4.9), xytext=(5.0, 5.3), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(5.0, 3.7), xytext=(5.0, 4.2), arrowprops=dict(arrowstyle="->", lw=1.5))

# Accuracy Decision Arrows
ax.annotate("", xy=(2.9, 3.1), xytext=(3.4, 3.1), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(3.05, 3.25, "No", fontsize=8, fontweight='bold', color="#D62828")
ax.annotate("", xy=(5.0, 4.9), xytext=(1.7, 3.45), arrowprops=dict(arrowstyle="->", lw=1.2, connectionstyle="arc3,rad=-0.4"))

ax.annotate("", xy=(7.2, 3.1), xytext=(6.6, 3.1), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(6.85, 3.25, "Yes", fontsize=8, fontweight='bold', color="#2A9D8F")
ax.annotate("", xy=(5.0, 2.1), xytext=(8.45, 2.75), arrowprops=dict(arrowstyle="->", lw=1.2, connectionstyle="arc3,rad=-0.3"))

ax.annotate("", xy=(5.0, 0.75), xytext=(5.0, 1.4), arrowprops=dict(arrowstyle="->", lw=1.5))

plt.tight_layout()
act_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\activity_diagram.png'
plt.savefig(act_path, dpi=300, bbox_inches='tight')
plt.close()
print("Saved Activity Diagram at", act_path)
