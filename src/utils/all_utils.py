import numpy as np
import pandas as pd
import yaml
import logging
import json
import os


def readYamlFile(filepath:str) -> dict:
    with open(filepath) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"Yaml file loaded sucessfully")
    return content


def createDicrectory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        logging.info(f"{dir_path} directory created")

def saveToLoacal(data,datapath,index_status = False):
    data.to_csv(datapath,index_status = False)
    logging.info(f"{data} is sucessfully saved")