import yt_dlp
from moviepy.video.io.VideoFileClip import VideoFileClip
from IPython.display import HTML
from base64 import b64encode
from moviepy.editor import VideoFileClip

# Replace the YouTube URL with your desired video URL
video_url = "https://www.youtube.com/watch?v=NhmGNfILDyw"

!yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' {video_url}

video_path = 'downloaded_video.mp4'

# In case if has downloaded it in Wbem
# !ffmpeg -i /content/downloaded_video_mp4.webm  /content/downloadMP4.mp4

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

