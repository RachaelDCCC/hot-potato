def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)
timer = 0
timer = randint (5, 15)
basic.show_icon(IconNames.CHESSBOARD)
basic.pause(1000 * timer)
basic.show_icon(IconNames.SKULL)
basic.pause(1000 * randint(5, 15))