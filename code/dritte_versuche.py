from ollama import chat, ChatResponse
from data_structure import Song, SongList, SongCategory

with open("lyrics.txt", "r", encoding="utf-8") as f:
    lyrics = f.read()

# Remove line breaks and extra whitespace
lyrics_clean = " ".join(lyrics.split())

song = Song(
    song_id="ts_002",
    title="You Belong With Me",
    album="Fearless",
    year=2008,
    lyrics_source="manual_test",
    lyrics=lyrics_clean,
    primary_category=SongCategory.unrequited  # you can set a default for testing
)

song_list = SongList(root=[song])

system_prompt = f"""
You are a person with a high school degree and no prior knowledge of Taylor Swift.
Respond according to the following JSON schema: {SongList.model_json_schema()}
"""

response: ChatResponse = chat(
    model="llama3.2:3b",
    format=SongList.model_json_schema(),  # ensures Ollama outputs matching JSON
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": f"Using the lyrics provided, categorize the song:\n{lyrics_clean}"
        }
    ]
)

try:
    song_list_from_model = SongList.model_validate_json(response.text)
    print(song_list_from_model.model_dump_json(indent=2))
except Exception as e:
    print("Validation error:", e)
    print("Raw response from Ollama:", response.text)
