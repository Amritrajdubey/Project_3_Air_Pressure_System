import logging
import os
from datetime import datetime 
import os,sys

LOG_FILE_NAME = f"{datetime().now().strftime('%m%d%y_%H%M_%S')}.log" # Log file name
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs") # Log file directory

os.makedirs(LOG_FILE_DIR,exit_ok =True) #Create folder if now exist

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME) #Log file path

logging.basicConfig(
    filename= LOG_FILE_PATH ,
     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)
