import os
import sys
import numpy as np
import pandas as pd
"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"



"""
Data Ingestion related contetn satrting with Data_Ingestion var name
"""

DATA_INGESTION_COLLECTION_NAME ="NetworkData"
DATA_INGESTION_DATABASE_NAME = "lokesh"
DATA_INGESTION_DIR_NAME= "data_ingestion"
DATA_INGESTION_FEATURE_STORE_NAME = "feature_store"
DATA_INGESTION_INGESTED_DIR_NAME = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO_NAME :float = 0.2
