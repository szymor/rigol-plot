#!/bin/env python3

import matplotlib.pyplot as plt
import csv
import argparse

def plot_data_from_csv(file_path):
    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # Skip the header
        next(csvreader)
        
        # Extract data
        data = [float(row[0]) for row in csvreader if row[0]]

    # Plot the data
    plt.plot(data)
    plt.xlabel('Sample Number')
    plt.ylabel('Voltage')
    
    # Save the plot as a PNG file
    plt.savefig('plot.png')
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot data from a CSV file.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    plot_data_from_csv(args.file_path)
