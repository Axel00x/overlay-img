import os
import sys
import json

__version__ = "1.1"

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
    "up": '<alt>+<up>',
    "down": '<alt>+<down>',
    "left": '<alt>+<left>',
    "right": '<alt>+<right>',
    "open": '<ctrl>+<alt>+o',
    "quit": '<ctrl>+<alt>+q',
    "op_up": '<alt>++',
    "op_down": '<alt>+-',
    "in": '<alt>+<shift>++',
    "out": '<alt>+<shift>+-',
    "settings": '<ctrl>+<alt>+s',
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
            "up": data.get("up", DEFAULT_SETTINGS["up"]),
            "down": data.get("down", DEFAULT_SETTINGS["down"]),
            "left": data.get("left", DEFAULT_SETTINGS["left"]),
            "right": data.get("right", DEFAULT_SETTINGS["right"]),
            "open": data.get("open", DEFAULT_SETTINGS["open"]),
            "quit": data.get("quit", DEFAULT_SETTINGS["quit"]),
            "op_up": data.get("op_up", DEFAULT_SETTINGS["op_up"]),
            "op_down": data.get("op_down", DEFAULT_SETTINGS["op_down"]),
            "in": data.get("in", DEFAULT_SETTINGS["in"]),
            "out": data.get("out", DEFAULT_SETTINGS["out"]),
            "settings": data.get("settings", DEFAULT_SETTINGS["settings"]),
        }

def save_settings(
    move: int = None,
    zoom: int = None,
    opacity: float = None,
    up: str = None,
    down: str = None,
    left: str = None,
    right: str = None,
    open_: str = None,
    quit: str = None,
    op_up: str = None,
    op_down: str = None,
    in_: str = None,
    out: str = None,
    settings_: str = None
    ):
    
    settings = load_settings()
    if move is not None:
        settings["move"] = move
    if zoom is not None:
        settings["zoom"] = zoom
    if opacity is not None:
        settings["opacity"] = opacity
    if up is not None:
        settings["up"] = up
    if down is not None:
        settings["down"] = down
    if left is not None:
        settings["left"] = left
    if right is not None:
        settings["right"] = right
    if open_ is not None:
        settings["open"] = open_
    if quit is not None:
        settings["quit"] = quit
    if op_up is not None:
        settings["op_up"] = op_up
    if op_down is not None:
        settings["op_down"] = op_down
    if in_ is not None:
        settings["in"] = in_
    if out is not None:
        settings["out"] = out
    if settings_ is not None:
        settings["settings"] = settings_
        
    settings["version"] = __version__  # Ensure version is always up-to-date
    
    settings["move"] = int(settings["move"])  # Ensure move is an integer
    settings["zoom"] = int(settings["zoom"])  # Ensure zoom is an integer
    settings["opacity"] = float(settings["opacity"])  # Ensure opacity is a float
    settings["up"] = str(settings["up"])
    settings["down"] = str(settings["down"])
    settings["left"] = str(settings["left"])
    settings["right"] = str(settings["right"])
    settings["open"] = str(settings["open"])
    settings["quit"] = str(settings["quit"])
    settings["in"] = str(settings["in"])
    settings["out"] = str(settings["out"])
    settings["settings"] = str(settings["settings"])
    
    if SETTINGS_PATH is None:
        print("Hello World")
    
    with open(SETTINGS_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)
        
def get_version():
    return load_settings()["version"]