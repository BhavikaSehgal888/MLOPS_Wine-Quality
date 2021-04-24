## Read Params
## Process
## return dataframe
import os
import yaml
import pandas as pd
import numpy as np
import argparse

def read_params(config_path):
    with open(config_path) as file:
        config = yaml.safe_load(file)
    return config

def get_data_given(config_path):
    config = read_params(config_path)
    #print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path,sep=";",encoding="utf-8")
    return df


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parse_args = args.parse_args()
    data = get_data_given(config_path=parse_args.config)