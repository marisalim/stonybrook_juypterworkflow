import os
from urllib.request import urlretrieve
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL,
                     force_download=False):
    """Download and cache Fremont bike data.
    Uses pandas to format timestamps and add column labeling to return
    a dataframe ready for analysis.
    
    Args:
        filename (str): CSV file of data
        url (str): URL to retrieve file if not already downloaded
        force_download (bool): Force (re-)download of file.
        
    Returns:
        pandas.DataFrame: Fremont bike counter data
 
    """
    if force_download or not os.path.exists(filename):
        # You can now download the data from the database
        urlretrieve(url, filename)
    data = pd.read_csv(filename, index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format="%m/%d/%Y %I:%M:%S %p")
    except (ValueError, TypeError):
        data.index = pd.to_datetime(data.index)
    data.columns = ['East', 'West']
    data['Total'] = data['West'] + data['East']
    return data