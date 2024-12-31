
import seaborn as sns
import matplotlib.pyplot as plt


def scatter_plot_with_name(data):
    
    plt.figure(figsize=(24, 16))
    sns.scatterplot(
        x='yop',        # x-axis: Year of Production
        y='price',      # y-axis: Price
        hue='brand',    # Color points by Brand
        data=data,
        palette='viridis',
        alpha=0.8#point transparency        
    )
    #Plot Label
    plt.title('Price vs. Year of Production by Brand')
    plt.xlabel('Year of Production')
    plt.ylabel('Price')
    
    
    # Annotate some points with the watch name
    for _, row in data.iterrows():
        if row['Price'] > 100000:  # Annotate only watches with high prices
            plt.text(
                row['yop'], 
                row['price'], 
                row['name'], 
                fontsize=8, 
                alpha=0.7
            )
    

    
    plt.legend(title='Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
    #plt.tight_layout()
    plt.show()
    plt.savefig("scatter_plot.png")  # Save to the project directory
    plt.close()  # Close the plot to avoid warnings
