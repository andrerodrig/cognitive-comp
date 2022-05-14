import requests
from typing import Union
from pathlib import Path
from zipfile import ZipFile
from invoke import task

from dsm.nlp import get_nltk_models


def create_datadirs(path: Union[Path, str]) -> None:
    path_ = Path(path) 
    if not path_.is_dir():
        path_.mkdir(parents=True)
        
        
def download_data(url: str, filename: str) -> None:
    resp = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for data in resp.iter_content():
            f.write(data)


def unzip_data(dirpath: Union[str, Path], zipname: str) -> None:
    with ZipFile(Path(dirpath) / zipname, 'r') as zipobj:
        zipobj.extractall(dirpath)
        

@task
def get_data(c):
    datadir = Path('./data')
    data_url = 'https://raw.githubusercontent.com/hundredblocks/concrete_NLP_tutorial/master/socialmedia_relevant_cols.csv'
    filepath = datadir / 'socialmedia_relevant_cols.csv'

    create_datadirs(datadir)
    
    if not filepath.is_file():
        download_data(data_url, filename=filepath)
        
    print("Done!")


@task(iterable='model')
def get_model(c, model):
    for m in model:
        get_nltk_models(m)