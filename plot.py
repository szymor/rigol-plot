import matplotlib.pyplot as plt
import csv

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
    plt.title('Data Plot')
    plt.xlabel('Sample Number')
    plt.ylabel('Value')
    
    # Save the plot as a PNG file
    plt.savefig('plot.png')
    plt.close()

if __name__ == "__main__":
    plot_data_from_csv('example.csv')
