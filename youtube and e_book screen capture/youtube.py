
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

print(Path.home())
 # Add /downloads folder to the home directory
SAVE_PATH = Path.home() / 'Downloads'
print(SAVE_PATH)



# from pytubefix.cli import on_progress
# from pytubefix import YouTube
# import os
# import subprocess

# # Function to merge video and audio using ffmpeg
# def merge_video_audio(video_path, audio_path, output_path):
#     command = [
#         'ffmpeg',
#         '-i', video_path,
#         '-i', audio_path,
#         '-c:v', 'copy',
#         '-c:a', 'aac',
#         '-strict', 'experimental',
#         output_path
#     ]
#     subprocess.run(command, check=True)


# yt = YouTube(input("ENTER YOUTUBE URL:"), on_progress_callback=on_progress)

# # Filter video-only streams (higher resolution)
# video_only_streams = yt.streams.filter(only_video=True, file_extension='mp4')
# # Filter audio-containing streams (progressive, lower resolution)
# audio_video_streams = yt.streams.filter(progressive=True, file_extension='mp4')

# # Select the highest resolution video-only stream
# highest_res_video_stream = max(video_only_streams, key=lambda s: int(s.resolution.rstrip('p')))
# # Select the highest resolution audio-containing stream
# highest_res_audio_stream = max(audio_video_streams, key=lambda s: int(s.resolution.rstrip('p')))

# # Download the streahttps://www.youtube.com/watch?v=Q71xBFP5vikms
# video_path = highest_res_video_stream.download(filename='video_only.mp4')
# audio_path = highest_res_audio_stream.download(filename='audio_video.mp4')

# # Merge the video and audio
# output_path = SAVE_PATH / 'merged_video.mp4'
# merge_video_audio(video_path, audio_path, output_path)

# # Clean up temporary files
# os.remove(video_path)
# os.remove(audio_path)

# print(f'Merged video saved to {output_path}')





# ##dowload playlist
# from pytubefix import Playlist
# from pytubefix.cli import on_progress


# pl = Playlist(input("ENTER YOUTUBE URL:"))

# for video in pl.videos:
#     ys = video.streams.get_highest_resolution()
#     ys.download(SAVE_PATH)





# yt = YouTube(input("ENTER YOUTUBE URL:"), on_progress_callback=on_progress)

# # Extract numerical values from the resolution strings and sort the streams based on these values
# sorted_streams = sorted(
#     [stream for stream in yt.streams.filter(progressive=True) if stream.resolution],
#     key=lambda x: int(x.resolution.rstrip('p')),  # Convert resolution string to integer for sorting
#     reverse=True
# )

# # Select the stream with the highest resolution
# highest_res_stream = sorted_streams[0]

# print(highest_res_stream)
# highest_res_stream.download(output_path=SAVE_PATH)


###dowload playlist
# from pytubefix import Playlist
# from pytubefix.cli import on_progress
 
# url = "url"

# pl = Playlist(url)

# for video in pl.videos:
#     ys = video.streams.get_audio_only()
#     ys.download(mp3=True) # pass the parameter mp3=True to save in .mp3



# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download(output_path="/Users/macbookpro/Downloads")
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# #which pyDownload(link)



## Download single youtube video
# where to save 
SAVE_PATH = "/Users/macbookpro/Downloads" #to_do 

# link of the video to be downloaded 
link = "https://www.youtube.com/watch?v=_5_QHE3p8EA"

try: 
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for mp4 files
mp4_streams = yt.streams.filter(file_extension='mp4').all()

# get the video with the highest resolution
d_video = mp4_streams[-1]

try: 
    # downloading the video 
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except: 
    print("Some Error!")



#url = "https://www.youtube.com/watch?v=_5_QHE3p8EA"
SAVE_PATH = "/Users/macbookpro/Downloads"

yt = YouTube(input("ENTER YOUTUBE URL:"), on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_highest_resolution()
ys.download(output_path=SAVE_PATH)