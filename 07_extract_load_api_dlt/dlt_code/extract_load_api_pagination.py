#========================================#
#                                        #
#    This script loads job ads with      #
#    the keyword "data" with pagination  #
#    to load more job ads                #
#                                        #
#========================================#


import dlt
import requests
import json
from pathlib import Path
import os


def _get_ads(url_for_search, params):
    headers = {"accept": "application/json"}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode("utf8"))


@dlt.resource(write_disposition="append")
def jobads_resource(params):

    url = "https://jobsearch.api.jobtechdev.se"
    url_for_search = f"{url}/search"
    limit = params.get("limit", 100)
    offset = 0

    while True:
        # build this page’s params
        page_params = dict(params, offset=offset)
        data = _get_ads(url_for_search, page_params)

        # stop if there is no more result
        hits = data.get("hits", [])
        if not hits:
            break

        # yield each ad on this page
        for ad in hits:
            yield ad

        # if fewer than a full page was returned, we’re done
        if len(hits) < limit or offset > 1900:
            break

        offset += limit


@dlt.source
def jobads_source(params):
    return jobads_resource(params)


def run_pipeline(query, table_name):
    pipeline = dlt.pipeline(
        pipeline_name="jobsearch",
        destination="snowflake",
        dataset_name="staging",
    )

    params = {"q": query, "limit": 100}

    load_info = pipeline.run(jobads_source(params=params), table_name=table_name)
    print(load_info)


if __name__ == "__main__":
    working_directory = Path(__file__).parent
    os.chdir(working_directory)

    query = "data"
    table_name = "data_field_job_ads"

    run_pipeline(query, table_name)
