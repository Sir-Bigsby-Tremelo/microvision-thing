from microbit import *

pins = [
    pin16,
    pin15,
    pin14,
    pin13,
    pin12
]

alphabet = {
    "e": [
        "#####",
        "#    ",
        "#####",
        "#    ",
        "#####"
    ],
    "h": [
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #"
    ],
    "l": [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####"
    ],
    "o": [
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ]
}

def print_letter(letter, pins = True):
    print(letter)
    pattern = alphabet[letter]

    if pattern:

        sleep(time_1)
        for x in range(0, 5):
            for y in range(0, 5):
                print("%d,%d" % (x,y))
                code = pattern[y][x]
                pin_value = 1 if code == "#" else 0
                if pins:
                    pins[y].write_digital(pin_value)
                else:
                    display.set_pixel(x, y, pin_value*9)
            sleep(time_)

        for y in range(0, 5):
            if pins:
                pins[y].write_digital(0)
            else:
                display.clear()

time_  = 1
time_1 = 1
gap = 100
#use a to increase the delay after the reed switch and b to decrease it
if button_a.is_pressed():
    gap=gap+10
if button_b.is_pressed():
    gap=gap-10

word = "hello"

while True:

    sleep(gap)

    for char in list(word):
        print_letter(char, pin0.read_digital())
