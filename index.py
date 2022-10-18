def pushA():
    global x
    led.unplot(x, y)
    x += -1
    led.plot(x, y)
input.on_button_pressed(Button.A, pushA)

def pushB():
    global x
    led.unplot(x, y)
    x += 1
    led.plot(x, y)
input.on_button_pressed(Button.B, pushB)
x = 2
y = 3
led.plot(x, y)
while True:
    if led.point(0, 2) == True and led.point(1, 2) == True and led.point(2, 2) == True and led.point(3, 2) == True and led.point(4, 2) == True:
        basic.show_string("YOU WIN")
    y_e = 0
    x_e = randint(0, 5)
    led.plot(x_e, y_e)
    for i in range(6):
        if y_e == y and x_e == x:
            print("k")
        else:
            led.unplot(x_e, y_e - 1)
        led.plot(x_e, y_e)
        y_e += 1
        basic.pause(500)
