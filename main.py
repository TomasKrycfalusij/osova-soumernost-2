displej = 5
osaX = 2
#OSA
def draw_osaX():
    for i in range(displej):
        led.plot_brightness(osaX, i, 100)

#BODY
A = 0
def rozhod_body():
    global displej, A
    A = [2, randint(0, displej-1)]
    B = [randint(0,1), randint(0, displej-1)]
    C = [randint(0,1), randint(0, displej-1)]
    if B == C:
        rozhod_body()
rozhod_body()
print(A)

#def zobrazeni_bodu():
#led.plot(A[0], A[1])




for a in range(3):
    draw_osaX()
    #zobrazeni_bodu()
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)