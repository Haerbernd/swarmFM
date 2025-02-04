#!/bin/sh

yt-dlp https://www.youtube.com/@boop/live -f bestaudio -g | xargs vlc
