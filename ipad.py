import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

df = pd.read_html('https://en.m.wikipedia.org/wiki/List_of_Nobel_laureates')[0]
print(f'Total tables: {len(df)}')
print(type(df))
print(df.head())