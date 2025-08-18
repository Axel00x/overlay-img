import ctypes

def _vk_down(vk):
    return bool(ctypes.windll.user32.GetAsyncKeyState(vk) & 0x8000)

def ctrl_pressed():
    return _vk_down(0x11)   # VK_CONTROL

def alt_pressed():
    return _vk_down(0x12)   # VK_MENU (Alt)

def shift_pressed():
    return _vk_down(0x10)   # VK_SHIFT