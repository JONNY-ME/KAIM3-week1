import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(df, date_column='date', stock_value_column='stock_value', title='Stock Value Over Time'):
    """
    Plots stock value over time from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.
    - date_column (str): The name of the date column in the CSV file (default is 'date').
    - stock_value_column (str): The name of the stock value column in the CSV file (default is 'stock_value').
    - title (str): Title for the plot (default is 'Stock Value Over Time').
    """

    df[date_column] = pd.to_datetime(df[date_column], errors='coerce', format='%Y-%m-%d %H:%M:%S')

    df.dropna(subset=[date_column], inplace=True)

    plt.figure(figsize=(10, 6))
    plt.plot(df[date_column], df[stock_value_column], label=stock_value_column, color='b')

    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    plt.title(title)

    plt.xticks(rotation=45)

    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_time_series(data, time_unit, title, xlabel):
    """
    Plots article count over time (year, month, week, or day) aggregated by the specified time_unit.

    Parameters:
        data: DataFrame containing a datetime column 'date'.
        time_unit: One of 'year', 'month', 'week', or 'day'.
        title: Title of the plot.
        xlabel: Label for the x-axis.
    """
    
    # Extract year, month, week, and day for aggregation
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.to_period('M').dt.strftime('%Y-%m') 
    data['week'] = data['date'].dt.to_period('W').dt.strftime('%Y-%U')  
    data['day'] = data['date'].dt.date  

    # Group by the selected time_unit
    if time_unit == 'year':
        grouped_data = data.groupby('year').size().reset_index(name='article_count')
        x_column = 'year'
    elif time_unit == 'month':
        grouped_data = data.groupby('month').size().reset_index(name='article_count')
        x_column = 'month'
    elif time_unit == 'week':
        grouped_data = data.groupby('week').size().reset_index(name='article_count')
        x_column = 'week'
    elif time_unit == 'day':
        grouped_data = data.groupby('day').size().reset_index(name='article_count')
        x_column = 'day'
    else:
        raise ValueError("Invalid time_unit. Use 'year', 'month', 'week', or 'day'.")

    # Plot the data
    plt.figure(figsize=(24, 6))
    plt.plot(grouped_data[x_column], grouped_data['article_count'], marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Article Count')
    plt.xticks(rotation=90)  
    plt.grid(True)
    plt.tight_layout()
    plt.show()
