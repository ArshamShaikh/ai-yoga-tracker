import os
from PIL import Image, ImageDraw, ImageOps

src_dir = r'C:\Users\shams\.gemini\antigravity\brain\a88d7ee9-e08e-4f70-a4be-3c70c75e44dd'
out_dir = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\screenshots_rounded'
os.makedirs(out_dir, exist_ok=True)

# Mapping of images to their descriptive roles
screenshot_map = {
    'media__1791774388440.png': ('screen_1_home_studio.png', 'Studio Home Dashboard'),
    'media__1791774265942.png': ('screen_2_pose_library.png', '75-Pose Taxonomy Library'),
    'media__1791774299410.png': ('screen_3_vinyasa_flows.png', 'Curated Vinyasa Flows'),
    'media__1791774344851.png': ('screen_4_therapeutic_programs.png', 'Therapeutic Programs'),
    'media__1791774235109.png': ('screen_5_practice_analytics.png', 'Practice Analytics & Stats')
}

def round_corners(image_path, output_path, radius=32, border_color=(220, 225, 230), border_width=2):
    im = Image.open(image_path).convert("RGBA")
    w, h = im.size
    
    # Create high-resolution mask for smooth anti-aliased corners
    scale = 2
    mask = Image.new('L', (w * scale, h * scale), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, w * scale - 1, h * scale - 1], radius=radius * scale, fill=255)
    mask = mask.resize((w, h), Image.Resampling.LANCZOS)
    
    # Apply rounded mask
    im.putalpha(mask)
    
    # Create canvas with white background and border
    canvas = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    canvas.paste(im, (0, 0), im)
    
    # Draw subtle border
    border_mask = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(border_mask)
    b_draw.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, outline=border_color + (255,), width=border_width)
    
    final_img = Image.alpha_composite(canvas, border_mask)
    final_img.save(output_path, "PNG")
    print(f"Processed: {output_path} (size: {final_img.size})")

for src_name, (out_name, title) in screenshot_map.items():
    src_file = os.path.join(src_dir, src_name)
    out_file = os.path.join(out_dir, out_name)
    if os.path.exists(src_file):
        round_corners(src_file, out_file, radius=36, border_color=(200, 210, 220), border_width=2)
    else:
        print(f"Source file not found: {src_file}")

print("All screenshots rounded and saved successfully.")
