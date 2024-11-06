import re

def remove_timestamps(translated_text):
    # Regular expression to match timestamps in the format [00:01:09.780 --> 00:01:11.840]
    return re.sub(r'\[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]\s*', '', translated_text)
