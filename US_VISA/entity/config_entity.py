import os
from US_VISA.constant.constants import (
    PIPELINE_NAME, 
    ARTIFACT_DIR, 
    DATA_INGESTION_DIR_NAME, 
    DATA_INGESTION_FEATURE_STORE_DIR,
    DATA_INGESTION_INGESTED_DIR,
    DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO,
    DATA_INGESTION_COLLECTION_NAME,
    FILE_NAME,
    TRAIN_FILE_NAME,
    TEST_FILE_NAME

)
#from dotenv import load_dotenv, dotenv_values 
from dataclasses import dataclass
from datetime import datetime

TIME_STAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
#load_dotenv() 

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIME_STAMP)
    timestamp: str = TIME_STAMP

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME