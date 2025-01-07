import requests
from config import ELEVENLABS_API_KEY, ELEVENLABS_API_URL, AUDIO_DIR
import os

def text_to_audio(script, output_file):
    url = ELEVENLABS_API_URL
    querystring = {"output_format":"mp3_44100_128"} #dHZt8yoqTSDwjElzgqey
    payload = {
        "text": script,
        "voice_settings": {
            "stability": 0.3, #0.3 #0.5
            "similarity_boost": 1.0, #1.0 #0.75
            "style": 0.9, #0.9 #0.5
            "use_speaker_boost": True
        },
        "model_id": "eleven_multilingual_v2"
    }
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    os.makedirs(AUDIO_DIR, exist_ok=True)
    with open(output_file, "wb") as f:
        f.write(response.content)
    print(f"Audio saved to {output_file}")

    return output_file
