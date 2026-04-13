# HueHunter

🎨 HueHunter: A command-line tool for quickly identifying and naming dominant colors in digital images. 🌈

## Features

- Detects dominant colors in an image using KMeans clustering.
- Maps detected colors to the nearest CSS3 color names for easy reference.
- Simple command-line interface for straightforward usage.

## Installation

Before installing HueHunter, ensure you have Python installed on your system.

To install the current source version:

```bash
git clone https://github.com/txhno/huehunter.git
cd huehunter
python -m pip install .
```

If you want to install directly from GitHub without cloning the repository first:

```bash
python -m pip install git+https://github.com/txhno/huehunter.git
```

Both commands install HueHunter and its dependencies in one step.

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
