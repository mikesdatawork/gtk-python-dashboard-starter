#!/usr/bin/env python3
"""
Logo Generator - Fixed
Creates 150x150 PNG logo with GTK3 and DASHBOARD text that fits properly
"""

from PIL import Image, ImageDraw, ImageFont
import os


def create_logo(output_path, width=150, height=150):
    """
    Create logo with GTK3 and DASHBOARD text that fits within bounds
    
    Args:
        output_path: Where to save the logo
        width: Logo width in pixels
        height: Logo height in pixels
    """
    # Create image with transparent background
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Try to load fonts
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except:
        try:
            font_large = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 38)
            font_small = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 20)
        except:
            # Fallback to default
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
    
    # Text to draw
    text_top = "GTK3"
    text_bottom = "DASHBOARD"
    
    # Get text bounding boxes
    bbox_top = draw.textbbox((0, 0), text_top, font=font_large)
    bbox_bottom = draw.textbbox((0, 0), text_bottom, font=font_small)
    
    # Calculate text dimensions
    text_top_width = bbox_top[2] - bbox_top[0]
    text_top_height = bbox_top[3] - bbox_top[1]
    text_bottom_width = bbox_bottom[2] - bbox_bottom[0]
    text_bottom_height = bbox_bottom[3] - bbox_bottom[1]
    
    # Check if bottom text is too wide and scale if needed
    max_width = width - 10  # Leave 5px margin on each side
    if text_bottom_width > max_width:
        # Calculate scale factor
        scale = max_width / text_bottom_width
        new_size = int(20 * scale)
        try:
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", new_size)
        except:
            try:
                font_small = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", new_size)
            except:
                pass
        # Recalculate
        bbox_bottom = draw.textbbox((0, 0), text_bottom, font=font_small)
        text_bottom_width = bbox_bottom[2] - bbox_bottom[0]
        text_bottom_height = bbox_bottom[3] - bbox_bottom[1]
    
    # Calculate positions (centered)
    spacing = 10  # Reduced from 13
    total_height = text_top_height + text_bottom_height + spacing
    start_y = (height - total_height) // 2
    
    pos_top_x = (width - text_top_width) // 2
    pos_top_y = start_y
    
    pos_bottom_x = (width - text_bottom_width) // 2
    pos_bottom_y = start_y + text_top_height + spacing
    
    # Draw text in white
    draw.text((pos_top_x, pos_top_y), text_top, fill=(238, 238, 238, 255), font=font_large)
    draw.text((pos_bottom_x, pos_bottom_y), text_bottom, fill=(238, 238, 238, 255), font=font_small)
    
    # Save the image
    image.save(output_path, 'PNG')
    print(f"✓ Logo created: {output_path}")
    print(f"  Size: {width}x{height}")
    print(f"  GTK3: {text_top_width}x{text_top_height} at ({pos_top_x}, {pos_top_y})")
    print(f"  DASHBOARD: {text_bottom_width}x{text_bottom_height} at ({pos_bottom_x}, {pos_bottom_y})")


if __name__ == "__main__":
    # Output path
    logo_path = "logo.png"
    
    # Create logo
    create_logo(logo_path, width=150, height=150)
    
    print("")
    print("Logo ready!")
    print(f"Copy to: resources/images/logo.png")
