import sys

from src import init

try:
    # The following comments stop PyCharm from complaining
    # noinspection PyUnresolvedReferences
    import tkinter as tk
    # noinspection PyUnresolvedReferences
    from tkinter import ttk
except ImportError:
    print("Make sure you have tk installed\n")
    sys.exit(0)

# YouTube Live URL
yt_url: str = "https://www.youtube.com/@boop/live"

root, video_canvas = init.init()

root.mainloop()
