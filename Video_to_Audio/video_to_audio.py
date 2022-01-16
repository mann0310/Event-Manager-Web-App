import moviepy.editor
from tkinter.filedialog import*

try:
     video = askopenfilename()
     video = moviepy.editor.VideoFileClip(video)
     #you can also provide start and end point of video to be converted in audio
     audio = video.audio

     audio.write_audiofile("audio_file.mp3")

except:
     print("Please input a proper video file")
