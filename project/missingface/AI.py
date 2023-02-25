import os 
import requests
import json
import pickle
from collections import defaultdict
import pandas as pd 
import numpy as np 
def get_user_submitted_data(status = "NR"):
  url = "http://localhost:8000/user_submission"
  try:
    result = requests.get(url)
    if result.status_code == 200:
      result = json.loads(result.text)
      d1=pd.Dataframe(result, columns=["label","face_encoding"])
      d2=pd.Dataframe(
        d1.pop("face_encoding"),values.tolist(), index=d1.index
      ).rename(columns= lambda x: "fe_{}".formate(x + 1))
      df = d1.join(d2)
      return df
  expect Expectation as e:
  return None


def match():
  model_name = "classifier.pkl"
  matched_image - defaultdict(list)
  user_submission_df = get_user_submitted_data()

  if user_submission