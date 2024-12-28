import pandas as pd

print(__file__)

# src/ufo_data_etl/data/clean_data

# cleaned_csv_file = 'ufo_data_etl/data/clean_data/ufo_data/filtered.csv'
cleaned_csv_file = 'src/ufo_data_etl/data/clean_data/ufo_data/filtered.csv'

ufo_data = pd.read_csv(cleaned_csv_file)

print(ufo_data.describe())