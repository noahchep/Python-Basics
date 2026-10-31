#yt-dlp
#pip install yt-dlp
import yt_dlp

video_url = "https://www.youtube.com/watch?v=7q58mWi_yRY"

ydl_opts = {
    # Single audio file, no merging, so ffmpeg isn't needed
    'format': 'bestaudio[ext=m4a]/bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])