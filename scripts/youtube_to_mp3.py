from pytube import YouTube
from pydub import AudioSegment
import os

# YouTube video URL'si
video_url = "https://www.youtube.com/watch?v=8eYZ6n3U-Ck"

# yukle ve qeyd et bura toxunmayin 
video_output_folder = 'video_output'
audio_output_folder = 'audio_output'

# yoxla yoxdursa yarad 
if not os.path.exists(video_output_folder):
    os.makedirs(video_output_folder)
if not os.path.exists(audio_output_folder):
    os.makedirs(audio_output_folder)

# YouTube videosunu yukle
yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()
video.download(output_path=video_output_folder, filename='video.mp4')

# yuklenen video fayl patha yukle
video_path = os.path.join(video_output_folder, 'video.mp4')
audio = AudioSegment.from_file(video_path, format="mp4")

# mp3 e cevir 
audio.export(os.path.join(audio_output_folder, "audio.mp3"), format="mp3")

print("video mp3 e ugurla cevrildi .")
