"""Transcribe the given audio file."""
from google.cloud import speech
import io

client = speech.SpeechClient()

with io.open("/Users/matthewfrost/unfinproj/summit/S-T/audio/Hello-summit_muffled.mp3", "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

response = client.recognize(config=config, audio=audio)

print(response.results)
# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print("Transcript: {}".format(result.alternatives[0].transcript))

