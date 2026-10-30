import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up figure
fig, ax = plt.subplots(figsize=(10, 7.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.5)
ax.axis('off')

# System Boundary Rectangle
system_box = patches.FancyBboxPatch((2.2, 0.4), 5.6, 6.7,
                                    boxstyle="round,pad=0.1",
                                    ec="#111111", fc="#F8F9FA", lw=2)
ax.add_patch(system_box)

# System Title
ax.text(5.0, 6.8, "AI-Based Yoga Trainer System Boundary", 
        fontsize=13, fontweight='bold', ha='center', va='center', color='#111111')

# Actor 1: Yoga Practitioner (Left)
ax.plot([1.0, 1.0], [4.4, 3.8], color='#111111', lw=2) # body
circle = patches.Circle((1.0, 4.7), 0.25, ec='#111111', fc='#E9ECEF', lw=2) # head
ax.add_patch(circle)
ax.plot([0.5, 1.5], [4.2, 4.2], color='#111111', lw=2) # arms
ax.plot([1.0, 0.6], [3.8, 3.1], color='#111111', lw=2) # left leg
ax.plot([1.0, 1.4], [3.8, 3.1], color='#111111', lw=2) # right leg
ax.text(1.0, 2.7, "Yoga Practitioner\n(Primary User)", fontsize=11, fontweight='bold', ha='center', va='top')

# Actor 2: Edge AI & Audio Engine (Right Top)
box_ai = patches.FancyBboxPatch((8.1, 4.4), 1.6, 1.4, boxstyle="round,pad=0.08", ec="#111111", fc="#E9ECEF", lw=1.5)
ax.add_patch(box_ai)
ax.text(8.9, 5.1, "<<System Actor>>\nEdge AI & Audio\nCoaching Engine", fontsize=9.5, fontweight='bold', ha='center', va='center')

# Actor 3: Local Storage Service (Right Bottom)
box_db = patches.FancyBboxPatch((8.1, 1.4), 1.6, 1.2, boxstyle="round,pad=0.08", ec="#111111", fc="#E9ECEF", lw=1.5)
ax.add_patch(box_db)
ax.text(8.9, 2.0, "<<Secondary Actor>>\nOffline Storage &\nAnalytics Service", fontsize=9.5, fontweight='bold', ha='center', va='center')

# Use Cases (Ovals)
use_cases = [
    (5.0, 6.1, "UC-01: Select Pose / Curated Flow Routine", 0.32),
    (5.0, 5.2, "UC-02: Calibrate Pre-Session Body Framing", 0.32),
    (5.0, 4.3, "UC-03: Execute Real-Time 3D BlazePose Tracking", 0.32),
    (5.0, 3.4, "UC-04: Evaluate 3D Joint Angles & Tolerances", 0.32),
    (5.0, 2.5, "UC-05: Receive Low-Latency Audio Coaching", 0.32),
    (5.0, 1.6, "UC-06: Track Hold Timers & Auto-Transition", 0.32),
    (5.0, 0.8, "UC-07: Persist Session Stats & Streaks", 0.28)
]

for x, y, text, height in use_cases:
    ellipse = patches.Ellipse((x, y), 4.2, height*2.2, ec='#212529', fc='#FFFFFF', lw=1.5)
    ax.add_patch(ellipse)
    ax.text(x, y, text, fontsize=9.5, fontweight='bold', ha='center', va='center', color='#111111')

# Association Lines from Practitioner
for _, y, _, _ in use_cases:
    ax.plot([1.45, 2.9], [4.1, y], color='#333333', lw=1.2, linestyle='-')

# Association Lines to Edge AI
ax.plot([7.1, 8.1], [4.3, 5.1], color='#333333', lw=1.2, linestyle='-') # UC-03 to AI
ax.plot([7.1, 8.1], [3.4, 5.1], color='#333333', lw=1.2, linestyle='-') # UC-04 to AI
ax.plot([7.1, 8.1], [2.5, 5.1], color='#333333', lw=1.2, linestyle='-') # UC-05 to Audio

# Association Lines to Local Storage
ax.plot([7.1, 8.1], [1.6, 2.0], color='#333333', lw=1.2, linestyle='-') # UC-06 to DB
ax.plot([7.1, 8.1], [0.8, 2.0], color='#333333', lw=1.2, linestyle='-') # UC-07 to DB

plt.tight_layout()
output_img = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\use_case_diagram.png'
plt.savefig(output_img, dpi=300, bbox_inches='tight')
plt.close()
print('Use case diagram successfully generated at', output_img)
