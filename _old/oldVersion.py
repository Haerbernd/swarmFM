# Works but is not the nicest version

import sys
import yt_dlp
import vlc

try:
    # The following comments stop PyCharm from complaining
    # noinspection PyUnresolvedReferences
    import tkinter as tk
    # noinspection PyUnresolvedReferences
    from tkinter import ttk
except ImportError:
    print("Make sure you have tk installed\n")
    sys.exit(0)

# SwarmFM Link
yt_url: str = "https://www.youtube.com/watch?v=thCiTnOzkOM"

# Create VLC Player
player: vlc.MediaPlayer = vlc.MediaPlayer()
muted: bool = False

def get_stream_url(video: bool = True) -> str:
    """Fetches the direct stream URL from YouTube."""
    format_option: str = "best" if video else "bestaudio"
    ydl_opts: dict = {
        "format": format_option,
        "live": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info: dict = ydl.extract_info(yt_url, download=False)
        return info["url"] if "url" in info else ""

def start_stream(video: bool = True) -> None:
    """Starts VLC playback with the YouTube stream."""
    stop_stream()
    stream_url: str = get_stream_url(video)
    if stream_url:
        media: vlc.Media = vlc.Media(stream_url)
        player.set_media(media)
        if video:
            player.set_xwindow(video_canvas.winfo_id())  # Embed video in Tkinter window
        player.play()

def stop_stream() -> None:
    """Stops VLC playback."""
    player.stop()

def toggle_mute() -> None:
    """Toggles mute state."""
    global muted
    muted = not muted
    player.audio_toggle_mute()

def set_volume(val: str) -> None:
    """Sets VLC player volume."""
    volume: int = int(float(val))
    player.audio_set_volume(volume)

def exit_program() -> None:
    """Stops playback and exits the application."""
    stop_stream()
    root.destroy()

# GUI Setup
root: tk.Tk = tk.Tk()
root.title("YouTube Live Stream Player")
root.geometry("800x500")
root.configure(bg="#1e1e1e")  # Dark theme background

# Video Canvas
video_canvas: tk.Canvas = tk.Canvas(root, bg="black", width=800, height=400)
video_canvas.pack()

# Style Customization
style: ttk.Style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5, background="#333", foreground="white")
style.configure("TLabel", font=("Arial", 12), background="#1e1e1e", foreground="white")

# Control Frame
control_frame: tk.Frame = tk.Frame(root, bg="#1e1e1e")
control_frame.pack(pady=10)

audio_btn: ttk.Button = ttk.Button(control_frame, text="Audio Only", command=lambda: start_stream(video=False))
video_btn: ttk.Button = ttk.Button(control_frame, text="Video + Audio", command=lambda: start_stream(video=True))
stop_btn: ttk.Button = ttk.Button(control_frame, text="Stop", command=stop_stream)
mute_btn: ttk.Button = ttk.Button(control_frame, text="Mute/Unmute", command=toggle_mute)
exit_btn: ttk.Button = ttk.Button(control_frame, text="Exit", command=exit_program)

volume_label: ttk.Label = ttk.Label(control_frame, text="Volume")
volume_slider: ttk.Scale = ttk.Scale(control_frame, from_=0, to=100, orient="horizontal", command=set_volume)

# Grid Layout for Controls
audio_btn.grid(row=0, column=0, padx=5)
video_btn.grid(row=0, column=1, padx=5)
stop_btn.grid(row=0, column=2, padx=5)
mute_btn.grid(row=0, column=3, padx=5)
exit_btn.grid(row=0, column=4, padx=5)
volume_label.grid(row=1, column=0, padx=5)
volume_slider.grid(row=1, column=1, columnspan=4, sticky="ew")

# Start GUI
root.mainloop()
