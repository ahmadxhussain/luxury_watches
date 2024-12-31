
import pandas as pd
import os


#now we will read data.

def read_and_filter(filename):
    try:
        
        read = pd.read_csv(filename, low_memory=False) #adress warning about mxied data types
        
        # Clean column names
        read.columns = read.columns.str.strip().str.lower()
    
        required_cols = ['brand', 'name', 'yop', 'price']

         # Filter the first 500 rows by required columns
        filtered_data = read.loc[:499, required_cols]

        # Clean 'yop' column
        filtered_data['yop'] = filtered_data['yop'].str.extract(r'(\d{4})', expand=False)
        filtered_data['yop'] = pd.to_numeric(filtered_data['yop'], errors='coerce')

        # Clean 'price' column
        filtered_data['price'] = filtered_data['price'].str.replace(r'[^\d.]', '', regex=True)  # Remove non-numeric characters
        filtered_data['price'] = filtered_data['price'].replace('', float('nan'))  # Replace empty strings with NaN
        filtered_data['price'] = pd.to_numeric(filtered_data['price'], errors='coerce')  # Convert to float

        # Drop rows with missing or invalid values in 'yop' or 'price'
        filtered_data = filtered_data.dropna(subset=['yop', 'price'])

        # Save filtered data to a new CSV file
        save_path = os.path.join(os.path.dirname(filename), 'filtered_data.csv')
        filtered_data.to_csv(save_path, index=False)

        #print(filtered_data.head())
    
        return filtered_data
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    
