import sys

from US_VISA.exception.exception import USvisaException
from US_VISA.logger.logger import logging

import os
from US_VISA.constant.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, dotenv_values 
#import certifi

#ca = certifi.where()
load_dotenv(r'C:\Users\Amit\Desktop\Amit\US_VISA_PREDICTION\US_VISA_PREDICTION\.env')

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv("MONGODB_URL_KEY")
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, server_api=ServerApi('1'))
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise USvisaException(e,sys)