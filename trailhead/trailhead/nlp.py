import nltk


def get_nltk_models(model: str) -> bool:
    download = nltk.download(model)
    if download:
        print(f'{model} downloaded.')
        return download
    else:
        raise ValueError('Data not found!')