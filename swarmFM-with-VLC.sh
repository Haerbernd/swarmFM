#!/bin/sh

vlc -vvv https://www.youtube.com/@boop/live --no-video --sout '#transcode{acodec=mp3,ab=128,channels=2,samplerate=44100}:standard{access=http,mux=raw,dst=:8080}'
