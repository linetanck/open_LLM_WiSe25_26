import os
import pandas as pd

dictionary = {}

directory = "data/Red"

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            key = filename[:-4]
            content = content.split(sep = "\n")
            content[-1] = content[-1][:-7]
            bereinigt = []
            for j in content:
                if "]" in j:
                    pass
                else:
                    bereinigt.append(j)
            bereinigt = " ".join(bereinigt)   
            dictionary[key]= bereinigt


df = pd.DataFrame.from_dict(dictionary, orient="index", columns=["content"])
df.index.name = "filename"

df["label"] = ""


print(df.head())

