import os
import sys 
from src.logger import logging 
from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer

if __name__ == '__main__': 
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initate_data_transformation(train_path=train_data_path, test_path=test_data_path)
    model_trainer = ModelTrainer()
    model_trainer.initate_model_training(train_arr, test_arr)
