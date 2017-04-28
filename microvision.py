from microbit import *

pin_map = [
    pin16,
    pin15,
    pin14,
    pin13,
    pin12
]

alphabet = {
    "a": [
        " ### ",
        "#   #",
        "#####",
        "#   #",
        "#   #"
    ],
    "b": [
        "#### ",
        "#   #",
        "#### ",
        "#   #",
        "#### "
    ],
    "c": [
        "#####",
        "#    ",
        "#    ",
        "#    ",
        "#####"
    ],
    "d": [
        "#### ",
        "#   #",
        "#   #",
        "#   #",
        "#### "
    ],
    "e": [
        "#####",
        "#    ",
        "#####",
        "#    ",
        "#####"
    ],
    "f": [
        "#####",
        "#    ",
        "#####",
        "#    ",
        "#    "
    ],
    "g": [
        " ####",
        "#    ",
        "#  ##",
        "#   #",
        " ####"
    ],
    "h": [
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #"
    ],
    "i": [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "#####"
    ],
    "j": [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "###  "
    ],
    "k": [
        "#   #",
        "#  # ",
        "##   ",
        "#  # "
        "#   #"
    ],
    "l": [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####"
    ],
    "m": [
        "#   #",
        "## ##",
        "# # #",
        "#   #",
        "#   #"
    ],
    "n": [
        "#   #",
        "##  #",
        "# # #",
        "#  ##",
        "#   #"
    ],
    "o": [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        " ### "
    ],
    "p": [
        "#### ",
        "#   #",
        "#### ",
        "#    ",
        "#    "
    ],
    "q": [
        " ### ",
        "#   #",
        "#   #",
        "#  ##",
        " ####"
    ],
    "r": [
        "#### ",
        "#   #",
        "#### ",
        "#  # ",
        "#   #"
    ],
    "s": [
        "#####",
        "#    ",
        "#####",
        "    #",
        "#####"
    ],
    "t": [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  "
    ],
    "u": [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ],
    "v": [
        "#   #",
        "#   #",
        " # # ",
        " # # ",
        "  #  "
    ],
    "w": [
        "#   #",
        "#   #",
        "# # #",
        "## ##",
        "#   #"
    ],
    "x": [
        "#   #",
        " # # ",
        "  #  ",
        " # # ",
        "#   #"
    ],
    "y": [
        "#   #",
        " # # ",
        "  #  ",
        "  #  ",
        "  #  "
    ],
    "z": [
        "#####",
        "   # ",
        "  #  ",
        " #   ",
        "#####"
    ],
    " ": [
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ],
    ".": [
        "     ",
        "     ",
        "     ",
        "     ",
        "  #  "
    ]
}

def print_letter(letter, pins = True):
    print(letter)
    pattern = alphabet[letter]

    if pattern:

        sleep(letter_pause)
        for x in range(0, 5):
            for y in range(0, 5):
                print("%d,%d" % (x,y))
                code = pattern[y][x]
                pin_value = 1 if code == "#" else 0
                # If we're not connected to the GPIO pins use the matrix instead
                if pins:
                    pin_map[y].write_digital(pin_value)
                else:
                    display.set_pixel(x, y, pin_value*9)
            sleep(col_pause)

        # Add blank column to turn the pins off
        for y in range(0, 5):
            if pins:
                pin_map[y].write_digital(0)
            else:
                display.clear()

# increase the timing if we're running this on the matrix
multiplier = 1 if pin0.read_digital() else 100
col_pause = 1 * multiplier
letter_pause = 1 * multiplier
gap = 100 * multiplier

#use a to increase the delay after the reed switch and b to decrease it
if button_a.is_pressed():
    gap=gap+10
if button_b.is_pressed():
    gap=gap-10

word = "hello world"

while True:

    sleep(gap)

    for char in list(word):
        print_letter(char, pin0.read_digital())
