import io
import requests
import pandas as pd
from sqlalchemy import create_engine

global file_directory
file_directory = "./data"

def run_pipeline(data_url, table_name):

    table = fetch_process_data(data_url)
    save_to_sql(table, table_name)

def fetch_process_data(url):

    dataframe = None

    try:
        response = requests.get(url).content
        dataframe = pd.read_csv(io.StringIO(response.decode('utf-8')))
        dataframe = dataframe.dropna()
    except Exception as e:
        print(f"Error: {e}")
    
    return dataframe

def save_to_sql(table, table_name):

    if table is not None:
        table_path = f"{file_directory}/{table_name}.db"
        engine = create_engine(f'sqlite:///{table_path}')
        table.to_sql(table_name, con=engine, if_exists='replace', index=False)
    else:
        print("Error: Table is empty")


data_sources = {
    "surface_temperature": "https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv",
    "land_cover": "https://opendata.arcgis.com/datasets/b1e6c0ea281f47b285addae0cbb28f4b_0.csv"
}

for table_name, url in data_sources.items():
    run_pipeline(url, table_name)

