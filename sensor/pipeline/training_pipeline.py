from sensor.logger import logging
from sensor.exception import SensorException
import sys,os
from sensor.entity import config_entity
from datetime import datetime
from sensor.utils import get_collections_as_dataframe
from sensor.components import data_ingestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer
from sensor.components.model_evaluation import ModelEvaluation
from sensor.components.model_pusher import ModelPusher


def start_training_pipeline():
     
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          # Data Ingestion
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config= training_pipeline_config)
          #print(data_ingestion_config.to_dict())
          data_ingestion = data_ingestion.DataIngestion(data_ingestion_config = data_ingestion_config)
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

          # Data Validation
          data_validation_config = config_entity.DataValidationConfig(training_pipeline_config = training_pipeline_config)
          data_validation = DataValidation(data_validation_config = data_validation_config,
                         data_ingestion_artifact = data_ingestion_artifact)

          data_validation_artifact = data_validation.initiate_data_validation()

          # Data transformation
          data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config= training_pipeline_config)
          data_transformation = DataTransformation(data_transformation_config = data_transformation_config,
                                   data_ingestion_artifact= data_ingestion_artifact)
          data_transformation_artifact = data_transformation.initiate_data_transformation()

          #Model Trainer
          model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
          model_trainer = ModelTrainer(model_trainer_config = model_trainer_config, 
                                   data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact = model_trainer.initiate_model_trainer()


          model_eval_config = config_entity.ModelEvaluationConfig(training_pipeline_config = training_pipeline_config)
          model_eval = ModelEvaluation(model_eval_config=model_eval_config,
            data_ingestion_artifact = data_ingestion_artifact,
            data_transformation_artifact = data_transformation_artifact,
            model_trainer_artifact = model_trainer_artifact)
          model_eval_artifact = model_eval.initiate_model_evaluation()
          
          # model pusher
          model_pusher_config = config_entity.ModelPusherConfig(training_pipeline_config)

          model_pusher = ModelPusher(model_pusher_config= model_pusher_config,
           data_transformation_artifact =data_transformation_artifact,
            model_trainer_artifact =model_trainer_artifact)

          model_pusher_artifact   = model_pusher.initiate_model_pusher()


     except Exception as e:
          print(e,sys)


# Mongodb_local_host_url = "mongodb://localhost:27017/neurolabDB"
          

