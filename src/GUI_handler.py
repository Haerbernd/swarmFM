import sys

from src import config_handler
from src import player_handler

try:
    # The following comments stop PyCharm from complaining
    # noinspection PyUnresolvedReferences
    import tkinter as tk
    # noinspection PyUnresolvedReferences
    from tkinter import ttk
except ImportError:
    print("Make sure you have tk installed\n")
    sys.exit(0)


def init() -> (tk.Tk, tk.Canvas):
    """
    Desc here
    :return: tkinter.Tk. Root instance of Tkinter.
    """

    settings: dict = config_handler.load_settings(config_handler.get_config_path())

    width: int = 800
    height: int = 500

    root: tk.Tk = tk.Tk()
    root.title("SwarmFM")
    root.geometry(f"{width}x{height}")
    root.configure(bg="#1e1e1e")  # Dark theme background

    # Video Canvas
    video_canvas: tk.Canvas = tk.Canvas(root, bg="black", width=width, height=height-100)
    if settings["mode"] == "video":
        video_canvas.pack(fill="both", expand=True)

    # Style Customization
    style: ttk.Style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=5, background="#333", foreground="white")
    style.configure("TLabel", font=("Arial", 12), background="#1e1e1e", foreground="white")

    # Control Frame
    control_frame: tk.Frame = tk.Frame(root, bg="#1e1e1e")
    control_frame.pack(pady=10)

    audio_btn: ttk.Button = ttk.Button(control_frame, text="Audio Only", command=lambda:player_handler
                                       .start_stream(video=False, video_canvas=video_canvas))
    video_btn: ttk.Button = ttk.Button(control_frame, text="Video + Audio", command=lambda: player_handler
                                       .start_stream(video=True, video_canvas=video_canvas))
    stop_btn: ttk.Button = ttk.Button(control_frame, text="Stop", command=player_handler.stop_stream)
    mute_btn: ttk.Button = ttk.Button(control_frame, text="Mute/Unmute", command=player_handler.toggle_mute)
    exit_btn: ttk.Button = ttk.Button(control_frame, text="Exit", command=player_handler.exit_program(root=root))

    volume_label: ttk.Label = ttk.Label(control_frame, text="Volume")
    volume_slider: ttk.Scale = ttk.Scale(control_frame, from_=0, to=100, orient="horizontal",
                                         command=player_handler.set_volume)
    volume_slider.set(settings["volume"])

    # Grid Layout for Controls
    audio_btn.grid(row=0, column=0, padx=5)
    video_btn.grid(row=0, column=1, padx=5)
    stop_btn.grid(row=0, column=2, padx=5)
    mute_btn.grid(row=0, column=3, padx=5)
    exit_btn.grid(row=0, column=4, padx=5)
    volume_label.grid(row=1, column=0, padx=5)
    volume_slider.grid(row=1, column=1, columnspan=4, sticky="ew")

    return root, video_canvas
