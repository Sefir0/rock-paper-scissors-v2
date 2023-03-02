hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            . # # # .
                        # # # # #
                        # # # # #
                        # # # # #
                        . # # # .
        """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                4191,
                1,
                177,
                80,
                300,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_leds("""
            # # # # #
                        # # . . #
                        # # . # #
                        # . # . #
                        # # # # #
        """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                3419,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif hand == 3:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                5000,
                0,
                255,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
