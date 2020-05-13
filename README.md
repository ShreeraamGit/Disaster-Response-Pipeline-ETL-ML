# Disaster-Response-Pipeline-ETL-ML
This repostry contains the files related to my project Disaster Resposnse Pipeline for ETL & ML


### Introduction

The goal of this project is to classify different messages, that people in a distress during any disaster might send, into proper classes for easy support and help can be planned and assisted. And also i have designed a Web Page to Classify the Messages which also shows the overview of the training Dataset

### Installation

The code should run with no issues using Python versions 3.* 

Special mention should be made as this project handles a lot of codes that deal with human language data, i would recommend NLTK libarary. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries.

### NLTK requires Python versions 3.5, 3.6, 3.7, or 3.8.

### MAC/LINUX users 

### Install NLTK: run pip install --user -U nltk

Run the following commands in the project's root directory to set up your database and model.

To run ETL pipeline that cleans data and stores in database 

 - Run python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db


To run ML pipeline that trains classifier and saves 

- Run python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl.


Run the following command in the app's directory to run your web app. 

 - Run python run.py and Go to http://0.0.0.0:3001/

### Licensing and Acknowledgements

This data set used for training is provided by [Figure Eight](https://appen.com/datasets/combined-disaster-response-data/).
