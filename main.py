import os


def download_dataset_if_needed():
    from io import BytesIO
    from zipfile import ZipFile
    import requests

    if not os.path.exists(os.path.join('data/cats_and_dogs_filtered/')):
        dataset_url = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
        response = requests.get(dataset_url)
        zipfile = ZipFile(BytesIO(response.content))
        zipfile.extractall('data/')


download_dataset_if_needed()
