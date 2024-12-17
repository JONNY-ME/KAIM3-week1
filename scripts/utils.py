import pandas as pd
import re
from textblob import TextBlob

def read_csv_file(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Remove any 'Unnamed:' columns
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    
    # Get additional info
    column_names = data.columns.tolist()  
    row_count = data.shape[0]  
    
    return {
        'data': data,
        'column_names': column_names,
        'row_count': row_count
    }


def extract_domain(email):
    '''
    Extracts the domain from an email address.

    Parameters:
    email (str): Email address

    Returns:
    str: Domain name    
    '''
    domain = re.search("@[\w.]+", email)

    return domain.group() if domain else None

def get_sentiment(text):
    '''
    Get sentiment polarity of the text.

    Parameters:
    text (str): Text for sentiment analysis

    Returns:
    float: Sentiment polarity
    '''

    analysis = TextBlob(text)

    return analysis.sentiment.polarity

def calculate_moving_averages(data, window=50):
    '''
    Calculate simple and exponential moving averages for the given stock data.

    Parameters:
    data (DataFrame): Stock data
    window (int): Window size for moving averages

    Returns:
    DataFrame: Stock data with moving averages 
    '''
    data['SMA'] = data['Close'].rolling(window=window).mean()
    data['EMA'] = data['Close'].ewm(span=window, adjust=False).mean()
    
    return data
