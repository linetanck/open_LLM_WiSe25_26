import os
import pandas as pd

df = pd.read_csv('data/classified_songs.csv')

correct = 0
for i, row in df.iterrows():
    goal_lable = row["goal_label"]
    llm_lable = row["llm_label"]
    if goal_lable == llm_lable:
        correct = correct + 1

ratio = (100/ len(df)) * correct
print(correct)
print(ratio)
