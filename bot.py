from ctypes import *
import time
import win32con, win32api


class POINT(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]


def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def getCursorPosition(refreshTime):
    GetCursorPos = windll.user32.GetCursorPos
    p = POINT()
    while True:
        GetCursorPos(byref(p))
        print(p.x, p.y)
        time.sleep(refreshTime)


# getCursorPosition(0.1)


for i in range(5):
    time.sleep(2)
    click(938, 890)
    time.sleep(5)
    click(900, 800)
    time.sleep(20 * 60)
