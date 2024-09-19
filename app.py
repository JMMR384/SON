import os
import openai
from dotenv import load_dotenv
import flask

load_dotenv()
openai.api_key = os.getenv()

app= Flask (__name__)
@app.route('/')
def index():
    return render_template("recorder")
def audio():
    audio = request.files.get("audio")
    audio.save("audio.mp3")
    transcribe = openai.Audio.transcribe("Whisper-1", audio_file)
    return {"result": "ok", "text": transcribe.text}

