import pandas as pd
import numpy as np

from .exceptions import MalformedDataException
    
def extract_csv_data(file):
    df = pd.read_csv(file)
    header_columns = list(df.columns)

    processed_data = []

    for _, row in df.iterrows():
        row_values = row.tolist() 

        if len(row_values) != len(header_columns) or any(pd.isnull(row_values)):
            raise MalformedDataException("The data is malformed or missing data in the rows.")

        processed_data.append([value for value in row_values])

    return processed_data
