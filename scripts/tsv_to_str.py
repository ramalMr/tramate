import pandas as pd


df = pd.read_csv('tsvdata/audio2.tsv', sep='\t', header=None)

#0-ci row run time 1-ci end time 2- ci ise text olur
with open('out_fayl.srt', 'w', encoding='utf-8') as srt_file:
    for index, row in df.iterrows():
        start_ms = int(row[0])
        end_ms = int(row[1])
        text = row[2]
        start_time_srt = f'{start_ms // 3600000:02d}:{(start_ms % 3600000) // 60000:02d}:{(start_ms % 60000) // 1000:02d},{start_ms % 1000:03d}'
        end_time_srt = f'{end_ms // 3600000:02d}:{(end_ms % 3600000) // 60000:02d}:{(end_ms % 60000) // 1000:02d},{end_ms % 1000:03d}'
        srt_file.write(f"{index + 1}\n")
        srt_file.write(f"{start_time_srt} --> {end_time_srt}\n")
        srt_file.write(f"{text}\n\n")