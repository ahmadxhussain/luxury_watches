from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

def model_regression():
        
    # Get the full path to the saved filtered data
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up one level from 'main'
    filtered_data_path = os.path.join(base_dir, 'csv_locators/filtered_data.csv')

    # Load the filtered data directly from the CSV
    filtered_data = pd.read_csv(filtered_data_path)

    # Debugging: Check if data loaded correctly
    print(f"Filtered data loaded successfully with {filtered_data.shape[0]} rows.")
    #print(filtered_data.head())

    # Select features (X) and target (y)
    X = filtered_data[['brand', 'yop', 'model', 'cond', 'size']]
    y = filtered_data['price']

    # Convert categorical 'brand' to numeric using one-hot encoding
    X = pd.get_dummies(X, columns=['brand', 'model', 'cond', 'size'], drop_first=True)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Test the model with the test data
    y_pred = model.predict(X_test)

    # Print model coefficients and intercept
    #print("Model Coefficients:", model.coef_)
    #print("Model Intercept:", model.intercept_)
    # Print performance metrics
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R² Score:", r2_score(y_test, y_pred))

    # Visualize Actual vs. Predicted Prices
    plt.scatter(y_test, y_pred)
    plt.title('Actual vs. Predicted Prices')
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

    # Save the plot dynamically to the same directory as the script
    plot_path = os.path.join(base_dir, 'main/prediction_plot.png')
    plt.savefig(plot_path)
    #print(f"Prediction plot saved to: {plot_path}")

    plt.show()
    plt.close()
