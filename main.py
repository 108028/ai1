def on_gesture_screen_down():
    basic.show_string("Im a AI")
    basic.show_leds("""
        . # # # .
                . # . # .
                . # # # .
                . # . # .
                . # . # .
    """)
    basic.show_leds("""
        . . # . .
                . . . . .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # # .
                . # . . .
                # . # # #
    """)
    basic.show_leds("""
        . # # . .
                # . . # .
                . . # . .
                . . . . .
                . . # . .
    """)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_a():
    basic.show_leds("""
        . # # . .
                . # . . .
                . # . . .
                # # . . .
                # # . . .
    """)
    music.play_melody("C5 A B G A F G E ", 120)
    music.play_melody("G B A G C5 B A B ", 120)
    basic.show_leds("""
        # # # . .
                # . # . .
                # . # . .
                # . # . .
                # # # . .
    """)
    basic.show_leds("""
        # # . . .
                . # . . .
                . # . . .
                . # . . .
                # # . . .
    """)
    basic.show_leds("""
        # . . . #
                # . . . #
                # . . . #
                # . . . #
                # . . . #
    """)
    basic.show_leds("""
        . . . # .
                . . . # .
                . . . # #
                . . . # .
                . . . # .
    """)
    basic.show_leds("""
        . . # . .
                . . # . #
                . . # # .
                . . # . #
                . . # . .
    """)
    basic.show_leds("""
        . # . . #
                . # . # .
                . # # . .
                . # . # .
                . # . . #
    """)
    basic.show_leds("""
        # . . # .
                # . # . .
                # # . . .
                # . # . .
                # . . # .
    """)
    basic.show_leds("""
        . . # . .
                . # . . .
                # . . . .
                . # . . .
                . . # . .
    """)
    basic.show_leds("""
        . # . . .
                # . . . .
                . . . . .
                # . . . .
                . # . . .
    """)
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
    """)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . # . # .
                # . # . #
    """)
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
                # . # . #
                # . # . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . # .
                . . . . #
                # . . . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . # # .
                . . . . #
                . . . . #
                # . . . #
                . # # # .
    """)
    basic.clear_screen()
    music.play_tone(349, music.beat(BeatFraction.DOUBLE))
    serial.redirect_to_usb()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_string("Boy Boy")
    basic.show_leds("""
        . . # . .
                # . # . #
                # . # . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                # . # . #
                # . # . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . # . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . # # # .
    """)
    for index in range(9999999999):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global _1
    basic.show_leds("""
        # # # # .
                # . # . #
                # . # # #
                # . . . #
                # # # # #
    """)
    basic.show_leds("""
        # # . . #
                # # . # .
                . . # . .
                # # . # .
                # # . . #
    """)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        # # # # .
                # . # . #
                # . # # #
                # . . . #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    _1 = 0
    _1 = randint(1, 2)
    if _1 == 1:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        """)
    elif 0 == 0:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    else:
        basic.show_leds("""
            # # # # .
                        # . # . #
                        # . # # #
                        # . . . #
                        # # # # #
        """)
    basic.pause(5000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # . . .
                # # . . .
                # # # # .
                # # # # .
                # # # # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

_1 = 0
basic.show_leds("""
    . # # # .
        # . . . .
        # . . # #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        # # # . #
        # . # . .
        # # # . #
        # . # . #
""")
basic.show_leds("""
    . . . . .
        # . . . #
        # # # . .
        # . # . #
        # . # . #
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")

def on_forever():
    pass
basic.forever(on_forever)
