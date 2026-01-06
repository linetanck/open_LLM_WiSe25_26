# virtual evironment heißt llmsprojekt

from ollama import chat
from ollama import ChatResponse
from daten_verarbeiten import test_df
import pandas as pd

system_prompt = f'You are a Person with a high school degree and have no previous knowledge of Taylor Swift.'
categories = "happily in love, broken up, longing, revenge empowerment, forbidden love and not a love song"

for index, row in test_df.iterrows():
    lyrics = row["lyrics"]
    response: ChatResponse = chat(model='llama3.2:3b', 
                                 messages=[
    
        {'role': 'system', 'content': system_prompt},
        {'role': 'user','content': f'Using the lyrics provided, please give the song one of the following love-related categories: {categories}. Only answer with the category. The lyrics are: {lyrics}.'},
    ])
    
    test_df.loc[index, "llm_lable"] = response.message.content

print(test_df.head())
