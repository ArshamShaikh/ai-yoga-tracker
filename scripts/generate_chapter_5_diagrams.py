import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------------------------------------
# DIAGRAM 1: 3D VECTOR ANGLE GEOMETRIC MODEL (Figure 5.1)
# -------------------------------------------------------------
fig = plt.figure(figsize=(9, 7), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Coordinates for Joint B (Vertex, e.g., Knee), Joint A (Hip), Joint C (Ankle)
B = np.array([0.0, 0.0, 0.0]) # Vertex
A = np.array([1.5, 3.0, 1.2]) # Proximal Joint (Hip)
C = np.array([2.8, -1.2, 2.0]) # Distal Joint (Ankle)

# Plot Joint Nodes
ax.scatter([A[0]], [A[1]], [A[2]], color='#111111', s=120, zorder=5)
ax.scatter([B[0]], [B[1]], [B[2]], color='#E63946', s=160, zorder=5)
ax.scatter([C[0]], [C[1]], [C[2]], color='#111111', s=120, zorder=5)

# Label Nodes
ax.text(A[0]+0.1, A[1]+0.2, A[2]+0.2, "Joint A (Hip)\nP_A = (x_A, y_A, z_A)", fontsize=9.5, fontweight='bold')
ax.text(B[0]-0.3, B[1]-0.5, B[2]-0.3, "Vertex Joint B (Knee)\nP_B = (x_B, y_B, z_B)", fontsize=10, fontweight='bold', color='#E63946')
ax.text(C[0]+0.1, C[1]-0.3, C[2]+0.1, "Joint C (Ankle)\nP_C = (x_C, y_C, z_C)", fontsize=9.5, fontweight='bold')

# Plot Limb Vectors u and v
ax.quiver(B[0], B[1], B[2], A[0]-B[0], A[1]-B[1], A[2]-B[2], color='#1D3557', lw=2.8, arrow_length_ratio=0.1)
ax.quiver(B[0], B[1], B[2], C[0]-B[0], C[1]-B[1], C[2]-B[2], color='#1D3557', lw=2.8, arrow_length_ratio=0.1)

# Annotate Vector names
ax.text((A[0]+B[0])/2 - 0.4, (A[1]+B[1])/2 + 0.2, (A[2]+B[2])/2, r"$\vec{u} = \vec{BA} = A - B$", fontsize=10.5, fontweight='bold', color='#1D3557')
ax.text((C[0]+B[0])/2 + 0.2, (C[1]+B[1])/2 - 0.4, (C[2]+B[2])/2, r"$\vec{v} = \vec{BC} = C - B$", fontsize=10.5, fontweight='bold', color='#1D3557')

# Draw Angle Arc theta
t = np.linspace(0, 1, 30)
u_norm = A / np.linalg.norm(A)
v_norm = C / np.linalg.norm(C)
arc = 0.8 * (np.outer(1 - t, u_norm) + np.outer(t, v_norm))
arc_norm = arc / np.linalg.norm(arc, axis=1)[:, None] * 0.9
ax.plot(arc_norm[:, 0], arc_norm[:, 1], arc_norm[:, 2], color='#E63946', lw=2.5, ls='--')
ax.text(0.5, 0.4, 0.7, r"Interior Angle $\theta$", fontsize=11, fontweight='bold', color='#E63946')

# Coordinate Axes indicators
ax.set_xlabel('X (Lateral / Horizontal)', fontsize=8.5, labelpad=8)
ax.set_ylabel('Y (Vertical Height)', fontsize=8.5, labelpad=8)
ax.set_zlabel('Z (Depth from Hips)', fontsize=8.5, labelpad=8)
ax.set_title("3D Euclidean Vector Kinematics at Articular Joint B", fontsize=11.5, fontweight='bold', pad=12)

plt.tight_layout()
out_vec = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\vector_angle_geometry.png'
plt.savefig(out_vec, dpi=300, bbox_inches='tight')
plt.close()
print('Vector geometry diagram saved at', out_vec)

# -------------------------------------------------------------
# DIAGRAM 2: EMA FILTER NOISE SMOOTHING (Figure 5.2)
# -------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(9, 4.5), dpi=300)

np.random.seed(42)
frames = np.arange(0, 60)
true_angle = np.piecewise(frames, [frames < 20, (frames >= 20) & (frames < 40), frames >= 40], [175, lambda f: 175 - (f - 20) * 4.25, 90])
noise = np.random.normal(0, 3.8, size=len(frames))
raw_signal = true_angle + noise

# Compute EMA with alpha = 0.40
alpha = 0.40
ema_signal = np.zeros_like(raw_signal)
ema_signal[0] = raw_signal[0]
for i in range(1, len(raw_signal)):
    ema_signal[i] = alpha * raw_signal[i] + (1 - alpha) * ema_signal[i - 1]

ax2.plot(frames, raw_signal, color='#ADB5BD', lw=1.5, ls=':', label='Raw Sensor Signal (Optical Jitter & Noise)', alpha=0.9)
ax2.plot(frames, ema_signal, color='#1D3557', lw=2.5, label=r'EMA Filtered Signal ($\alpha = 0.40$, Sub-35ms Stabilization)')
ax2.plot(frames, true_angle, color='#2A9D8F', lw=2.0, ls='--', label='Ideal Ground-Truth Kinematic Trajectory')

# Threshold Tolerance Band for Target Warrior II Knee (90 deg +/- 15 deg)
ax2.axhspan(75, 105, color='#E9ECEF', alpha=0.5, label=r'Calibrated Target Tolerance Band ($90^\circ \pm 15^\circ$)')

ax2.set_xlabel('Video Frame Index (30 FPS Stream)', fontsize=10, fontweight='bold')
ax2.set_ylabel('Articular Joint Angle (Degrees)', fontsize=10, fontweight='bold')
ax2.set_title(r'Anti-Jitter Temporal Signal Filtering: Raw Sensor vs. EMA Smoothing ($\alpha=0.40$)', fontsize=11, fontweight='bold')
ax2.legend(loc='upper right', frameon=True, facecolor='#FFFFFF', framealpha=0.9, fontsize=8.5)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
out_ema = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\ema_signal_smoothing.png'
plt.savefig(out_ema, dpi=300, bbox_inches='tight')
plt.close()
print('EMA signal smoothing diagram saved at', out_ema)
