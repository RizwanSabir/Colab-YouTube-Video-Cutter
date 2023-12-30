import yt_dlp
from moviepy.video.io.VideoFileClip import VideoFileClip
from IPython.display import HTML
from base64 import b64encode

# Set your video URL
video_url = 'https://www.youtube.com/watch?v=ysQoihAK-TE'

# Set up yt-dlp options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'downloaded_video.%(ext)s',
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
# Define the video path
video_path = 'downloaded_video.mp4'

# Trim the video from seconds 108 to 120
with VideoFileClip(video_path) as video:
    trimmed_video = video.subclip(108, 120)

    # Save the trimmed video
    trimmed_video.write_videofile('trimmed_video.mp4')
# Define the path to the trimmed video
video_path = 'trimmed_video.mp4'

# Create an HTML string to display the video
video_html = HTML("""
<video width=400 controls>
  <source src="data:video/mp4;base64,{0}" type="video/mp4">
</video>
""".format(b64encode(open(video_path, "rb").read()).decode()))

# Display the video
display(video_html)

