from pytube import YouTube

# video_url = 'https://www.youtube.com/watch?v=NJRPrDeNR0g&t=4s'
video_url = 'https://youtu.be/NJRPrDeNR0g'

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution().download()

print('Видео сперто ))) ')