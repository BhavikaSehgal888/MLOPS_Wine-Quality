#Read data from data source
# Save it in data/raw for further processing

import os
from src.get_data import read_params,get_data
import argparse

def load_and_save_data(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_columns = [col.replace(" ","_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(os.path.join(os.path.split(os.getcwd())[0],raw_data_path),sep=",",index=False, header=new_columns)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parse_args = args.parse_args()
    load_and_save_data(config_path=parse_args.config)


