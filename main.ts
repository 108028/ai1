input.onGesture(Gesture.ScreenDown, function () {
    basic.showString("Im a AI")
    basic.showLeds(`
        . # # # .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        `)
    basic.showLeds(`
        . . # . .
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # . . .
        # . # # #
        `)
    basic.showLeds(`
        . # # . .
        # . . # .
        . . # . .
        . . . . .
        . . # . .
        `)
})
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . # # . .
        . # . . .
        . # . . .
        # # . . .
        # # . . .
        `)
    music.playMelody("C5 A B G A F G E ", 120)
    music.playMelody("G B A G C5 B A B ", 120)
    basic.showLeds(`
        # # # . .
        # . # . .
        # . # . .
        # . # . .
        # # # . .
        `)
    basic.showLeds(`
        # # . . .
        . # . . .
        . # . . .
        . # . . .
        # # . . .
        `)
    basic.showLeds(`
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        `)
    basic.showLeds(`
        . . . # .
        . . . # .
        . . . # #
        . . . # .
        . . . # .
        `)
    basic.showLeds(`
        . . # . .
        . . # . #
        . . # # .
        . . # . #
        . . # . .
        `)
    basic.showLeds(`
        . # . . #
        . # . # .
        . # # . .
        . # . # .
        . # . . #
        `)
    basic.showLeds(`
        # . . # .
        # . # . .
        # # . . .
        # . # . .
        # . . # .
        `)
    basic.showLeds(`
        . . # . .
        . # . . .
        # . . . .
        . # . . .
        . . # . .
        `)
    basic.showLeds(`
        . # . . .
        # . . . .
        . . . . .
        # . . . .
        . # . . .
        `)
    basic.showLeds(`
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        `)
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        # . # . #
        `)
    basic.clearScreen()
    basic.showLeds(`
        . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . . # .
        . . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . # # #
        . . . . #
        . . # . #
        # # . . #
        . # # # .
        `)
    basic.clearScreen()
    music.playTone(349, music.beat(BeatFraction.Double))
    serial.redirectToUSB()
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Boy Boy")
    basic.showLeds(`
        . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # . # . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . # # # .
        `)
    for (let index = 0; index < 9999999999; index++) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        # # # # .
        # . # . #
        # . # # #
        # . . . #
        # # # # #
        `)
    basic.showLeds(`
        # # . . #
        # # . # .
        . . # . .
        # # . # .
        # # . . #
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        # # # # .
        # . # . #
        # . # # #
        # . . . #
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    _1 = 0
    _1 = randint(1, 2)
    if (_1 == 1) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    } else if (0 == 0) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            # # # # .
            # . # . #
            # . # # #
            # . . . #
            # # # # #
            `)
    }
    basic.pause(5000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # . . .
        # # . . .
        # # # # .
        # # # # .
        # # # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
let _1 = 0
basic.showLeds(`
    . # # # .
    # . . . .
    # . . # #
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    # # # . #
    # . # . .
    # # # . #
    # . # . #
    `)
basic.showLeds(`
    . . . . .
    # . . . #
    # # # . .
    # . # . #
    # . # . #
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.forever(function () {
	
})
