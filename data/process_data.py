import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    
    messages = pd.read_csv('disaster_messages.csv')
    categories = pd.read_csv('disaster_categories.csv')
    df = pd.merge(messages,categories,on = 'id',how = 'inner')
    
    return df

def clean_data(df):
    
    '''
    INPUT
    df - a pandas dataframe resulted from 2 data source
    
    OUTPUT
    df - a pandas dataframe after cleaning and transforming
    '''
    category_name = df.categories.str.split(";", expand=True).loc[1,:].apply(lambda x: x[:-2])
    df_category = df.categories.str.split(";", expand=True)
    df_category.columns = category_name
    df_category = df_category.applymap(lambda x: x[-1:])
    cols = df_category.columns
    df_category[cols] = df_category[cols].apply(pd.to_numeric, errors='coerce', axis=1)
    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df, df_category], axis=1)
    df['related'] = df['related'].apply(lambda x: 1 if x not in ['1', '0', 1, 0] else x)
    df = df.drop_duplicates()
    return df


def save_data(df, database_filename):
    
    engine = create_engine('sqlite:///DisasterResponse_project.db')
    df.to_sql('messages_table', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()