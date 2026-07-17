import dlt
import pandas as pd
from pathlib import Path
import os


#extract data manually from source, in this case a local csv file
def csv_data(file_path, **kwargs):
    df = pd.read_csv(file_path, **kwargs)
    return df


if __name__ == "__main__":
    #need to change to current working directory as this is where
    # dlt looks for .dlt and when using the play button in vscode
    # it will run from where you are in the terminal, not neccessarily
    # where this script is resided
    working_directory = Path(__file__).parent

    #if you are using files from .dlt, 
    # the working directory should be the direct parent of .dlt folder
    os.chdir(working_directory)
    csv_path = working_directory / "data" / "NetflixOriginals.csv"
    data = csv_data(csv_path, encoding="latin1")

    pipeline = dlt.pipeline(
        pipeline_name='movies',
        destination="snowflake",
        dataset_name='staging'
        )
    
    load_info = pipeline.run(data, table_name="netflix")

    # pretty print the information on data that was loaded
    print(f"Loading information: {load_info}")
          

