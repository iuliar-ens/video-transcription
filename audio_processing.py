import subprocess
import os
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from text_processing import speech_to_text
from pydub import AudioSegment

def generate_wav_file(file, wav_file_path):
    ffmpeg_command = ['ffmpeg', '-i', file, '-ar', '16000', '-ac', '1', '-async', '1', wav_file_path]
    try:
        subprocess.run(ffmpeg_command, stderr=subprocess.DEVNULL, check=True) #remove stderr=subprocess.DEVNULL to see logs
    except Exception as ex:
        print(f"An error occured when using ffmpeg: {ex}")

def convert_mp3_to_wav(mp3_file_path):
    wav_file_path = os.path.splitext(mp3_file_path)[0] + '.wav'
    ffmpeg_command = ['ffmpeg', '-i', mp3_file_path, wav_file_path]

    try:
        subprocess.run(ffmpeg_command, check=True)
        return wav_file_path  
    except Exception as ex:
        print(f"Error converting MP3 to WAV: {ex}")
        return None