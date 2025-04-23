from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys
if __name__ == "__main__":
     try :
          traininingpipelineconfig = TrainingPipelineConfig()
          dataingestionconfig = DataIngestionConfig(traininingpipelineconfig)

          data_ingestion = DataIngestion(dataingestionconfig)
          logging.info("Initiating the data ingestion")
          dataingestionartifact = data_ingestion.initiate_data_ingetsion()
          print(dataingestionartifact)
     except Exception as e:
          raise NetworkSecurityException(e,sys)
