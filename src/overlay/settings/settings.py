import os
import sys
import json

__version__ = "1.1b1"

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SETTINGS_PATH = os.path.join(BASE_DIR, 'settings.json')

# Default settings
DEFAULT_SETTINGS = {
    "move": 10,  # Default move value in pixels
    "zoom": 10,  # Default zoom value in pixels
    "opacity": 0.05,  # Default opacity change (1.0 = fully opaque)
    "version": __version__,
}

def load_settings() -> dict:
    if not os.path.exists(SETTINGS_PATH):
        # Create directory if it doesn't exist
        os.makedirs(BASE_DIR, exist_ok=True)
        with open(SETTINGS_PATH, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
        return DEFAULT_SETTINGS.copy()

    with open(SETTINGS_PATH, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            # If JSON is invalid, reset to default
            data = DEFAULT_SETTINGS.copy()
            with open(SETTINGS_PATH, 'w', encoding='utf-8') as fw:
                json.dump(data, fw, indent=4)
        # Ensure all keys are present
        return {
            "move": data.get("move", DEFAULT_SETTINGS["move"]),
            "zoom": data.get("zoom", DEFAULT_SETTINGS["zoom"]),
            "opacity": data.get("opacity", DEFAULT_SETTINGS["opacity"]),
            "version": data.get("version", __version__),
        }

def save_settings(
    move: int = None,
    zoom: int = None,
    opacity: float = None,
    ):
    
    settings = load_settings()
    if move is not None:
        settings["move"] = move
    if zoom is not None:
        settings["zoom"] = zoom
    if opacity is not None:
        settings["opacity"] = opacity
        
    settings["version"] = __version__  # Ensure version is always up-to-date
    
    settings["move"] = int(settings["move"])  # Ensure move is an integer
    settings["zoom"] = int(settings["zoom"])  # Ensure zoom is an integer
    settings["opacity"] = float(settings["opacity"])  # Ensure opacity is a float

    with open(SETTINGS_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)

def get_version() -> str:
    return load_settings()["version"]

def get_move_val() -> int:
    return load_settings()["move"]

def set_move_val(value: int):
    save_settings(move=value)

def get_zoom_val() -> int:
    return load_settings()["zoom"]

def set_zoom_val(value: int):
    save_settings(zoom=value)
    
def get_opacity_val() -> float:
    return load_settings()["opacity"]

def set_opacity_val(value: float):
    save_settings(opacity=value)