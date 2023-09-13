import configparser

import pandas as pd


def load_config(category: str) -> configparser.SectionProxy:
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[category]


def save_dataframe(df: pd.DataFrame, save_path: str):
    df.to_csv(save_path, encoding = "utf-8", index=False)
