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
    domain = re.search("@[\w.]+", email)
    return domain.group() if domain else None

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity