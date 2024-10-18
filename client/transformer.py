import pandas as pd
import numpy as np
from numpy import add

# Read csv
df = pd.read_csv('small_online_retail.csv')

# Add a json column to the dataframe (splitlines will split the json into multiple rows not a single one)
df['json'] = df.to_json(orient='records', lines=True).splitlines()

# Get json column of dataframe
dfjson = df['json']

# Print out the dataframe to a file
# Note that the timestamp forward slash will be escaped to stay true to JSON schema
np.savetxt(r'./output.txt', dfjson.values, fmt='%s')