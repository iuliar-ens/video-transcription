import os
import glob
import subprocess

from utils import remove_timestamps
from text_processing import speech_to_text, text_to_speech
from translator import translate_file
from audio_processing import generate_wav_file, convert_mp3_to_wav

def replace_audio_in_video(original_video_path, new_audio_path, output_mp4_path):
    ffmpeg_command = [
        'ffmpeg', 
        '-i', original_video_path,  
        '-i', new_audio_path,       
        '-c:v', 'copy',              
        '-map', '0:v:0',            
        '-map', '1:a:0',             
        output_mp4_path              
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
    except Exception as ex:
        print(f"An error occurred while replacing audio in video: {ex}")
    
def main(root_folder, whisper_folder):
    for folder, subfolders, files in os.walk(root_folder):
        mp4_files = glob.glob(os.path.join(folder, '*.mp4'))
        
        if mp4_files:
            for file in mp4_files:
                mp4_file_name = os.path.basename(file)
                
                #create new folder where to store processed files
                new_folder_name = os.path.splitext(mp4_file_name)[0] 
                new_folder_path = os.path.join(folder, new_folder_name)
                os.makedirs(new_folder_path, exist_ok=True)

                print("--- ORIGINAL AUDIO START ---")
                #original audio
                wav_file_name = os.path.splitext(mp4_file_name)[0] + '.wav'
                wav_file_path = os.path.join(new_folder_path, wav_file_name) 
                generate_wav_file(file, wav_file_path) #generate wav file from original audio
                print("--- ORIGINAL AUDIO END ---")

                print("--- ORIGINAL TEXT START ---")
                #original text
                output_txt_name = os.path.splitext(mp4_file_name)[0] + '.txt'
                output_txt_path = os.path.join(new_folder_path, output_txt_name) 
                speech_to_text(output_txt_path, wav_file_path, new_folder_path, whisper_folder) #convert original audio to text
                print("--- ORIGINAL TEXT END ---")

                print("--- TRANSLATE TEXT START ---")
                #translate text
                translated_text_with_timestamps = translate_file(output_txt_path) #translate original text keeping the timestamps
                translated_text_without_timestamps = remove_timestamps(translated_text_with_timestamps) #remove timestamps from translated text
                print("--- TRANSLATE TEXT END ---")

                print("--- TTS START ---")
                #text to speech from translated text
                audio_file_path = output_txt_path.replace('.txt', '_translated.mp3')
                text_to_speech(audio_file_path, translated_text_without_timestamps) #generate audio file from translated text
                print("--- TTS END ---")

                #replace original audio from video with the translated one
                translated_wav_path = convert_mp3_to_wav(audio_file_path)
                translated_mp4_path = os.path.splitext(file)[0] + '_translated.mp4'
                replace_audio_in_video(file, translated_wav_path, translated_mp4_path)

                print(f"DONE PROCESSING {mp4_file_name}")

if __name__ == "__main__":
    root_folder = os.path.expanduser('path to root folder')
    whisper_folder =  os.path.expanduser('path to whisper folder')
    
    main(root_folder, whisper_folder)
