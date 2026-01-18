import sys
from pynput import keyboard

from overlay import *
from utils import *

def main():
    app     = QtWidgets.QApplication(sys.argv)
    overlay = OverlayWindow()

    hotkeys = {
        load_settings()["open"]: overlay.sig_open.emit,
        load_settings()["up"]: overlay.sig_up.emit,
        load_settings()["down"]: overlay.sig_down.emit,
        load_settings()["left"]: overlay.sig_left.emit,
        load_settings()["right"]: overlay.sig_right.emit,
        load_settings()["in"]: lambda: overlay.sig_plus.emit()  if not shift_pressed() else None,
        load_settings()["out"]: lambda: overlay.sig_minus.emit() if not shift_pressed() else None,
        load_settings()["in"]: overlay.sig_zoom_in.emit,
        load_settings()["out"]: overlay.sig_zoom_out.emit,
        load_settings()["settings"]: overlay.sig_settings.emit,
        load_settings()["quit"]: overlay.sig_quit.emit,
    }
    listener = keyboard.GlobalHotKeys(hotkeys)
    listener.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    load_settings()  # Load settings at startup
    main()