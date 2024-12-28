import os
import csv
from pathlib import Path
from typing import List
from constant import csv_file_path

def remove_unwanted_data(csv_file_path: Path) -> List:
    """
    Clean / remove rows which has more columns.

    :param: csv_file_path csv file path.
    :return: list of clean data
    """

    data_list = []
    
    with open(csv_file_path, 'r') as csv_file:

        raw_csv_data = csv.reader(csv_file)

        for index, row in enumerate(raw_csv_data):

            if index == 0:
                
                columns = row
                print(f"Setting columns values {columns}")
                data_list.append(row)

            elif len(row) > len(columns):

                # print(f"More columns found at {index} {len(row)}")
                pass

            else:

                data_list.append(row)
        
        print(f"Total Rows in Raw Data {index}")

    return data_list


def create_folder(file_path: Path) -> Path:
    """
    Create folder if not exists.

    :param: file_path csv file path
    :return: csv file path 
    """

    new_csv_file = file_path.replace("raw", "clean").replace("complete", "filtered")

    if not os.path.exists(os.path.dirname(new_csv_file)):

        os.mkdir(os.path.dirname(new_csv_file))
    
    return new_csv_file


def create_csv_file(csv_file_name: Path, csv_data: List[List]):
    """
    Write clean data to csv file.

    :param: csv_file_name csv file path.
    :param: csv_data clean csv data.
    """

    with open(csv_file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator="\n")
        csv_writer.writerows(csv_data)

    print(f"CSV file created successfully at {csv_file_name}")


if __name__ == "__main__":

    clean_data = remove_unwanted_data(csv_file_path)

    print(f"Total rows in Cleaned data {len(clean_data)}")

    new_csv_file = create_folder(csv_file_path)

    create_csv_file(new_csv_file, clean_data)



