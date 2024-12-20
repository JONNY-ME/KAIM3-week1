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


def plot_moving_averages(data, date_column, stock_value_column, window, title):
    '''
    Plot the moving averages for a given stock.

    Parameters:
    - data: DataFrame containing historical stock data
    - date_column: Name of the column containing date information
    - stock_value_column: Name of the column containing stock values
    - window: Window size for moving averages
    - title: Title of the plot

    Returns:
    - None (displays the plot)    
    '''
    plt.figure(figsize=(12, 6))
    plt.plot(data[date_column], data[stock_value_column], label='Close Price')
    plt.plot(data[date_column], data['SMA'], label=f'SMA ({window})')
    plt.plot(data[date_column], data['EMA'], label=f'EMA ({window})')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_correlation(data, x_col, y_col, title):
    '''
    Plot the correlation between two columns in the data

    :param data: The DataFrame containing the data
    :param x_col: The column name for the x-axis
    :param y_col: The column name for the y-axis
    :param title: The title of the plot

    :return: None
    '''
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_col], data[y_col], color='blue')
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()