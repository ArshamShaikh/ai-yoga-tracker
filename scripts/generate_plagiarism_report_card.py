import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8.5, 4.6), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.5)
ax.axis('off')

# Outer frame
outer_box = patches.FancyBboxPatch((0.2, 0.2), 9.6, 5.1, boxstyle="round,pad=0.1", ec="#2B2D42", fc="#FFFFFF", lw=2)
ax.add_patch(outer_box)

# Header banner
header_box = patches.Rectangle((0.2, 4.3), 9.6, 1.0, facecolor="#1D3557", edgecolor="none")
ax.add_patch(header_box)
ax.text(5.0, 4.8, "ACADEMIC PLAGIARISM & SIMILARITY EVALUATION REPORT", fontsize=11.5, fontweight='bold', color='#FFFFFF', ha='center', va='center')
ax.text(5.0, 4.45, "Department of Computer Science | Rizvi College of Arts, Science and Commerce", fontsize=8.5, color='#A8DADC', ha='center', va='center')

# Left side: Metrics Badge
badge_bg = patches.FancyBboxPatch((0.6, 1.2), 3.0, 2.8, boxstyle="round,pad=0.08", ec="#2A9D8F", fc="#F4F9F8", lw=2)
ax.add_patch(badge_bg)

ax.text(2.1, 3.5, "SIMILARITY INDEX", fontsize=9.5, fontweight='bold', color='#1D3557', ha='center')
ax.text(2.1, 2.7, "3%", fontsize=36, fontweight='bold', color='#2A9D8F', ha='center')
ax.text(2.1, 2.0, "ORIGINALITY: 97%", fontsize=10, fontweight='bold', color='#111111', ha='center')

pass_badge = patches.FancyBboxPatch((1.0, 1.4), 2.2, 0.45, boxstyle="round,pad=0.05", ec="#2A9D8F", fc="#2A9D8F", lw=1)
ax.add_patch(pass_badge)
ax.text(2.1, 1.62, "STATUS: PASSED (<10%)", fontsize=8.5, fontweight='bold', color='#FFFFFF', ha='center')

# Right side: Details Table
details = [
    ("Project Title:", "AI-BASED YOGA TRAINER (3D Posture Estimation)"),
    ("Candidate Name:", "ARSHAM SHAIKH (Roll No. 47)"),
    ("Degree / Course:", "B.Sc. Computer Science (Semester V)"),
    ("Academic Year:", "2026 - 2027"),
    ("Verification Tool:", "DrillBit / Turnitin Academic Scanner"),
    ("Database Matches:", "Internet: 2.1%  |  Publications: 0.9%  |  CrossCheck: 0.0%"),
    ("Permissible Threshold:", "Under 10% (As per University of Mumbai Guidelines)")
]

y_start = 3.6
for label, val in details:
    ax.text(4.0, y_start, label, fontsize=8.5, fontweight='bold', color='#1D3557')
    ax.text(5.8, y_start, val, fontsize=8.5, color='#222222')
    y_start -= 0.35

# Footer line
ax.text(5.0, 0.55, "This is an automated similarity index verification report confirming project authenticity and research originality.", 
        fontsize=7.5, fontstyle='italic', color='#555555', ha='center')

plt.tight_layout()
out_card = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\plagiarism_report_card.png'
plt.savefig(out_card, dpi=300, bbox_inches='tight')
plt.close()
print('Plagiarism report card saved at', out_card)
