import pandas as pd

from jupyterworkflow.data import get_fremont_data

def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['East', 'West', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
