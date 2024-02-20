#transform.py --> transformation pour chaques fichiers

from pandas import DataFrame


def rename_cols(df: DataFrame, mapping_dict: dict) ->DataFrame:
    # Rename all the columns
    '''
    :param df: input dataframe
    :param mapping_dict: dict of columns names
    :return: ouput dataframe
    '''

    df.rename(columns=mapping_dict,inplace=True)
    return df



def specific_cols(df: DataFrame, specific_cols: list):
    # get specific cols df
    '''
    :param df: input dataframe
    :param specific_cols: list of columns names
    :return: ouput dataframe
    '''
    return df[specific_cols]



def join_df(left_df: DataFrame, right_df: DataFrame, ON_COLUMNS:list, JOIN_TYPE: str)->DataFrame:
    # Join two dataframes
    '''
    :param left_df: input dataframe
    :param right_df: input dataframe
    :param ON_COLUMNS: list of columns to perform join
    :param JOIN_TYPE: Join type
    :return: ouput dataframe
    '''
    output_df=left_df.merge(right_df, on=ON_COLUMNS, how=JOIN_TYPE)
    return output_df