from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
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
          logging.info("Data Transformation has been initiated")
          data_transformation_config=DataTransformationConfig(traininingpipelineconfig)
          data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)

          data_transformation_artifact = data_transformation.initiate_data_transformation()
          print(data_transformation_artifact)
          logging.info("Data Transformation has been completed")
          
          logging.info("Model Training stared")
          model_trainer_config=ModelTrainerConfig(traininingpipelineconfig)
          model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact=model_trainer.initiate_model_trainer()

          logging.info("Model Training artifact created")

     except Exception as e:
          raise NetworkSecurityException(e,sys)
