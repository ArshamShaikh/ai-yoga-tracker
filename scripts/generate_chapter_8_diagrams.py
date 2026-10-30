import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------
# DIAGRAM 1: END-TO-END PIPELINE LATENCY BREAKDOWN (Figure 8.1)
# -------------------------------------------------------------
stages = [
    'Camera Frame\nAcquisition',
    'WebGL Tensor\nBinding',
    'MediaPipe 3D\nInference',
    'Vector Angle\nMath & EMA',
    'State & Audio\nDispatch'
]
latencies = [6.2, 3.1, 18.4, 0.6, 1.2]
colors = ['#457B9D', '#A8DADC', '#1D3557', '#E63946', '#2A9D8F']

fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=300)
bars = ax.bar(stages, latencies, color=colors, width=0.55, edgecolor='#111111', lw=1.2)

# Annotate values on top of bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.4, f"{yval:.1f} ms", ha='center', va='bottom', fontsize=9.5, fontweight='bold')

# Horizontal line for 30 FPS deadline (33.3 ms)
total_lat = sum(latencies)
ax.axhline(33.3, color='#E63946', linestyle='--', linewidth=1.5, label='30 FPS Budget Limit (33.3 ms)')
ax.text(2.5, 34.0, '30 FPS Frame Deadline (33.3 ms)', color='#E63946', fontweight='bold', fontsize=9)

ax.set_ylim(0, 38)
ax.set_ylabel('Execution Time per Frame (Milliseconds)', fontsize=10, fontweight='bold')
ax.set_title(f'End-to-End Pipeline Latency Breakdown (Total Frame Latency: {total_lat:.1f} ms / ~34 FPS)', fontsize=11, fontweight='bold', pad=12)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper right', frameon=True)

plt.tight_layout()
out_lat = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\latency_breakdown_chart.png'
plt.savefig(out_lat, dpi=300, bbox_inches='tight')
plt.close()
print('Latency breakdown chart saved at', out_lat)

# -------------------------------------------------------------
# DIAGRAM 2: ANGULAR ACCURACY & MAE BY JOINT (Figure 8.2)
# -------------------------------------------------------------
joints = ['Knee Flexion\n(Warrior II)', 'Hip Abduction\n(Triangle)', 'Shoulder Flexion\n(Down Dog)', 'Spine Extension\n(Cobra)', 'Elbow Flexion\n(Plank)']
mae = [2.14, 2.82, 3.18, 3.45, 2.38] # Mean Absolute Error in degrees
std = [0.42, 0.55, 0.62, 0.71, 0.48]

fig2, ax2 = plt.subplots(figsize=(8.5, 4.5), dpi=300)
x_pos = np.arange(len(joints))
bars2 = ax2.bar(x_pos, mae, yerr=std, capsize=5, color='#2A9D8F', width=0.52, edgecolor='#111111', lw=1.2)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.9, f"MAE: {yval:.2f}°", ha='center', va='bottom', fontsize=9, fontweight='bold')

ax2.axhline(5.0, color='#E63946', linestyle=':', linewidth=1.5, label='Clinical Acceptability Threshold (< 5.0°)')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(joints, fontsize=9, fontweight='bold')
ax2.set_ylim(0, 6.0)
ax2.set_ylabel('Mean Absolute Error vs. Goniometer (Degrees)', fontsize=10, fontweight='bold')
ax2.set_title('Biomechanical Articular Angle Precision: Experimental Error vs. Clinical Baseline', fontsize=11, fontweight='bold', pad=12)
ax2.grid(axis='y', linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', frameon=True)

plt.tight_layout()
out_acc = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\angular_accuracy_chart.png'
plt.savefig(out_acc, dpi=300, bbox_inches='tight')
plt.close()
print('Angular accuracy chart saved at', out_acc)
