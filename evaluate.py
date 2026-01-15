import os
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


df = pd.read_csv('data/classified_songs.csv')

correct = 0
for i, row in df.iterrows():
    goal_label = row["goal_label"]
    llm_label = row["llm_label"]
    if goal_label == llm_label:
        correct = correct + 1
    #if goal_label == "unrelated to love":
        #print(llm_label)

ratio = (100/ len(df)) * correct
print(correct)
print(ratio)

# confusion matrix

y_true = df["goal_label"]
y_pred = df["llm_label"]

labels = sorted(df["goal_label"].unique())

cm = confusion_matrix(y_true, y_pred, labels=labels)
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
disp.plot(cmap="Blues", xticks_rotation=45)
plt.show()
