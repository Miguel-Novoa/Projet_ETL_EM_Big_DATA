from pandas import DataFrame
import pandas as pd
import sys

# If you are not able to import constant py file use below code
sys.path.insert(1, 'etl_pandas\metadata')
from constant import connection



def load(type: str, df: DataFrame, target: str):
    # Load the data based on type
    '''
    :param type: Input Storage type (db|csv) Based on type data stored in MySQL or FileSystem
    :param df: Input Dataframe
    :param target: Input target -For filesystem - Location where to store the data           
                                -For MySQL - table name
    '''

    # Write data on mysql database with table name
    if type=="db":
       df.to_sql(target, con=connection(), if_exists='replace', index=False)
       print("Data succesfully loaded to MySQL Database !!")

    if type=="csv":
    # Write data on filesystem
      df.to_csv(target, index=False)
      print("Data succesfully loaded to filesystem !!")