from data_reading import read_and_filter
from plott import scatter_plot_with_name
from linear_model import model_regression
from random_forest_model import random_forest
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
        print("Successul Scatter Plot created")
        model_regression()
        print("Linear Regression Model Created.")
        random_forest()
        print("Random Forest Regression Model Created")
    else:
        print("Data not read, or not filtered")
        
        