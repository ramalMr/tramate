"""ffmpeg eger yoxdursa o zaman git reposuna gedib .7z faylin yukleyib extract edib sonra 3 fayl olacaq 
   hemin o fayllari her hansisa bir qovluqa atib daha sonra istenilen locationda baslada bilmek ucun path elave edirik 
   diqqet: hem system hem user ucun olan path'a """

command =  ['ffmpeg -i .\filmm.mp4 -vf subtitles=audio2_converted.srt -c:a copy output_video.mp4']
