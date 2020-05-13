# Disaster-Response-Pipeline-ETL-ML
This repostry contains the files related to my project Disaster Resposnse Pipeline for ETL & ML


### Introduction

This project is done under the Udacity Data Science Nano Degree.
The goal of this project is to classify different messages, that people in a distress during any disaster might send, into proper classes for easy support and help can be planned and assisted.

### Installation

The code should run with no issues using Python versions 3.*

Run the following commands in the project's root directory to set up your database and model.

To run ETL pipeline that cleans data and stores in database 

 - Run python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db


To run ML pipeline that trains classifier and saves 

- Run python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl.


Run the following command in the app's directory to run your web app. 

 - Run python run.py and Go to http://0.0.0.0:3001/

### Licensing and Acknowledgements

This data set used for training is provided by [Figure Eight](https://appen.com/datasets/combined-disaster-response-data/).
