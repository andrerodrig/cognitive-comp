import re
import unicodedata
import pandas as pd

from typing import List


def slugify(text: str) -> str:
    slug = unicodedata.normalize('NFKD', text) \
        .encode('ascii', 'ignore') \
        .lower() \
        .decode('utf-8')
        
    slug = re.sub(r'(?:https\S+|http|@|#)', '', slug)
    return re.sub(r'[^\w\s]+', '', slug).strip('_')


def standardize(df: pd.DataFrame, col: str) -> pd.Series:
    for index, data in df[col].iteritems():
        df[col].loc[index] = slugify(data)
    
    return df[col]


def standardize_dataset(df: pd.DataFrame) -> pd.DataFrame:
    for col in df:
        if all([isinstance(txt, str) for txt in df[col]]):
            df[col] = standardize(df, col)
    
    return df