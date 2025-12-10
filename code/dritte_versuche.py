from ollama import chat, ChatResponse
from data_structure import Song, SongList, SongCategory

# 1️⃣ Read and clean lyrics
with open("lyrics.txt", "r", encoding="utf-8") as f:
    lyrics = f.read()

# Remove line breaks and extra whitespace
lyrics_clean = " ".join(lyrics.split())

# 2️⃣ Create a Song instance
song = Song(
    song_id="ts_002",
    title="You Belong With Me",
    album="Fearless",
    year=2008,
    lyrics_source="manual_test",
    lyrics=lyrics_clean,
    primary_category=SongCategory.unrequited  # you can set a default for testing
)

# 3️⃣ Wrap it in a SongList
song_list = SongList(root=[song])

# 4️⃣ Prepare system prompt (telling the model the expected schema)
system_prompt = f"""
You are a person with a high school degree and no prior knowledge of Taylor Swift.
Respond according to the following JSON schema: {SongList.model_json_schema()}
"""

# 5️⃣ Send to Ollama
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

# 6️⃣ Validate Ollama response with Pydantic
try:
    song_list_from_model = SongList.model_validate_json(response.text)
    print(song_list_from_model.model_dump_json(indent=2))
except Exception as e:
    print("Validation error:", e)
    print("Raw response from Ollama:", response.text)
