import os, sys, io
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from stt import SpeechtoText
import uvicorn
PATH = os.getcwd().split('MaCALL')[0] + 'MaCALL/'
audio_folder = os.path.join(PATH, 'audios_tmp')

app = FastAPI(title="Datametrica AI Assistant API", version="1.0.0")

stt = SpeechtoText(path_voicerecords = audio_folder)

@app.get('/')
def root():
    return {"AutoInstruct4LLMs": "AI Python Services"}

@app.post("/local_faster_whisper_transcription")
async def transcription(client_speech: UploadFile):
    if client_speech.filename.endswith(('.mp3', '.wav', '.opus')):
        transcripted_audio = await stt.get_local_faster_whisper_transcription(client_speech)
        return transcripted_audio
    else:
        raise HTTPException(status_code=400, detail="Invalid client_speech extension. Please upload a .wav file")

@app.post("/local_insanely_fast_whisper_transcription")
async def transcription(client_speech: UploadFile):
    if client_speech.filename.endswith(('.mp3', '.wav', '.opus')):
        transcripted_audio = await stt.get_local_insanely_fast_whisper_transcription(client_speech)
        return transcripted_audio
    else:
        raise HTTPException(status_code=400, detail="Invalid client_speech extension. Please upload a .wav or .mp3 file")

@app.post("/denoiser")
async def denoiser(client_speech: UploadFile):
    if client_speech.filename.endswith(('.mp3', '.wav', '.opus')):
        denoised_audio = await stt.denoise_audio(client_speech)
        return StreamingResponse(io.BytesIO(denoised_audio), media_type="audio/wav")
    else:
        raise HTTPException(status_code=400, detail="Invalid client_speech extension. Please upload a .wav or .mp3 file")


if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=5001, reload=True)
