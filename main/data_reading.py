
import pandas as pd
import os

# Constants
REQUIRED_COLS = ['brand', 'name', 'yop', 'price', 'model', 'cond', 'size']
MAX_PRICE = 1_000_000
MIN_YEAR = 1900



#now we will read data.

def read_and_filter(filename):
    try:
        
        
        read = pd.read_csv(filename, low_memory=False) #adress warning about mxied data types
        
        print(read.shape[0])
        
        # Clean column names
        read.columns = read.columns.str.strip().str.lower()
    

         #read all data
        filtered_data = read.loc[:, REQUIRED_COLS]

        # Clean 'yop' column
        filtered_data['yop'] = filtered_data['yop'].str.extract(r'(\d{4})', expand=False)
        filtered_data['yop'] = pd.to_numeric(filtered_data['yop'], errors='coerce')

        # Clean 'price' column
        filtered_data['price'] = filtered_data['price'].str.replace(r'[^\d.]', '', regex=True)  # Remove non-numeric characters
        filtered_data['price'] = filtered_data['price'].replace('', float('nan'))  # Replace empty strings with NaN
        filtered_data['price'] = pd.to_numeric(filtered_data['price'], errors='coerce')  # Convert to float
        
        #clean size column
        filtered_data['size'] = filtered_data['size'].str.extract(r'(\d+)', expand=False)
        filtered_data['size'] = filtered_data['size'].replace('', float('nan'))  # Replace empty strings with NaN
        filtered_data['size'] = pd.to_numeric(filtered_data['size'], errors='coerce')  # Convert to float

        # Drop rows with missing or invalid values in 'yop' or 'price'
        filtered_data = filtered_data.dropna(subset=['yop', 'price', 'cond', 'model'])
        
        #Also filter data for outliers, before 1900 and price < 1,000,000
        filtered_data = filtered_data[
            (filtered_data['yop'] >= MIN_YEAR) &
            (filtered_data['price'] <= MAX_PRICE)
        ]

        # Save filtered data to a new CSV file
        save_path = os.path.join(os.path.dirname(filename), 'filtered_data.csv')
        filtered_data.to_csv(save_path, index=False)

        #print(filtered_data.head())
    
        return filtered_data
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    