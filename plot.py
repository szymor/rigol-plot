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
        t0 = float(header[1].split('=')[1].strip().replace('s', ''))
        tInc = float(header[2].split('=')[1].strip().replace('s', ''))
        
        # Extract data and calculate timestamps
        data = []
        timestamps = []
        current_time = t0
        for row in csvreader:
            if row[0]:
                data.append(float(row[0]))
                timestamps.append(current_time)
                current_time += tInc

    # Plot the data
    plt.plot(timestamps, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage')
    
    # Save the plot as a PNG file
    plt.savefig('plot.png')
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot data from a CSV file.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    plot_data_from_csv(args.file_path)
