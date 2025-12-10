# virtual evironment heißt llmsprojekt

from ollama import chat
from ollama import ChatResponse
from data_structure import SongCategory, Song, SongList
system_prompt = f'You are a Person with a high school degree and have no previous knowledge of Taylor Swift. Respond according to the following JSON schema: {SongList.model_json_schema()}'

response: ChatResponse = chat(model='llama3.2:3b', 
                              format=SongList.model_json_schema(), 
                              messages=[
    
    {'role': 'system', 'content': system_prompt},
    {'role': 'user','content': f'Using the lyrics provided, please give the song one of the following love-related categories: '},
])



print(response.text)
