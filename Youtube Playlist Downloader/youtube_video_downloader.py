"""
This script can be used to download Youtube videos.
Dependency : 'pytube' module.
"""
# Author : Vikas Jethwani(Stan.Vj)
from pytube import YouTube

# Pass the link of the video
def download_vid(link):
    YouTube(link).streams.first().download()

if __name__ == '__main__':
    input_link = input("Please enter a valid Youtube video link : ")
    try:
        download_vid(input_link)
        print("Video has been downloaded successfully!")
    except:
        print("Some error occured or Invalid Video Link.")
