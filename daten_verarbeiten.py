import os
import pandas as pd

dictionary = {}

directory = ["data/Red", "data/Lover"]

for folder in directory:

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
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


df = pd.DataFrame(list(dictionary.items()), columns=["filename", "lyrics"])

# creating two new columns for the lables

df["goal_label"] = ""

# add lables
df.loc[0, "goal_label"] = "unrelated to love"
df.loc[1, "goal_label"] = "broken up"
df.loc[2, "goal_label"] = "happily in love"
df.loc[3, "goal_label"] = "yearning"
df.loc[4, "goal_label"] = "happily in love"
df.loc[5, "goal_label"] = "revenge empowerment"
df.loc[6, "goal_label"] = "happily in love"
df.loc[7, "goal_label"] = "yearning"
df.loc[8, "goal_label"] = "revenge empowerment"
df.loc[9, "goal_label"] = "yearning"
df.loc[10, "goal_label"] = "broken up"
df.loc[11, "goal_label"] = "happily in love"
df.loc[12, "goal_label"] = "happily in love"
df.loc[13, "goal_label"] = "happily in love"
df.loc[14, "goal_label"] = "yearning"
df.loc[15, "goal_label"] = "unrelated to love"
df.loc[16, "goal_label"] = "yearning"
df.loc[17, "goal_label"] = "forbidden love" 
df.loc[18, "goal_label"] = "broken up"

# Ab hier lover
df.loc[19, "goal_label"] = "forbidden love"
df.loc[20, "goal_label"] = "happily in love"
df.loc[21, "goal_label"] = "yearning"
df.loc[22, "goal_label"] = "yearning"
df.loc[23, "goal_label"] = "broken up"
df.loc[24, "goal_label"] = "forbidden love"
df.loc[25, "goal_label"] = "broken up" # I forgot that you existed



#print(df.tail())

