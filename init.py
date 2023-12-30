from moviepy.video.io.VideoFileClip import VideoFileClip


video_path = '/content/downloaded_video.webm'

with VideoFileClip(video_path) as video:
    trimmed_video = video.subclip(108, 120)  

    # Save the trimmed video
    trimmed_video.write_videofile('trimmed_video.mp4')

from IPython.display import HTML
from base64 import b64encode

# Replace this with the correct path to your video file
video_path = '/content/trimmed_video.mp4'

# Create an HTML string to display the video
video_html = HTML("""
<video width=400 controls>
  <source src="data:video/mp4;base64,{0}" type="video/mp4">
</video>
""".format(b64encode(open(video_path, "rb").read()).decode()))

# Display the video
display(video_html)

