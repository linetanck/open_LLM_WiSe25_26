# virtual evironment heißt llmsprojekt

from ollama import chat
from ollama import ChatResponse
from daten_verarbeiten import test_df

lyrics = """You're on the phone with your girlfriend, she's upset She's going off about something that you said 'Cause she doesn't get your humor like I do I'm in the room, it's a typical Tuesday night I'm listening to the kind of music she doesn't like And she'll never know your story like I do But she wears short skirts, I wear T-shirts She's Cheer Captain, and I'm on the bleachers Dreaming about the day when you wake up and find That what you're looking for has been here the whole time If you could see that I'm the one who understands you Been here all along, so why can't you see? You belong with me, you belong with me Walk in the streets with you in your worn-out jeans I can't help thinking this is how it ought to be Laughing on a park bench, thinking to myself "Hey, isn't this easy?" And you've got a smile that can light up this whole town I haven't seen it in a while since she brought you down You say you're fine, I know you better than that Hey, what you doing with a girl like that? She wears high heels, I wear sneakers She's Cheer Captain, and I'm on the bleachers Dreaming about the day when you wake up and find That what you're looking for has been here the whole time If you could see that I'm the one who understands you Been here all along, so why can't you see? You belong with me Standing by and waiting at your backdoor All this time how could you not know, baby? You belong with me, you belong with me Oh, I remember you driving to my house in the middle of the night I'm the one who makes you laugh when you know you're 'bout to cry I know your favorite songs and you tell me 'bout your dreams Think I know where you belong, think I know it's with me Can't you see that I'm the one who understands you? Been here all along, so why can't you see? You belong with me Standing by and waiting at your backdoor All this time how could you not know, baby? You belong with me, you belong with me You belong with me Have you ever thought, just maybe You belong with me? You belong with me"""
system_prompt = f'You are a Person with a high school degree and have no previous knowledge of Taylor Swift.'
categories = "happily in love, broken_up, longing, revenge empowerment, forbidden love and not a love song"

response: ChatResponse = chat(model='llama3.2:3b', 
                              messages=[
    
    {'role': 'system', 'content': system_prompt},
    {'role': 'user','content': f'Using the lyrics provided, please give the song one of the following love-related categories: {categories}. Only answer with the category. The lyrics are: {lyrics}.'},
])


print(response.message.content)
