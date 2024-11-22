# CSV Plotter

This script, `plot.py`, is designed to plot data from a CSV file using Matplotlib. It reads the CSV file, extracts the data, and generates a plot saved as a PNG image.

## Requirements

- Python 3.x
- Matplotlib

## Installation

To install the required dependencies, you can use pip:

```bash
pip install matplotlib
```

## Usage

The script can be run from the command line with the following options:

```bash
python plot.py [-h] [--start START] [--end END] [--width WIDTH] [--height HEIGHT] [--no-labels] file_path
```

### Positional Arguments

- `file_path`: Path to the CSV file containing the data to be plotted.

### Optional Arguments

- `--start START`: Start time for the plot (default: None).
- `--end END`: End time for the plot (default: None).
- `--width WIDTH`: Width of the output image in pixels (default: 800).
- `--height HEIGHT`: Height of the output image in pixels (default: 600).
- `--no-labels`: Remove labels and axes from the plot.

## Example

To plot data from a CSV file named `data.csv` with default settings, run:

```bash
python plot.py data.csv
```

To plot data with a specific time range and image dimensions, run:

```bash
python plot.py data.csv --start 0.0 --end 10.0 --width 1024 --height 768
```

This will generate a `plot.png` file in the current directory.

## License

This project is licensed under the MIT License.
