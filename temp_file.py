import os

PATH = os.getcwd().split('WhispersAPI')[0] + 'WhispersAPI/'
temp_audio_folder = os.path.join(PATH, 'audios_tmp/')

async def create_temp_audio(audio, filename) -> str:
    temp_audio_path = temp_audio_folder + filename
    with open(temp_audio_path, 'wb') as temp_audio:
        temp_audio.write(await audio.read())
    return temp_audio_path

def delete_temp_audio(filename):
    temp_audio_path = temp_audio_folder + filename
    os.remove(temp_audio_path)