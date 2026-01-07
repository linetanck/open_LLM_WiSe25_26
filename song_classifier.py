# virtual evironment heißt llmsprojekt

from ollama import chat
from ollama import ChatResponse
import pandas as pd

df = pd.read_csv('data/annotated_songs.csv')

system_prompt = f'You are a Person with a high school degree and have no previous knowledge of Taylor Swift.'

def classify_lyrics(row):
    lyrics = row["lyrics"]
    response: ChatResponse = chat(
        model='llama3.2:3b',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f"""
            You are a strict song lyrics classifier.

            Choose EXACTLY ONE label from this list:
            happily in love
            broken up
            yearning
            revenge empowerment
            forbidden love
            unrelated to love

            Decision rules (follow in order):
            1. If the lyrics are NOT mainly about romantic love → unrelated to love
            2. If they express anger or moving on after being hurt → revenge empowerment
            3. If a relationship has ended or is ending → broken up
            4. If the singer wants someone they are NOT with (distance, unrequited, waiting, missing) → yearning
            5. If the love must be hidden or is socially forbidden → forbidden love
            6. If the relationship is mutual, happy, and ongoing or the lyrics express being happily in love → happily in love

            First, silently analyze the lyrics.
            Then output ONLY the label.
            No explanation. No punctuation.
                        
            Lyrics: {lyrics}"""},
        ],
        options={
        "temperature": 0.4,
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

