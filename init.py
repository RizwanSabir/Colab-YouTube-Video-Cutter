from pytube import YouTube

def download_youtube_video(url, output_path='/content/test.mp4'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path)
        print("Download complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = "https://www.youtube.com/watch?v=vkLQylA4388"
output_path = "/content/test.mp4"

download_youtube_video(video_url, output_path)
