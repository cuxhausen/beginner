import pytube # pip install pytube, pytube3
from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

# Title of video
print("Title: ", yt.title)

# Number of views of video
print("Number of views: ", yt.views)

# Length of the video
print("Length of video: ", yt.length, "seconds")

# Description of video
print("Description: ", yt.description)

# Rating
print("Ratings: ", yt.rating)

# Printing all the available streams
#print(yt.streams)
#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(only_video=True))
#print(yt.streams.filter(progressive=True)) # filter out progressive streams

ys = yt.streams.get_highest_resolution() # the highest resolution progressive stream

ys = yt.streams.get_by_itag('22') # We can also choose any stream by the help of its itag

ys.download() # Upload a video to the current directory

# ys.download('location')

"""
import pytube
video_link = imput("Enter your video link: ") # https://www.youtube.com/watch?v=8ZpVwAeLzm4
yt = pytube.YouTube(video_link)
videos = yt.videos
video = yt.get('mp4', '720p') # we filter the video by format and quality
path = '/Users/Oltjano/Desktop'
video.download(path)
"""