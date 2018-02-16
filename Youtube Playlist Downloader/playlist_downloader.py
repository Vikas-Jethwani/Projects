"""
This script can be used to download Youtube playlists.
It uses regex to find links of youtube videos in a playlist.
With the help of 'pytube' module, it downloads the videos one-by-one.
Currently, if a playlist has more than 100 videos, it will only download the first 100.
Made by :- Vikas Jethwani( StAn.Vj )
"""
import requests, re, sys
from youtube_video_downloader import download_vid

# Helper function to download videos one-by-one, and keep user updated about the current progress.
def download_all(links):
    total = len(links)
    url = 'http://www.youtube.com/watch?v='
    for idx in range(total):
        print("Downloading " + str(idx+1) + " of " + str(total))
        print("Link of video : ", url + links[idx])
        download_vid(url + links[idx])
        print("Video downloaded ...\n")


if __name__ == '__main__':
    playlist_link = input("Enter Youtube Playlist link : ")
    try:
        html = str(requests.get(playlist_link).content)
    except:
        print("Enter valid Youtube Playlist Link !")
        sys.exit(0)

    regex = r'href="/watch\?v=(.+?)"'
    pattern = re.compile(regex)

    links = list(re.findall(pattern, html))
    if len(links) == 0:
        print("Zero video items found on the current link.\nPlease enter valid youtube playlist link.")
        sys.exit(0)

    links = links[2::2]    # To remove duplicate links

    try:
        download_all(links)
        print("Playlist has been successfully downloaded!")
    except KeyboardInterrupt:
        print("Keyboard Interrupt encountered. Terminating program.")
    except Exception:
        print("Some error occured, please try again later.")
