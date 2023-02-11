"""The file contains function that 
loads data into the database"""

import pandas as pd
import sqlite3

def load_data(database_location:str, data_location:str):
    """database_location: Relative path to the file script
                            location
        data_location: full path to the data_location"""
    conn = sqlite3.connect(f'sqlite:///{database_location}')
    dataframe = pd.read_csv(data_location)
    dataframe.to_sql('bikers_table',conn,
                     if_exists='append',index=False)
    print('import completed')

