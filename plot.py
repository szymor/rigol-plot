#!/bin/env python3

import matplotlib.pyplot as plt
import csv
import argparse

def plot_data_from_csv(file_path):
    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # Read the header to get t0 and tInc
        header = next(csvreader)
        t0 = float(header[1].split('=')[1].strip().replace('s', '').replace('E', 'e'))
        tInc = float(header[2].split('=')[1].strip().replace('s', '').replace('E', 'e'))
        
        # Extract data and calculate timestamps, filtering by start and end time
        data = []
        timestamps = []
        current_time = t0
        for row in csvreader:
            if row[0]:
                if (args.start is None or current_time >= args.start) and (args.end is None or current_time <= args.end):
                    data.append(float(row[0]))
                    timestamps.append(current_time)
                current_time += tInc

    # Determine the appropriate time scale for labels
    if timestamps:
        time_range = max(timestamps) - min(timestamps)
        if time_range < 1e-9:
            time_scale = 1e12
            time_unit = 'ps'
        elif time_range < 1e-6:
            time_scale = 1e9
            time_unit = 'ns'
        elif time_range < 1e-3:
            time_scale = 1e6
            time_unit = 'µs'
        elif time_range < 1:
            time_scale = 1e3
            time_unit = 'ms'
        else:
            time_scale = 1
            time_unit = 's'
    else:
        time_scale = 1
        time_unit = 's'
    # Adjust timestamps according to the time scale
    scaled_timestamps = [t * time_scale for t in timestamps]
    plt.plot(scaled_timestamps, data, linewidth=1)

    plt.xlabel(f'Time ({time_unit})')
    plt.ylabel('Voltage')
    
    # Save the plot as a PNG file with specified dimensions
    plt.gcf().set_size_inches(args.width / plt.gcf().dpi, args.height / plt.gcf().dpi)
    plt.savefig('plot.png', dpi=plt.gcf().dpi)
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot data from a CSV file.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    parser.add_argument('--start', type=float, default=None, help='Start time for the plot')
    parser.add_argument('--end', type=float, default=None, help='End time for the plot')
    parser.add_argument('--width', type=int, default=800, help='Width of the output image in pixels')
    parser.add_argument('--height', type=int, default=600, help='Height of the output image in pixels')
    args = parser.parse_args()

    plot_data_from_csv(args.file_path)
