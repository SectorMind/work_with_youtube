# pip install pytube moviepy
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

video_id = 'm4821y4821y'
yt = YouTube(f'https://youtu.be/{video_id}')
video_url = f"https://www.youtube.com/watch?v={video_id}"
# Download the YouTube video
# yt = YouTube(video_url)
yt_title = yt.title
yt_title = yt_title.replace(" ", "_").replace(".", "").replace("/", "").replace(":", "").replace("*", "").replace("?", "").replace("»", "").replace("<", "").replace(">", "").replace("|", "")
yt_title = f"{yt_title}.mp4"
print(yt_title)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=f"{yt_title}")


pre_start_time = "00:00:01"
pre_end_time = "01:12:15"
arr_pre_start_time = pre_start_time.split(":")
arr_pre_end_time = pre_end_time.split(":")

# Define the start and end times in seconds (adjust as needed)
start_time = int(arr_pre_start_time[0])*3600 + int(arr_pre_start_time[1])*60 + int(arr_pre_start_time[2])  # Start time in seconds
end_time = int(arr_pre_end_time[0])*3600 + int(arr_pre_end_time[1])*60 + int(arr_pre_end_time[2])   # End time in seconds

# stream = yt.streams.get_highest_resolution()
# stream.download(filename=yt_title)

# Input video file name
input_video = f"{yt_title}"

# Output video file name
output_video = f"{yt_title[:-4]}_cut.mp4"

# Cut the video at the specified time
ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=output_video)

print(f"Video cut from {start_time} to {end_time} seconds saved as {output_video}")
