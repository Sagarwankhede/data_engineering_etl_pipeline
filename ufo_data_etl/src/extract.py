from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
from constant import dataset_name, raw_data_path

def authenticate_kaggle() -> KaggleApi:
    """
    Function for authenticating Kaggle API.
    :return: KaggleApi object.
    """

    api = KaggleApi()
    api.authenticate()
    return api

def download_dataset(kaggle_api: KaggleApi, kaggle_dataset_name: str, dataset_path: Path) -> None:
    """
    Download any kaggle dataset.

    :param: kaggle_api object.
    :param: kaggle_dataset_name with username.
    :param: dataset_path folder where to download dataset.
    """

    try:

        kaggle_api.dataset_download_files(kaggle_dataset_name, path=dataset_path, unzip=True)
        print(f"Dataset downloaded successfully.... at {dataset_path}")

    except Exception as error_msg:

        print(f"{str(error_msg)}")


if __name__ == '__main__':

    kaggle_api_object = authenticate_kaggle()

    download_dataset(kaggle_api_object, kaggle_dataset_name=dataset_name, dataset_path=raw_data_path)
