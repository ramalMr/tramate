import pandas as pd
import stable_whisper
from pydub import AudioSegment
from IPython.display import Audio, display
import time
import os



class TSVProcessor:
    def __init__(self, model_name, tsv_file_path):
        self.model_name = model_name
        self.tsv_file_path = tsv_file_path
        self.result = None
        self.tsv_data = None

    def transcribe_and_save_to_tsv(self, mp3_file_path):
        model = stable_whisper.load_faster_whisper(self.model_name)
        self.result = model.transcribe_stable(mp3_file_path)
        self.result.to_tsv(self.tsv_file_path, segment_level=True, word_level=False)

    def read_tsv(self):
        self.tsv_data = pd.read_csv(self.tsv_file_path, sep='\t', header=None)
        self.tsv_data.columns = ['start', 'end', 'text']

    def process_data(self):
        if self.tsv_data is None:
            self.read_tsv()

        new_data = []
        ilk_baslama = None
        metin = ''

        for i in range(len(self.tsv_data)):
            start_time = self.tsv_data.iloc[i]['start']
            text = self.tsv_data.iloc[i]['text']

            if ilk_baslama is None:
                ilk_baslama = start_time

            metin += text

            if text.endswith('.'):
                end_time = self.tsv_data.iloc[i]['end'] + 250
                new_data.append((ilk_baslama, end_time, metin))
                ilk_baslama = None
                metin = ''

        return pd.DataFrame(new_data, columns=['start', 'end', 'text'])

    def play_audio_segments(self, mp3_dir):
        for mp3_file in os.listdir(mp3_dir):
            if mp3_file.endswith('.mp3'):
                mp3_file_path = os.path.join(mp3_dir, mp3_file)
                audio = AudioSegment.from_mp3(mp3_file_path)
                for index, row in self.process_data().iterrows():
                    start_time = row['start']
                    end_time = row['end']
                    extracted_segment = audio[start_time:end_time]
                    file_name = f"extracted_segment_{index}.mp3"
                    extracted_segment.export(file_name, format="mp3")
                    print(row['text'])
                    display(Audio(file_name))
                    duration = (end_time - start_time) / 1000  
                    time.sleep(duration)



model_name = 'base'
tsv_file_path = r'C:\Users\ramal\azspeech_youtube\tsvdata\audio2.tsv'
mp3_dir = r"C:\Users\ramal\azspeech_youtube\audio_output\audio.mp3"

processor = TSVProcessor(model_name, tsv_file_path)
processor.transcribe_and_save_to_tsv(mp3_dir)  
processor.play_audio_segments(mp3_dir)  
