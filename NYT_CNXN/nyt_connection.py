"""
script for connecting to new york times api and returning connection

"""
from streamlit.connections import ExperimentalBaseConnection
from pynytimes import NYTAPI
import datetime
import json
import pandas as pd
import streamlit as st


# -----------------
def json_encoder(obj):
    # serialize json data
    if isinstance(obj, datetime.datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


def response_to_df(data):
    # convert json response string into pandas df
    jd = json.dumps(data, default=json_encoder)
    df = pd.read_json(jd)
    return df


# ------------------
class NYTDBConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs):
        return NYTAPI(st.secrets["nykey"], parse_dates=True)

    def query(self, query, **kwargs):
        cnxn = self._connect()
        res = None
        print(kwargs)
        if query == "top_stories":
            res = cnxn.top_stories()
        elif query == "most_shared":
            res = cnxn.most_shared(kwargs.get("days", 1))
        elif query == "most_viewed":
            res = cnxn.most_viewed(kwargs.get("days", 1))
        # elif query == "movie_reviews":
        #     res = cnxn.movie_reviews()
        # if res != None:

        #     res = response_to_df(res)
        return res
