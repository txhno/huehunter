import sys
import cv2
import numpy as np
from PIL import Image
import webcolors
from sklearn.cluster import KMeans

def load_image(image_path):
    """Loads an image from the specified path."""
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Image not found or unable to load.")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def get_dominant_colors(img_rgb, num_colors=5):
    """Extracts the dominant colors from an RGB image."""
    pixels = img_rgb.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)
    return colors

def closest_css3_color_name(rgb_color):
    """Finds the closest CSS3 color name to a given RGB color."""
    min_diff = float('inf')
    closest_color = None
    for hex_code, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(hex_code)
        diff = (r - rgb_color[0]) ** 2 + (g - rgb_color[1]) ** 2 + (b - rgb_color[2]) ** 2
        if diff < min_diff:
            min_diff = diff
            closest_color = color_name
    return closest_color

def detect_colors(image_path):
    """Detects the dominant colors in an image and returns their closest CSS3 color names."""
    img_rgb = load_image(image_path)
    dominant_colors = get_dominant_colors(img_rgb)
    color_names = [(closest_css3_color_name(color), color) for color in dominant_colors]
    return color_names

def rgb_to_ansi(rgb):
    """Converts an RGB tuple to an ANSI terminal color code."""
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"

def main():
    if len(sys.argv) < 2:
        print("\033[91mUsage: huehunter <image_path>\033[0m")
        sys.exit(1)

    image_path = sys.argv[1]
    try:
        color_descriptions = detect_colors(image_path)
        image_name = image_path.split('/')[-1]
        print("\033[96mImage Name:\033[0m", "\033[93m{}\033[0m".format(image_name))
        detected_colors_output = ', '.join([f"{rgb_to_ansi(color[1])}{color[0]}\033[0m" for color in color_descriptions])
        print("\033[96mDetected Colors:\033[0m", detected_colors_output)
    except FileNotFoundError as e:
        print("\033[91mError:\033[0m", e)

if __name__ == "__main__":
    main()
