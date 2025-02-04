import json
import os
import platform
import subprocess

from src import player_handler

def get_config_path() -> str:
    """
    Get the path of the config file config.json.
    :return: String. Path of the config file (config.json).
    """
    user_os: str = platform.system().lower()

    if user_os == "windows":
        shell: subprocess = subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE)
        user: str = shell.communicate()[0].decode().split('\\')[-1].replace("\n", '').replace("\r", "")
        config_path: str = f"C:/Users/{user}/AppData/Roaming/SwarmFM/config.json"
    elif user_os == 'linux' or 'linux2':
        shell = subprocess.Popen('logname', shell=True, stdout=subprocess.PIPE)
        #  Notice: The usage of "logname" returns the username the user logged into -> sudo resistant
        user = shell.communicate()[0].decode().replace("\n", '')
        config_path: str = f"/home/{user}/.config/SwarmFM/config.json"
    elif user_os == 'darwin':
        config_path: str = "~/Library/Application Support/config.json"
    else:
        config_path: str = "./config/config.json"

    if os.path.exists(config_path):
        return config_path

    os.mkdir(config_path.replace("/config.json", ""))
    return config_path


def save_settings(volume: int | float = player_handler.player.audio_get_volume(),
                  current_mode: str = player_handler.current_mode, CONFIG_FILE = get_config_path()) -> None:
    """
    Saves settings to a JSON file.
    :param volume: The volume of the program. Intended as the return value of player.audio_get_volume().
    :param current_mode: Mode of the player. Either 'audio' or 'video'
    :return: None
    """
    settings_f: dict = {"volume": volume, "mode": current_mode}
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings_f, file)


def load_settings(CONFIG_FILE: str = get_config_path()) -> dict:
    """
    Loads settings from a JSON file.
    :return: Dictionary. The config/settings of the program as dictionary.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    save_settings(volume=50, current_mode="audio")
    return {"volume": 50, "mode": "audio"}



