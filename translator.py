from deep_translator import GoogleTranslator

def translate_text_in_chunks(text, chunk_size=4000):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    translated_text = ''
   
    for chunk in chunks:
        print(chunk)
        translated_chunk = GoogleTranslator(source='ru', target='en').translate(chunk)
        translated_text += translated_chunk 
    return translated_text


def translate_file(output_txt_path):
    try:
        with open(output_txt_path, 'r', encoding='utf-8') as file:
            russian_text = file.read()             
        translated_text_with_timestamps = translate_text_in_chunks(russian_text)
        translated_output_path_with_timestamps = output_txt_path.replace('.txt', '_translated.txt')
   
        with open(translated_output_path_with_timestamps, 'w', encoding='utf-8') as file:
            file.write(translated_text_with_timestamps)
        
        return translated_text_with_timestamps
        

    except Exception as ex:
            print(f"An error occured when translating: {ex}")

