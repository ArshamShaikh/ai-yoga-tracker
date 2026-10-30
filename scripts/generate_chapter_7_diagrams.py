import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.5)
ax.axis('off')

# Title
ax.text(5.0, 6.1, "Software Quality Assurance V-Model for AI-Based Yoga Trainer", 
        fontsize=12, fontweight='bold', ha='center', color='#111111')

# Left side of V: Development Lifecycle
left_boxes = [
    (0.8, 4.8, 2.5, 0.9, "Requirements Analysis\n(FRs, NFRs, Biomechanics)"),
    (1.8, 3.5, 2.5, 0.9, "System Architecture\n(Layered 3-Tier Edge)"),
    (2.8, 2.2, 2.5, 0.9, "Mathematical Design\n(Vector Angles & EMA)"),
    (3.8, 0.9, 2.4, 0.9, "Implementation\n(React Native & TFJS)")
]

for x, y, w, h, txt in left_boxes:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", ec="#111111", fc="#F8F9FA", lw=1.5)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, fontsize=8.5, ha='center', va='center', fontweight='bold', color='#111111')

# Right side of V: Verification & Testing
right_boxes = [
    (6.7, 4.8, 2.5, 0.9, "User Acceptance Testing\n(Real Yogi Evaluation)"),
    (5.7, 3.5, 2.5, 0.9, "System & Stress Testing\n(75 Poses, 6 Flows, Heat)"),
    (4.7, 2.2, 2.5, 0.9, "Integration Testing\n(FSM & Audio Queue)"),
    (3.8, 0.9, 2.4, 0.9, "Implementation\n(Shared Vertex)") # Vertex
]

for x, y, w, h, txt in right_boxes[:-1]:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", ec="#111111", fc="#E9ECEF", lw=1.5)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, fontsize=8.5, ha='center', va='center', fontweight='bold', color='#111111')

# Downward arrows on left
ax.annotate('', xy=(2.3, 4.4), xytext=(2.0, 4.8), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))
ax.annotate('', xy=(3.3, 3.1), xytext=(3.0, 3.5), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))
ax.annotate('', xy=(4.3, 1.8), xytext=(4.0, 2.2), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))

# Upward arrows on right
ax.annotate('', xy=(5.7, 2.2), xytext=(5.3, 1.8), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))
ax.annotate('', xy=(6.7, 3.5), xytext=(6.3, 3.1), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))
ax.annotate('', xy=(7.7, 4.8), xytext=(7.3, 4.4), arrowprops=dict(facecolor='#111111', arrowstyle='->', lw=1.5))

# Horizontal verification dashed lines
ax.annotate('', xy=(6.7, 5.25), xytext=(3.3, 5.25), arrowprops=dict(facecolor='#555555', edgecolor='#555555', arrowstyle='<->', ls='--', lw=1.2))
ax.text(5.0, 5.4, "Validates Requirements", fontsize=8, ha='center', color='#444444')

ax.annotate('', xy=(5.7, 3.95), xytext=(4.3, 3.95), arrowprops=dict(facecolor='#555555', edgecolor='#555555', arrowstyle='<->', ls='--', lw=1.2))
ax.text(5.0, 4.1, "Verifies Architecture", fontsize=8, ha='center', color='#444444')

ax.annotate('', xy=(4.7, 2.65), xytext=(5.3, 2.65), arrowprops=dict(facecolor='#555555', edgecolor='#555555', arrowstyle='<->', ls='--', lw=1.2))
ax.text(5.0, 2.8, "Verifies Math & FSM", fontsize=8, ha='center', color='#444444')

plt.tight_layout()
out_v = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\testing_v_model.png'
plt.savefig(out_v, dpi=300, bbox_inches='tight')
plt.close()
print('Testing V-Model diagram saved at', out_v)
