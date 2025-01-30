!pip install yt-dlp

from yt_dlp import YoutubeDL
from google.colab import drive
# drive.mount('/content/gdrive', force_remount=True)
root_dir = '/content/'

link = 'https://www.youtube.com/watch?v=9JJKfFyM-CY'

ydl_opts = {}

with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(link, download=False)
    video_title = info_dict.get('title', None)

path = f'{root_dir}/{video_title}.mp4'

ydl_opts.update({'outtmpl':path})

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
