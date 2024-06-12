import os
import pandas as pd
from sqlalchemy import create_engine

# Path where the databases should be
file_directory = "../data"

# Test data sources, mimicking the actual data pipeline inputs but could be mocked or smaller datasets
test_data_sources = {
    "surface_temperature": "https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv",
    "land_cover": "https://opendata.arcgis.com/datasets/b1e6c0ea281f47b285addae0cbb28f4b_0.csv"
}

def test_pipeline_execution():
    from pipeline import run_pipeline  # Import your pipeline function

    for table_name, url in test_data_sources.items():
        run_pipeline(url, table_name)
        db_path = f"{file_directory}/{table_name}.db"
        assert os.path.exists(db_path), f"Database file for {table_name} does not exist."

        engine = create_engine(f'sqlite:///{db_path}')
        df = pd.read_sql_table(table_name, con=engine)
        assert not df.empty, f"Database {table_name} is empty."

if __name__ == "__main__":
    test_pipeline_execution()
