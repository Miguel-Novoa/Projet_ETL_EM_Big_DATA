import json
import sys

sys.path.insert(1, 'etl_pandas\metadata')

from constant import connection
import pandas as pd

def extract(type: str, source: str):
    if type=="db":
       output_df = pd.read_sql(f'SELECT * FROM {source}', con=connection())
    if type=="csv":
       output_df = pd.read_csv(source)
    elif type == "html":
        output_df = pd.read_html(source)
    elif type == "json":
        with open(source, 'r') as f:
            data = json.load(f)
        output_df = pd.DataFrame(data)
    else:
        raise ValueError("Type de données non pris en charge")
    return output_df