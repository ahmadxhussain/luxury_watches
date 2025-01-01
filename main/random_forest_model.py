from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import os

#first load data back into it

def random_forest():
    
    #get data and read from data. getting file path
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up one level from 'main'
    filtered_data_path = os.path.join(base_dir, 'csv_locators/filtered_data.csv')
    
    filtered_data = pd.read_csv(filtered_data_path)
    
    x = filtered_data[['brand', 'yop', 'model', 'cond', 'size']]
    y = filtered_data['price']
    
    x = pd.get_dummies(x, columns=['brand', 'model', 'cond', 'size'], drop_first=True)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)
    
    rfModel = RandomForestRegressor()
    
    rfModel.fit(x_train, y_train)
    
    y_pred = rfModel.predict(x_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R² Score: {r2}")
    
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.title('Actual vs. Predicted Prices')
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.show()

    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

    # Save the plot dynamically to the same directory as the script
    plot_path = os.path.join(base_dir, 'main/random_forest_plot.png')
    plt.savefig(plot_path)
    #print(f"Prediction plot saved to: {plot_path}")

    plt.show()
    plt.close()