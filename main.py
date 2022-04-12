displej = 5
osaX = 2

#OSA
def draw_osaX():
    for i in range(displej):
        led.plot_brightness(osaX, i, 100)

#BODY
A = [2, randint(0, 4)]

def zobrazeni_bodu():
    led.plot(A[0], A[1])




for a in range(3):
    draw_osaX()
    zobrazeni_bodu()
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)