import pandas as pd
import random

df = pd.read_csv('data/annotated_songs.csv')

labels =["happily in love", "broken up", "yearning", "revenge empowerment", "forbidden love", "unrelated to love"]

number = 0
for i in range(200):
    new_column = []
    for i, row in df.iterrows():
        new_column.append(labels[random.randint(0, 5)])

    df["random_label"] = new_column

    correct = 0
    for i, row in df.iterrows():
        goal_label = row["goal_label"]
        random_label = row["random_label"]
        if goal_label == random_label:
            correct = correct + 1


    ratio = (100/ len(df)) * correct
    number = number + ratio

average = number / 200

print(average)

