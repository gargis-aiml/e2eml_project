# importing all kinds of databases
import os
import sys
from src.exception import CustomException # Use our custom Exception
from src. logger import logging # we need logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# Any required input will go through the following function
@dataclass #decorator
class DataIngestionConfig: #creating input required by data ingestion component
    train_data_path: str=os.path.join("artifacts", "train.csv") #train dataset will be saved in this path
    test_data_path: str=os.path.join("artifacts", "test.csv") #test dataset will be saved in this path
    raw_data_path: str=os.path.join("artifacts", "data.csv") #raw dataset will be saved in this path
# this function knows where to save input, train and test data

class DataIngestion:
    def __init__(self):
        # the 3 paths mentioned above will get saved in this class variable
        self.ingestion_config = DataIngestionConfig() 
    def initiate_data_ingestion(self): #function
        #if your code is saved in some databases
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook\stud.csv") #read the dataset
            logging.info('read the dataset as dataframe') 
            # writing logs to understand where the exceptions are happening
            # create folders for training data, raw data and test data paths 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) # train data path
            # combine directory pathways: if that directory is already there, we will keep that folder.
            # save the raw data path in a specific location
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            # splitting the dataset
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=243)
            # saving in a target folder
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            # saving in a target folder
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is done!")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))