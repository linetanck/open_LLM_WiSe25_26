from typing import List
from pydantic import BaseModel
from pydantic import RootModel

from enum import Enum

class SongCategory(str, Enum):
    happily_together = "happily_together"
    broken_up = "broken_up"
    longing = "longing"
    not_love_song = "not_a_love_song"
    revenge_empowerment = "revenge_empowerment"
    forbidden_love = "forbidden_love"
   

# Single song model
class Song(BaseModel):
    song_id: str
    title: str
    album: str
    year: int
    lyrics: str
    primary_category: SongCategory

# Root model for multiple songs
class SongList(RootModel):
    root: List[Song]

#testing json model
test_json = """
{
    "root": [
        {
            "song_id": "ts_002",
            "title": "You Belong With Me",
            "album": "Fearless",
            "year": 2008,
            "lyrics": "You're on the phone with your girlfriend, she's upset She's going off about something that you said 'Cause she doesn't get your humor like I do I'm in the room, it's a typical Tuesday night I'm listening to the kind of music she doesn't like And she'll never know your story like I do But she wears short skirts, I wear T-shirts She's Cheer Captain, and I'm on the bleachers Dreaming about the day when you wake up and find That what you're looking for has been here the whole time If you could see that I'm the one who understands you Been here all along, so why can't you see? You belong with me, you belong with me Walk in the streets with you in your worn-out jeans I can't help thinking this is how it ought to be Laughing on a park bench, thinking to myself "Hey, isn't this easy?" And you've got a smile that can light up this whole town I haven't seen it in a while since she brought you down You say you're fine, I know you better than that Hey, what you doing with a girl like that? She wears high heels, I wear sneakers She's Cheer Captain, and I'm on the bleachers Dreaming about the day when you wake up and find That what you're looking for has been here the whole time If you could see that I'm the one who understands you Been here all along, so why can't you see? You belong with me Standing by and waiting at your backdoor All this time how could you not know, baby? You belong with me, you belong with me Oh, I remember you driving to my house in the middle of the night I'm the one who makes you laugh when you know you're 'bout to cry I know your favorite songs and you tell me 'bout your dreams Think I know where you belong, think I know it's with me Can't you see that I'm the one who understands you? Been here all along, so why can't you see? You belong with me Standing by and waiting at your backdoor All this time how could you not know, baby? You belong with me, you belong with me You belong with me Have you ever thought, just maybe You belong with me? You belong with me",
            "primary_category": "unrequited"
        }
    ]
}
"""
song_list_from_model = SongList.model_validate_json(test_json)
print(song_list_from_model)
