import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def scatter_plot_with_name(data):
    # Get the directory of the running script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Define the file path dynamically
    file_path = os.path.join(script_dir, 'scatter_plot.png')
    
    plt.close('all')  # Close all open figures
    plt.clf()         # Clear the current figure
    
    plt.figure(figsize=(12, 8))
    sns.scatterplot(
        x='yop',        # x-axis: Year of Production
        y='price',      # y-axis: Price
        hue='brand',    # Color points by Brand
        data=data,
        palette='tab20',# Use tab20 palette
        alpha=0.8       # point transparency        
    )
    # Plot Label
    plt.title('Price vs. Year of Production by Brand')
    plt.xlabel('Year of Production')
    plt.ylabel('Price')

    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

    """top_expensive = data.nlargest(10, 'price')  # Select top 10 watches by price
    for _, row in top_expensive.iterrows():
        plt.text(
            row['yop'], 
            row['price'], 
            row['name'], 
            fontsize=8, 
            alpha=0.7
        )
    """
    
    plt.legend(title='Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    plt.savefig(file_path)  # Save dynamically in the script's directory
    plt.close()  # Close the plot to avoid warnings

# Usage
# scatter_plot_with_name(your_dataframe)
