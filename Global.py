credentials = {}
keyboard_clicks = ""


def get_keyboard_clicks():
    global keyboard_clicks
    return keyboard_clicks


def set_keyboard_clicks(click):
    global keyboard_clicks
    keyboard_clicks = keyboard_clicks + click


def clear_keyboard_clicks():
    global keyboard_clicks
    keyboard_clicks = ""
