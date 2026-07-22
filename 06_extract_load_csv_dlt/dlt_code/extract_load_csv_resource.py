import dlt
import pandas as pd
from pathlib import Path
import os


# with dlt resource decorator, use the combination of write disposition and strategy to handle different use cases of data loading
@dlt.resource(write_disposition="replace") # for full loading
#@dlt.resource(primary_key="Title", write_disposition="merge") # for incremental loading
#@dlt.resource(primary_key="Title", write_disposition={"disposition": "merge", "strategy": "scd2",},) # for scd2 strategy
#@dlt.resource(schema_contract={"columns": "evolve"}) # for schema evolution
def load_csv_resource(file_path: str, **kwargs):
    df = pd.read_csv(file_path, **kwargs)
    yield df


if __name__ == "__main__":
    #need to change to current working directory as this is where
    # dlt looks for .dlt and when using the play button in vscode
    # it will run from where you are in the terminal, not neccessarily
    # where this script is resided
    working_directory = Path(__file__).parent

    #if you are using files from .dlt, 
    # the working directory should be the direct parent of .dlt folder
    os.chdir(working_directory)
    csv_path = working_directory / "data" / "movies_original.csv" # update with different 
    data = load_csv_resource(csv_path, encoding="latin1")

    pipeline = dlt.pipeline(
        pipeline_name='movies',
        destination="snowflake",
        dataset_name='staging',
        #progress="log"
        )
    
    load_info = pipeline.run(data, table_name="netflix")

    # pretty print the information on data that was loaded
    print(load_info)