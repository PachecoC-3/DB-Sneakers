"""
DB Sneakers - Batch Image Background Replacer v2
==================================================
Removes backgrounds from product photos and places them on a black background.
Improved: More aggressive background removal for dark products.
"""

import os
import sys
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageFilter, ImageEnhance
from rembg import remove, new_session

# Configuration
INPUT_FOLDER = Path(__file__).parent / "raw_images"
OUTPUT_FOLDER = Path(__file__).parent / "processed_images"
BACKGROUND_COLOR = (0, 0, 0)  # Black background
OUTPUT_SIZE = (1024, 1024)  # Square images for Shopify
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff'}

# Use the isnet-general-use model - better for product photography
SESSION = None

def get_session():
    global SESSION
    if SESSION is None:
        print("  Loading AI model (first time only)...")
        SESSION = new_session("isnet-general-use")
    return SESSION

def clean_alpha(img_rgba):
    """Make the alpha mask more aggressive - remove gray edges."""
    r, g, b, a = img_rgba.split()
    
    # Make the alpha mask more aggressive:
    # Pixels that are semi-transparent (gray in alpha) get pushed to fully transparent
    # This removes the "halo" effect around dark products
    threshold = 128  # Anything below 50% opacity becomes fully transparent
    a = a.point(lambda x: 255 if x > threshold else 0)
    
    # Slight blur on the alpha to smooth jagged edges, then re-threshold
    a = a.filter(ImageFilter.GaussianBlur(radius=1))
    a = a.point(lambda x: 255 if x > 100 else 0)
    
    return Image.merge("RGBA", (r, g, b, a))

def process_image(input_path, output_path):
    """Remove background and place on black background."""
    print(f"  Processing: {input_path.name}...", end=" ")
    
    # Read the image
    with open(input_path, 'rb') as f:
        input_data = f.read()
    
    # Remove background with better model
    output_data = remove(
        input_data,
        session=get_session(),
        alpha_matting=True,
        alpha_matting_foreground_threshold=270,
        alpha_matting_background_threshold=20,
        alpha_matting_erode_size=10
    )
    
    # Open the result (has transparent background now)
    foreground = Image.open(BytesIO(output_data)).convert("RGBA")
    
    # Clean up the alpha channel - remove gray halos
    foreground = clean_alpha(foreground)
    
    # Create black background
    background = Image.new("RGBA", OUTPUT_SIZE, BACKGROUND_COLOR + (255,))
    
    # Resize foreground to fit nicely (with padding)
    max_size = int(min(OUTPUT_SIZE) * 0.85)
    foreground.thumbnail((max_size, max_size), Image.LANCZOS)
    
    # Center the product on the background
    x = (OUTPUT_SIZE[0] - foreground.width) // 2
    y = (OUTPUT_SIZE[1] - foreground.height) // 2
    
    background.paste(foreground, (x, y), foreground)
    
    # Convert to RGB and save
    final = background.convert("RGB")
    final.save(output_path, "PNG", quality=95)
    print("Done!")

def main():
    print("=" * 60)
    print("  DB SNEAKERS - BATCH IMAGE PROCESSOR v2")
    print("  Improved AI for dark products")
    print("=" * 60)
    print()
    
    # Find all images (including subfolders)
    images = [f for f in INPUT_FOLDER.rglob("*") 
              if f.is_file() and f.suffix.lower() in SUPPORTED_FORMATS]
    
    if not images:
        print(f"  No images found in: {INPUT_FOLDER}")
        print(f"  Drop your product photos in the 'raw_images' folder and try again!")
        print()
        input("  Press Enter to close...")
        return
    
    print(f"  Found {len(images)} image(s) to process")
    print(f"  Input:  {INPUT_FOLDER}")
    print(f"  Output: {OUTPUT_FOLDER}")
    print()
    
    # Process each image
    success = 0
    errors = 0
    for i, img_path in enumerate(images, 1):
        print(f"  [{i}/{len(images)}]", end="")
        try:
            output_name = img_path.stem + "_processed.png"
            output_path = OUTPUT_FOLDER / output_name
            process_image(img_path, output_path)
            success += 1
        except Exception as e:
            print(f" ERROR: {e}")
            errors += 1
    
    print()
    print("=" * 60)
    print(f"  COMPLETE! {success} processed, {errors} errors")
    print(f"  Your images are in: {OUTPUT_FOLDER}")
    print("=" * 60)
    print()
    input("  Press Enter to close...")

if __name__ == "__main__":
    main()
