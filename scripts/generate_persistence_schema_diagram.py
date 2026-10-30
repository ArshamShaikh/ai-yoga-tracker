import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(9.2, 5.8), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.5)
ax.axis('off')

# Title banner
title_box = patches.FancyBboxPatch((0.5, 5.8), 9.0, 0.55, boxstyle="round,pad=0.05", ec="#1B4D3E", fc="#E8F5E9", lw=1.5)
ax.add_patch(title_box)
ax.text(5.0, 6.07, "Entity-Relationship & Offline Data Persistence Schema (AsyncStorage)", 
        fontsize=11, fontweight='bold', color="#1B4D3E", ha="center", va="center")

def draw_entity(x, y, w, h, name, fields, color="#1D3557", bg="#F4F8FA"):
    # Header
    hdr = patches.Rectangle((x, y + h - 0.42), w, 0.42, facecolor=color, edgecolor=color)
    ax.add_patch(hdr)
    ax.text(x + w/2, y + h - 0.21, name, fontsize=8.5, fontweight='bold', color="#FFFFFF", ha="center", va="center")
    # Body
    body = patches.Rectangle((x, y), w, h - 0.42, facecolor=bg, edgecolor=color, lw=1.2)
    ax.add_patch(body)
    cur_y = y + h - 0.62
    for f in fields:
        is_pk = f.startswith("PK:")
        is_fk = f.startswith("FK:")
        weight = 'bold' if (is_pk or is_fk) else 'normal'
        t_col = "#B22222" if is_pk else ("#1D3557" if is_fk else "#333333")
        ax.text(x + 0.1, cur_y, f, fontsize=7.2, fontweight=weight, color=t_col, va="center")
        cur_y -= 0.24

# Entities
draw_entity(0.5, 3.2, 2.7, 2.2, "USER_PROFILE", [
    "PK: userId (string)",
    "userName (string)",
    "experienceLevel (string)",
    "audioCoachEnabled (bool)",
    "targetDailyMins (int)",
    "createdAt (timestamp)"
], color="#1B4D3E", bg="#F0F7F4")

draw_entity(3.7, 3.2, 2.7, 2.2, "WORKOUT_HISTORY", [
    "PK: sessionId (string)",
    "FK: userId (string)",
    "routineId (string)",
    "timestamp (ISO string)",
    "durationSecs (int)",
    "accuracyScore (int)",
    "posesCount (int)"
], color="#2A6F97", bg="#EBF2FA")

draw_entity(6.9, 3.2, 2.6, 2.2, "STREAK_METRICS", [
    "FK: userId (string)",
    "currentStreakDays (int)",
    "longestStreakDays (int)",
    "lastCompletedDate (string)",
    "weeklyDaysArray (list)",
    "updatedAt (timestamp)"
], color="#E76F51", bg="#FDF2E9")

draw_entity(1.8, 0.5, 2.8, 2.1, "ROUTINE_PRESETS", [
    "PK: routineId (string)",
    "title (string)",
    "subtitle (string)",
    "difficulty (string)",
    "durationMinutes (int)",
    "poses [ { poseId, holdSec } ]"
], color="#6A4C93", bg="#F6F2FA")

draw_entity(5.5, 0.5, 2.8, 2.1, "POSE_MASTERY_MAP", [
    "PK: poseId (string)",
    "FK: userId (string)",
    "totalPracticed (int)",
    "bestHoldSecs (int)",
    "isMastered (bool)",
    "lastAccuracy (int)",
    "lastPracticed (string)"
], color="#386641", bg="#F1F7F2")

# Relationships / Connector arrows
# User -> Workout History (1:N)
ax.annotate("", xy=(3.7, 4.3), xytext=(3.2, 4.3), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1B4D3E"))
ax.text(3.45, 4.45, "1 : N", fontsize=7.5, fontweight='bold', color="#1B4D3E", ha="center")

# User -> Streak Metrics (1:1)
ax.annotate("", xy=(6.9, 4.3), xytext=(6.4, 4.3), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1B4D3E"))
ax.text(6.65, 4.45, "1 : 1", fontsize=7.5, fontweight='bold', color="#1B4D3E", ha="center")

# Routine Presets -> Workout History (1:N)
ax.annotate("", xy=(4.6, 3.2), xytext=(3.6, 2.6), arrowprops=dict(arrowstyle="->", lw=1.3, color="#6A4C93"))
ax.text(4.25, 2.8, "references", fontsize=7, color="#6A4C93", rotation=30)

# Pose Mastery -> Workout History (1:N)
ax.annotate("", xy=(5.5, 3.2), xytext=(6.2, 2.6), arrowprops=dict(arrowstyle="->", lw=1.3, color="#386641"))
ax.text(6.0, 2.8, "tracks", fontsize=7, color="#386641", rotation=-30)

plt.tight_layout()
out_schema = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\persistence_schema_diagram.png'
plt.savefig(out_schema, dpi=300, bbox_inches='tight')
plt.close()
print("Saved persistence schema diagram at", out_schema)
