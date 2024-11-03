import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import  dataclass # we use this  to define the data structure of the data  (class variable) 

@dataclass   # directly define class variable, no need of init
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv') # Each variable is assigned a default value that represents the file path where the training and testing data will be stored. 
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    
class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()  #  we create an object of the class variable DataIngestionConfig , where infestion_config will refrence object of DataIngestionConfig() having train_data_path,test_data_path and raw_data_path
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(r'notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # if its already there then we dont have to delete it and recreate it again
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
        
            train_set, test_set = train_test_split(df,test_size=0.2,random_state = 42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of data completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                # these two will be reqired in data transformation
            ) 
        except Exception as e:
            raise CustomException(e,sys) from e
        
if  __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()  


