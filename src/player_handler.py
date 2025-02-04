import sys
import vlc
import yt_dlp

from src import config_handler

try:
    # The following comments stop PyCharm from complaining
    # noinspection PyUnresolvedReferences
    import tkinter as tk
    # noinspection PyUnresolvedReferences
    from tkinter import ttk
except ImportError:
    print("Make sure you have tk installed\n")
    sys.exit(0)

player: vlc.MediaPlayer = vlc.MediaPlayer()
muted: bool = False

current_mode: str = "audio"  # <-- -- -->


def get_stream_url(video: bool = True, yt_url: str = "https://www.youtube.com/watch?v=thCiTnOzkOM") -> str:
    """Fetches the direct stream URL from YouTube."""
    format_option: str = "best" if video else "bestaudio"
    ydl_opts: dict = {
        "format": format_option,
        "live": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info: dict = ydl.extract_info(yt_url, download=False)
        return info["url"] if "url" in info else ""


def start_stream(video_canvas: tk.Canvas, video: bool = True) -> None:
    """Starts VLC playback with the YouTube stream."""
    global current_mode
    stop_stream()
    stream_url: str = get_stream_url(video)
    if stream_url:
        media: vlc.Media = vlc.Media(stream_url)
        player.set_media(media)
        if video:
            video_canvas.pack(fill="both", expand=True)
            player.set_xwindow(video_canvas.winfo_id())  # Embed video in Tkinter window
        else:
            video_canvas.pack_forget()
        player.play()
        current_mode = "video" if video else "audio"
        config_handler.save_settings(current_mode=current_mode)


def stop_stream() -> None:
    """Stops VLC playback."""
    player.stop()


def toggle_mute() -> None:
    """Toggles mute state."""
    global muted
    muted = not muted
    player.audio_toggle_mute()


def set_volume(value: str) -> None:
    """Sets VLC player volume."""
    volume: int = int(float(value))
    player.audio_set_volume(volume)
    config_handler.save_settings(volume=volume)


def exit_program(root: tk.Tk) -> None:
    """Stops playback and exits the application."""
    stop_stream()
    root.destroy()
