# HueHunter

🎨 HueHunter: A command-line tool for quickly identifying and naming dominant colors in digital images. 🌈

## Features

- Detects dominant colors in an image using KMeans clustering.
- Maps detected colors to the nearest CSS3 color names for easy reference.
- Simple command-line interface for straightforward usage.

## Installation

Before installing HueHunter, ensure you have Python installed on your system. HueHunter works best with Python 3.6 or newer.

To install HueHunter directly from the source:

1. First, clone the repository:
   ```bash
   git clone https://github.com/txhno/huehunter.git
   ```
2. Navigate to the `huehunter` directory:
   ```bash
   cd huehunter
   ```
3. Install the package:
   ```bash
   pip install .
   ```

This series of commands will download the HueHunter source, move you into the HueHunter project directory, and install HueHunter along with its dependencies directly from the source code. This method is particularly useful if you plan to modify the code or contribute to the project.

## Dependencies

HueHunter relies on several third-party libraries:

- OpenCV-Python: For image processing.
- Pillow: For image manipulation tasks.
- numpy: For numerical operations.
- scikit-learn: For performing KMeans clustering to determine dominant colors.
- webcolors: For converting RGB values to human-readable color names.

These dependencies are automatically installed when you install HueHunter via pip.

## Usage

Once installed, you can run HueHunter directly from your terminal. To analyze an image and print out its dominant colors, use the following syntax:

```bash
huehunter path/to/your/image.jpg
```

### Example

```bash
huehunter example.jpg
```

Output:
```
Image Name: example.jpg
Detected Colors: silver, darkslategray, dimgray
```

This output tells you the image name and lists the dominant colors detected in the image.

## Contributing

Contributions to HueHunter are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

HueHunter is open-sourced under the MIT license. See the LICENSE file for more details.

## Contact

For support or to contact the developers, please send an email to [roshanwarrierwork@gmail.com].

Thank you for using HueHunter!
