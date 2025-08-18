import sys
from pynput import keyboard

from overlay import *
from utils import *

def main():
    app     = QtWidgets.QApplication(sys.argv)
    overlay = OverlayWindow()

    hotkeys = {
        '<ctrl>+<alt>+o': overlay.sig_open.emit,
        '<alt>+<up>'    : overlay.sig_up.emit,
        '<alt>+<down>'  : overlay.sig_down.emit,
        '<alt>+<left>'  : overlay.sig_left.emit,
        '<alt>+<right>' : overlay.sig_right.emit,
        '<alt>++'       : lambda: overlay.sig_plus.emit()  if not shift_pressed() else None,
        '<alt>+-'       : lambda: overlay.sig_minus.emit() if not shift_pressed() else None,
        '<alt>+<shift>++' : overlay.sig_zoom_in.emit,
        '<alt>+<shift>+-'   : overlay.sig_zoom_out.emit,
        '<ctrl>+<alt>+s': overlay.sig_settings.emit,
        '<ctrl>+<alt>+q': overlay.sig_quit.emit,
    }
    listener = keyboard.GlobalHotKeys(hotkeys)
    listener.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    load_settings()  # Load settings at startup
    main()