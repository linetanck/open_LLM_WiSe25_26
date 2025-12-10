# Read the lyrics from a file, remove line breaks, and write to a new file

# Open and read the original file
with open("data/lyrics_test.txt", "r", encoding="utf-8") as f:
    lyrics = f.read()

# Remove line breaks and extra whitespace
one_line_lyrics = " ".join(lyrics.split())

# Write the single-line lyrics to a new file
with open("data/lyrics_one_line.txt", "w", encoding="utf-8") as f:
    f.write(one_line_lyrics)

print("Lyrics have been written to lyrics_one_line.txt as a single line.")
