import pytest
import pandas as pd
import numpy as np
from project import load_csv, smooth, lbound, ubound

def test_load_csv():
    df = load_csv("all_data.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'ifInOctets11' in df.columns

def test_smooth():
    data = {'ifInOctets11': [100, 200, 300, 400, 500]}
    df = pd.DataFrame(data)
    smoothed = smooth(df, 'ifInOctets11', 3)
    assert smoothed.isna().sum() == 2
    assert round(smoothed.iloc[2], 2) == 200.0

def test_lbound():
    assert lbound(100, 20) == 70.0

def test_ubound():
    assert ubound(100, 20) == 130.0
