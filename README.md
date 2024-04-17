
# HueHunter 🎨 

HueHunter is a Python command-line tool designed to detect and name the dominant colors in images. It analyzes images and maps the detected colors to the closest CSS3 color names, helping designers, developers, and artists to quickly identify key colors used in various visual media.

## Features

- Detects dominant colors in an image.
- Maps detected colors to the nearest CSS3 color names.
- Simple command-line interface for easy use.

## Installation

Before installing HueHunter, ensure you have Python installed on your system. HueHunter works best with Python 3.6 or newer.

To install HueHunter, run the following command:

```bash
pip install HueHunter
```

This command will download and install HueHunter along with its dependencies.

## Dependencies

HueHunter relies on several third-party libraries:

- OpenCV-Python: For image processing.
- Pillow: For image manipulation tasks.
- numpy: For numerical operations.
- fast-colorthief: For extracting color palettes.
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
Image Name: example.jpg, Colors: ['black', 'darkslategray', 'dimgray']
```

This output tells you the image name and lists the dominant colors detected in the image.

## Contributing

Contributions to HueHunter are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

HueHunter is open-sourced under the MIT license. See the LICENSE file for more details.

## Contact

For support or to contact the developers, please send an email to [roshanwarrierwork@gmail.com].

Thank you for using HueHunter!
