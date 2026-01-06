# virtual evironment heißt llmsprojekt

from ollama import chat
from ollama import ChatResponse
from daten_verarbeiten import df
import pandas as pd

system_prompt = f'You are a Person with a high school degree and have no previous knowledge of Taylor Swift.'

def classify_lyrics(row):
    lyrics = row["lyrics"]
    response: ChatResponse = chat(
        model='llama3.2:3b',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f"""
            You are a classifier.

            Allowed labels (choose exactly ONE):

            happily in love
            - the singer is in a mutual, positive relationship

            broken up
            - the relationship has ended or is ending

            yearning
            - the singer wants someone they are NOT with (distance, unrequited love, waiting)

            revenge empowerment
            - anger, revenge, or self-empowerment after hurt

            forbidden love
            - love that must be hidden or is socially blocked

            unrelated to love
            - love is not the main theme

            Rules:
            - Output exactly ONE label
            - No explanation
            - No punctuation
            Lyrics: {lyrics}."""},
        ],
        options={
        "temperature": 0.2,
        "num_ctx": 1024,     # limits context window
        "num_predict": 5,    # short output
        },
        keep_alive="10m"
    )

    VALID_LABELS = {
    "happily in love",
    "broken up",
    "yearning",
    "revenge empowerment",
    "forbidden love",
    "unrelated to love",
    }

    label = response.message.content.strip().lower()

    return label if label in VALID_LABELS else "invalid"

labels = []

for i, row in df.iterrows():
    label = classify_lyrics(row)
    labels.append(label)

    # Progress output (and gives you a natural pause)
    if i % 5 == 0:
        print(f"Processed {i}/{len(df)} songs")

df["llm_label"] = labels

filepath_df = "data/classified_songs.csv"
df.to_csv(filepath_df, index=False, encoding="utf-8")

print(df.head())
print(df["llm_label"].value_counts())
