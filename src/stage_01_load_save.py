import numpy as np
import pandas as pd
import argparse
from utils.all_utils import readYamlFile,createDicrectory
import logging
import os
from tqdm import tqdm
import shutil

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def copy_file(source_dir,dest_dir):
    list_dir = os.listdir(source_dir)
    N=len(list_dir)
    for file in tqdm(list_dir,total =N,desc=f'copying file from {source_dir} to {source_dir}', colour="green"):
        src = os.path.join(source_dir, file)
        dest = os.path.join(dest_dir, file)
        shutil.copy(src, dest)

def loadSaveData(config_path):
    config = readYamlFile(config_path)
    source_download_dirs = config['source_download_dirs']
    local_data_dirs = config['local_data_dirs']
    #for source_download_dir, local_data_dir in tqdm(zip(source_download_dirs, local_data_dirs), total=2, desc= "list of folders", colour="red"):
    for source_download_dir,local_data_dir in tqdm(zip(source_download_dirs, local_data_dirs),total=2, desc= "list of folders", colour="red"):
        createDicrectory([local_data_dir])
        copy_file(source_download_dir,local_data_dir)
       

    #copy_file(source_download_dirs,local_data_dirs)



  




if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config','-c',default='config/config.yaml')
    parsed_args = args.parse_args()
    loadSaveData(parsed_args.config)
