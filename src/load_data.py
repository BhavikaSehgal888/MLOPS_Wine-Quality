#Read data from data source
# Save it in data/raw for further processing

import os
import pandas as pd
import yaml
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

def load_and_save_data(config_path):
    config = read_params(config_path)
    df = get_data_given(config_path)
    new_columns = [col.replace(" ","_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path,sep=",",index=False, header=new_columns)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parse_args = args.parse_args()
    load_and_save_data(config_path=parse_args.config)


