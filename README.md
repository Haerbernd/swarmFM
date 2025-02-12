# README

A simple Python program that streams the [SwarmFM YouTube Stream](https://www.youtube.com/@boop/live).

It uses VLC, yt-dlp and Tk to do it. You can change between the audio only stream or with video.

It is only available for desktop right now, but I might add Android support later. _Please also notice that as I don't own an Apple device and don't intend to change that, I am not able to test it on MacOS. I can only tell you that it **should** work, not that it will. If you can and want to verify the function of a build on MacOS, please do so._

The following two projects might also interest you:

- [SwarmFM Player by gwashark](https://github.com/gwashark/swarmfm-player)
- [SwarmFM Extension by tywaraxe](https://github.com/tywaraxe/SwarmFM-Extension)

## Requirements
- A functioning Python installation (with pip).
- Tk
  - Windows: Should be installed by default
  - MacOS: Should be installed by default
  - Linux:
    - Debian/Ubuntu: should be installed by default
    - I can't speak for other Distros, but you might need to install it via your package manager (i.e.: `sudo apt install tk`, `sudo pacman -S tk`, etc.)

## Installation
_Attention: There might be problems with your existing VLC installation (especially on Windows). I still have to find out the source of the problem. If you want to be sure that everything works, as intended, I would recommend you using a venv. But even then it works in general._

Pull the Repo and cd into it

`git pull https://github.com/Haerbernd/swarmFM`

`cd swarmFM`

Run the install-requirements script (`.sh` on Linux/Mac, `.bat` on Windows)

`./install-requirements.[bat/sh]`

Run `swarmFN.py` with Python

`python3 swarmFM.py`

## Legal and Stuff
### SwarmFM
SwarmFm is a 24/7 Neuro-sama radio where you can listen to music from Neuro-Sama and Evil's karaoke streams to your heart's content. It is provided via a 24/7 YouTube Stream by [boop](https://www.youtube.com/@boop).
### OpenSource Licenses
This project makes use of both the [yt-dlp project](https://github.com/yt-dlp/yt-dlp), published via the Unlicense and [VideoLAN's VLC](https://www.videolan.org/), published via the GNU General Public License version 2 (GNU GPLv2).
