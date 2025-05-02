from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_validation import DataValidation,DataValidationArtifact
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
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
          logging.info("data ingestion completed")
          logging.info("Initiated Data Validation")
          datavalidationconfig = DataValidationConfig(traininingpipelineconfig)
          data_validation = DataValidation(dataingestionartifact,datavalidationconfig)
          data_validation_artifact = data_validation.initiate_data_validation()
          logging.info("The Data Validation is complete")
          print(data_validation_artifact)
          

     except Exception as e:
          raise NetworkSecurityException(e,sys)
