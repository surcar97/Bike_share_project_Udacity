import pandas as pd
import numpy as np
import time
CITY_DATA = { 'CH': 'chicago.csv',
              'NY': 'new_york_city.csv',
              'DC': 'washington.csv' }

city = 'CH'
df = pd.read_csv(CITY_DATA[city])
city.index('')
def capitalize_input(city):
    for i in city