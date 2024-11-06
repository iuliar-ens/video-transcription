# Video Translation Tool

A Python-based tool that automatically translates videos from Russian to English. The tool extracts audio, transcribes speech, translates the text, generates new audio, and creates a new video with translated audio while preserving the original video content.

## Features

- 🎥 Processes MP4 video files
- 🗣️ Extracts and transcribes Russian audio using whisper.cpp
- 🔄 Translates Russian text to English using Google Translate
- 🔊 Generates natural-sounding English audio using gTTS
- 🎬 Creates a new video file with translated audio

## Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system
- whisper.cpp compiled and ready to use
- Git (for cloning the repository)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/iuliar-ens/video-transcription
cd video-transcription
```

2. Install required Python packages:
```bash
pip install pydub deep-translator gTTS
```

3. Install FFmpeg:
- **Linux**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **macOS**:
  ```bash
  brew install ffmpeg
  ```
- **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html)

4. Set up whisper.cpp:
   - Follow the installation instructions at [whisper.cpp repository](https://github.com/ggerganov/whisper.cpp)
   - Download the required model (ggml-large-v3.bin)
   - Note the path to your whisper.cpp installation

## Configuration

Edit `main.py` and set the following paths:
```python
root_folder = os.path.expanduser('path/to/your/videos')
whisper_folder = os.path.expanduser('path/to/whisper.cpp/directory')
```

## Usage

1. Place your Russian MP4 video files in the specified root folder

2. Run the translation tool:
```bash
python main.py
```

3. The tool will process each video and create:
   - A new folder for each video containing intermediate files
   - A new MP4 file with "_translated" suffix containing the English audio

## Project Structure

```
video-transcription/
├── main.py                 # Main execution script
├── audio_processing.py     # Audio extraction and conversion
├── text_processing.py      # Speech-to-text and text-to-speech
├── translator.py           # Text translation functionality
└── utils.py               # Utility functions
```

## How It Works

1. **Audio Extraction**: Extracts audio from the input video and converts it to WAV format
2. **Speech Recognition**: Uses whisper.cpp to transcribe Russian speech to text
3. **Translation**: Translates the transcribed text from Russian to English
4. **Audio Generation**: Creates English audio from the translated text
5. **Video Creation**: Combines the original video with the new English audio

## Limitations

- Requires local installation of whisper.cpp
- Processing time depends on video length and system capabilities
- Audio synchronization might not be perfect for all videos

## Acknowledgments

- [whisper.cpp](https://github.com/ggerganov/whisper.cpp) for speech recognition
- Google Translate API for translation
- gTTS (Google Text-to-Speech) for audio generation