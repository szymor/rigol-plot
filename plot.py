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

    # Plot the data
    plt.plot(timestamps, data, linewidth=1)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage')
    
    # Save the plot as a PNG file
    plt.savefig('plot.png')
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot data from a CSV file.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    parser.add_argument('--start', type=float, default=None, help='Start time for the plot')
    parser.add_argument('--end', type=float, default=None, help='End time for the plot')
    args = parser.parse_args()

    plot_data_from_csv(args.file_path)
