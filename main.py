import whisper

model = whisper.load_model("turbo")
result = model.transcribe("./public/sample_speech_to_text.mp3")

print(result["text"])