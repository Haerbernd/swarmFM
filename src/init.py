from typing import Tuple
from src import GUI_handler


def init() -> Tuple:
    """
    Initializes the program, to make sure everything is imported correctly
    :return: The root Tk instance and the video canvas.
    """

    root, video_canvas = GUI_handler.init()
    return root, video_canvas
