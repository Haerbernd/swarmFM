import sys

from typing import Tuple
from src import GUI_handler

try:
    # The following comments stop PyCharm from complaining
    # noinspection PyUnresolvedReferences
    import tkinter as tk
    # noinspection PyUnresolvedReferences
    from tkinter import ttk
except ImportError:
    print("Make sure you have tk installed\n")
    sys.exit(0)


def init() -> Tuple[tk.Tk, tk.Canvas]:
    """
    Initializes the program, to make sure everything is imported correctly
    :return: The root Tk instance and the video canvas.
    """

    (root, video_canvas) = GUI_handler.init()
    return root, video_canvas
