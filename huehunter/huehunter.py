import sys
import cv2
import numpy as np
from PIL import Image
import fast_colorthief
import webcolors

def detect_colors(image_path):
    """Detects the dominant colors in an image and returns their closest CSS3 color names."""
    # Load image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        return ["Image not found or unable to load."]
    
    # Convert the image to RGB (for PIL handling)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(img_rgb)

    # Convert image for color extraction
    image_pil = image_pil.convert('RGBA')
    image_np = np.array(image_pil).astype(np.uint8)

    # Get a palette of dominant colors
    palette = fast_colorthief.get_palette(image_np, color_count=5, quality=10)

    # Map the dominant colors to closest CSS3 color names
    color_names = []
    for color in palette:
        closest_color_name = get_closest_color_name(color)
        if closest_color_name not in color_names:
            color_names.append(closest_color_name)

    return color_names

def get_closest_color_name(rgb_color):
    """Finds the closest CSS3 color name to a given RGB color."""
    min_diff = float('inf')
    closest_color_name = None
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        diff = sum([(r - rgb_color[0])**2, (g - rgb_color[1])**2, (b - rgb_color[2])**2])
        if diff < min_diff:
            min_diff = diff
            closest_color_name = color_name
    return closest_color_name

def main():
    """Main function to handle command line arguments and print color detections."""
    if len(sys.argv) < 2:
        print("\033[91mUsage: huehunter <image_path>\033[0m")  # Red color for usage error
        sys.exit(1)

    image_path = sys.argv[1]
    color_description = detect_colors(image_path)
    image_name = image_path.split('/')[-1]
    print("\033[96mImage Name:\033[0m", "\033[93m{}\033[0m".format(image_name))  # Cyan for label, Yellow for image name
    print("\033[96mDetected Colors:\033[0m", "\033[92m{}\033[0m".format(', '.join(color_description)))  # Green for detected colors

if __name__ == "__main__":
    main()