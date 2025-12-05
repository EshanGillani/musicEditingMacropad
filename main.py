
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys




keyboard = KMKKeyboard()


macros = Macros()
keyboard.modules.append(macros)

mediaKeys = MediaKeys()
keyboard.extensions.append(MediaKeys())


PINS = [board.D7, board.D8, board.D9, board.D10, board.D0, board.D1]


keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MEDIA_PLAY_PAUSE, KC.R, KC.MEDIA_REWIND, KC.MEDIA_FAST_FORWARD, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
