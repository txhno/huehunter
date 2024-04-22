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
        return [("Image not found or unable to load.", (0, 0, 0))]

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
        closest_color_name, closest_color_rgb = get_closest_color_name(color)
        if closest_color_name not in [c[0] for c in color_names]:
            color_names.append((closest_color_name, closest_color_rgb))

    return color_names

def get_closest_color_name(rgb_color):
    """Finds the closest CSS3 color name to a given RGB color."""
    min_diff = float('inf')
    closest_color_name = None
    closest_color_rgb = (0, 0, 0)
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        diff = sum([(r - rgb_color[0])**2, (g - rgb_color[1])**2, (b - rgb_color[2])**2])
        if diff < min_diff:
            min_diff = diff
            closest_color_name = color_name
            closest_color_rgb = (r, g, b)
    return closest_color_name, closest_color_rgb

def rgb_to_ansi(rgb):
    """Converts an RGB tuple to an ANSI terminal color code."""
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"

def main():
    """Main function to handle command line arguments and print color detections."""
    if len(sys.argv) < 2:
        print("\033[91mUsage: huehunter <image_path>\033[0m")  # Red color for usage error
        sys.exit(1)

    image_path = sys.argv[1]
    color_descriptions = detect_colors(image_path)
    image_name = image_path.split('/')[-1]
    print("\033[96mImage Name:\033[0m", "\033[93m{}\033[0m".format(image_name))  # Cyan for label, Yellow for image name
    detected_colors_output = ', '.join([f"{rgb_to_ansi(color[1])}{color[0]}\033[0m" for color in color_descriptions])
    print("\033[96mDetected Colors:\033[0m", detected_colors_output)  # Print color names in their respective colors

if __name__ == "__main__":
    main()
