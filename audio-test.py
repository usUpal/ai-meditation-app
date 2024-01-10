# edge-playback --volume=-80%  -v "en-GB-RyanNeural" --text "I took the evening to work more on my business and work on my personal goals."

from pydub import AudioSegment

# from pydub.generators import silence

# Load the generated MP3 file
generated_audio = AudioSegment.from_mp3("hello_with_rate_halved.mp3")

# Load the second MP3 file you want to play at a lower volume
other_audio = AudioSegment.from_mp3("melodic.mp3")

# Adjust the volume of the second audio file (lower by 10 dB, for example)
other_audio = other_audio - 30

# Set the starting point of the overlay (adjust as needed)
overlay_start_time = 0  # Start overlay from the beginning

# Overlay the two audio files
combined_audio = generated_audio.overlay(other_audio, position=overlay_start_time)

# Export the result to a new MP3 file
combined_audio.export("combined_output.mp3", format="mp3")
print("done")
