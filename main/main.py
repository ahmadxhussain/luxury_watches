from data_reading import read_and_filter
from plott import scatter_plot_with_name
import os

if __name__ == "__main__":
    # Dynamically get the full path to the CSV file
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go one level up from 'main'
    filename = os.path.join(base_dir, 'csv_locators/Watches.csv')
    
    #read data
    data = read_and_filter(filename)
    
    
    #check if data is empty otherwise run scatter plot
    if data is not None:
        print(data.shape[0])
        #print(data.head())
        scatter_plot_with_name(data)
        print("Successul plot created")
    else:
        print("Data not read, or not filtered")
        
        