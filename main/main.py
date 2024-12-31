
import pandas as pd
import os


#now we will read data.

def read_and_filter(filename):
    try:
        
        read = pd.read_csv(filename)
    
        #ensure first 5 are correct
        #print(read.head())
        
        required_cols = ['brand', 'name', 'yop', 'price']
    
        #will filter the first 500 rows by Brand, Name, YOP, and Price
        filtered_data = read.loc[:499, required_cols]
        
        save_path = os.path.join(os.path.dirname(filename), 'filtered_data.csv')
    
        filtered_data.to_csv(save_path, index = False)

        #print(filtered_data.head())
    
        return filtered_data
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def main():
    filename = '/workspaces/luxury_watches/csv_locators/Watches.csv'
    data = read_and_filter(filename)
    
    print(data)
    print(f"Total number of columns: {data.shape[0]}")
    
#to run main
if __name__ == "__main__":
    main()
    