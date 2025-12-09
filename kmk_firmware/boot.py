import board

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner

_KEY_CFG = [
    board.SW1,  board.SW2,
    board.SW3,  board.SW4,
    board.SW5,  board.SW6,
]

# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        self.matrix = KeysScanner(
            pins=_KEY_CFG,
        )

keyboard = KMKKeyboard()

keyboard.keymap = [
    [
        KC.A, KC.B,
        KC.C, KC.D,
        KC.E, KC.F
    ],
]

if __name__ == '__main__':
    keyboard.go()
