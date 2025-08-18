import sys
from PyQt5 import QtWidgets
from pynput import keyboard

from overlay import *

def _vk_down(vk):
    return bool(ctypes.windll.user32.GetAsyncKeyState(vk) & 0x8000)

def ctrl_pressed():
    return _vk_down(0x11)   # VK_CONTROL

def alt_pressed():
    return _vk_down(0x12)   # VK_MENU (Alt)

def shift_pressed():
    return _vk_down(0x10)   # VK_SHIFT

def main():
    app     = QtWidgets.QApplication(sys.argv)
    overlay = OverlayWindow()

    hotkeys = {
        '<ctrl>+o': overlay.sig_open.emit,
        '<alt>+<up>'    : overlay.sig_up.emit,
        '<alt>+<down>'  : overlay.sig_down.emit,
        '<alt>+<left>'  : overlay.sig_left.emit,
        '<alt>+<right>' : overlay.sig_right.emit,
        '<alt>++'       : lambda: overlay.sig_plus.emit()  if not shift_pressed() else None,
        '<alt>+-'       : lambda: overlay.sig_minus.emit() if not shift_pressed() else None,
        '<alt>+<shift>++' : overlay.sig_zoom_in.emit,
        '<alt>+<shift>+-'   : overlay.sig_zoom_out.emit,
        '<ctrl>+q': overlay.sig_quit.emit,
    }
    listener = keyboard.GlobalHotKeys(hotkeys)
    listener.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()