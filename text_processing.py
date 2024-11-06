from gtts import gTTS
import subprocess

def speech_to_text(output_txt_path, wav_file_path, folder, whisper_folder):
    whisper_command = ['./main', '-f', wav_file_path, '-l', 'ru', '-m', 'models/ggml-large-v3.bin']    
    try:
        with open(output_txt_path, 'w') as output_file:
            subprocess.run(whisper_command, stdout=output_file, stderr=subprocess.DEVNULL, check=True, cwd=whisper_folder) #remove stderr=subprocess.DEVNULL to see logs
    except Exception as ex:
        print(f"An error occurred when using whisper: {ex}")
    

def text_to_speech(audio_file_path, translated_text_without_timestamps):
    tts = gTTS(text=translated_text_without_timestamps, lang="en")
    tts.save(audio_file_path)
