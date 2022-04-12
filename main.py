displej = 5
osaX = 2
trojuhelnik = [[0, randint(0, displej-1)], [1, randint(0, displej-1)], [2, randint(0, displej-1)]]
#OSA
def draw_osaX():
    for i in range(displej):
        led.plot_brightness(osaX, i, 100)
#BODY
def klm():
    for bod in trojuhelnik:
        led.plot(bod[0], bod[1])
#MIRROR
def mirror():
    for bod in trojuhelnik:
            led.plot(abs(bod[0]-4), bod[1])
#ZABLIKANI
for a in range(3):
    draw_osaX()
    klm()
    mirror()
    basic.pause(1000)
    basic.clear_screen()
    draw_osaX()
    basic.pause(1000)