import re
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from constant import CHUNK_SIZE

DATE_TIME_CLEANUP = True
DROP_COLUMN = True
DURATION_COLUMN = True

cleaned_csv_file = 'src/ufo_data_etl/data/clean_data/ufo_data/filtered.csv'

def read_cleaned_data(csv_file_name: Path) -> pd.DataFrame:
    """
    Reading CSV file using Pandas.

    :param: csv_file_name path.
    :returns: pd.DataFrame.
    """

    return pd.read_csv(csv_file_name)#, chunksize=CHUNK_SIZE)


def show_unique_values(data: pd.DataFrame, column_name: str) -> None:
    """
    Show unique values in a given column in Pandas.

    :param: data Pandas Data frame.
    :param: column_name string.
    """

    print(data[column_name].value_counts().to_list())
    print(list(data[column_name].value_counts().index))


def show_bar_chart(data: pd.DataFrame, column_name: str) -> None:

    height = data[column_name].value_counts().to_list()
    bars = list(data[column_name].value_counts().index)
    y_pos = range(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars, rotation=90)
    plt.show()


def sanitize_date_time(data: pd.DataFrame, column_name: str) -> pd.Series:
    """
    Sanitize given column in Pandas.

    :param: data Pandas Data frame.
    :param: column_name string.
    :returns: pd.Series
    """

    pattern = ' \b24\b:'
    replace_with = ' 00:'
    return data[column_name].map(lambda str_date_time: re.sub(pattern, replace_with, str_date_time))

    
def save_csv_data(data: pd.DataFrame, file_name: Path) -> None:
    """
    Save Pandas Data frame in CSV file using Pandas.

    :param: data Pandas Data frame.
    :param: file_name path.
    """

    data.to_csv(file_name, index=False)
    print(f"Successfully saved CSV file at {file_name}")


def drop_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Drop a given column in Pandas.

    :param: data Pandas Data frame.
    :param: column_name string.
    :returns: pd.DataFrame.
    """

    return data.drop(column_name, axis=1)


def sanitize_duration_column(data: pd.DataFrame, column_name: str) -> pd.Series:
    """
    Sanitize a given column in Pandas.

    :param: data Pandas Data frame.
    :param: column_name string.
    :returns: pd.Series.
    """

    return data[column_name].map(lambda str_duration: int(str(str_duration).split(".")[0].replace("`", "").replace("nan", "1")) 
                                              if str(str_duration).split(".")[0] else int(str_duration))
    

# show_bar_chart(ufo_data, 'country')

# show_bar_chart(ufo_data, 'shape')

# show_bar_chart(ufo_data, 'duration (seconds)')

# show_unique_values(ufo_data, 'duration (seconds)')

# show_unique_values(ufo_data, 'country')

if __name__ == "__main__":

    ufo_data = read_cleaned_data(cleaned_csv_file)

    if not DATE_TIME_CLEANUP:

        print(f"Date Column not sanitized cleaning.....")
        ufo_data['datetime'] = sanitize_date_time(ufo_data, 'datetime')
        save_csv_data(ufo_data, cleaned_csv_file)

    if not DROP_COLUMN:

        print(f"Dropping a column not needed.....")
        ufo_data = drop_column(ufo_data, 'duration (hours/min)')
        save_csv_data(ufo_data, cleaned_csv_file)

    if not DURATION_COLUMN:

        ufo_data['duration (seconds)'] = sanitize_duration_column(ufo_data, 'duration (seconds)')
        save_csv_data(ufo_data, cleaned_csv_file)

    else:

        print("Nothing to do.... zzzzzzz")
