let hand = 0
input.onGesture(Gesture.Shake, function () {
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showLeds(`
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            `)
        music.playSoundEffect(music.createSoundEffect(
        WaveShape.Noise,
        4191,
        1,
        177,
        80,
        300,
        SoundExpressionEffect.Vibrato,
        InterpolationCurve.Logarithmic
        ), SoundExpressionPlayMode.UntilDone)
    } else if (hand == 2) {
        basic.showLeds(`
            # # # # #
            # # . . #
            # # . # #
            # . # . #
            # # # # #
            `)
        music.playSoundEffect(music.createSoundEffect(
        WaveShape.Sine,
        3419,
        0,
        255,
        0,
        500,
        SoundExpressionEffect.None,
        InterpolationCurve.Linear
        ), SoundExpressionPlayMode.UntilDone)
    } else if (hand == 3) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
        music.playSoundEffect(music.createSoundEffect(
        WaveShape.Triangle,
        5000,
        0,
        255,
        0,
        100,
        SoundExpressionEffect.None,
        InterpolationCurve.Linear
        ), SoundExpressionPlayMode.UntilDone)
    }
})
basic.forever(function () {
	
})
