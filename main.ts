input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
})
let timer = 0
timer = randint(5, 15)
basic.showIcon(IconNames.Chessboard)
basic.pause(1000 * timer)
basic.showIcon(IconNames.Skull)
basic.pause(1000 * randint(5, 15))
