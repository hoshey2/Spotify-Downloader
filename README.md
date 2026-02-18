# Spotify-Downloader
Download Spotify songs using Musicfetch and yt-dlp.

## Description:
This script uses the Musicfetch API to download the YouTube music link of a Spotify song. The YouTube music link is then sent to yt-dlp to download the song locally.

## Platform:
Linux/Windows

## Prerequisites:
1.	A [Musicfetch](https://musicfetch.io) subscription. They have a 7-day free trial that you can use a virtual credit card with so you don’t get charged
2.	yt-dlp  – install instructions [here](https://github.com/yt-dlp/yt-dlp/wiki/Installation)
3.	ffmpeg – binaries located [here](https://www.ffmpeg.org/download.html#build-windows)

## Usage
1.	Drag and drop your Spotify playlist into a text document
2.	Run the spotifyDownloader.py script on your playlist document, this will generate a YouTube music link list
3.	Run yt-dlp.exe on your YouTube link list ```yt-dlp.exe -a "PATH_TO_YOUTUBE_LINK_LIST" -x --audio-format mp3 -P "PATH_TO_SAVE_SONGS"```
4.	Enjoy your music!
