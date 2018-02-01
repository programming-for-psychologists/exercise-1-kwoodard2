#Square Exercise 12
'''Show two rotating squares simultaneously, one left of center rotating clockwise,
 the other right of center, rotating counterclockwise'''

import time
import sys
from psychopy import visual,event,core
        
def square_revolution(square1,square2,angle,speed):
    square1.draw()
    square2.draw()
    win.flip()
    core.wait(speed)
    while True:
        square1.ori+=angle
        square2.ori-=angle
        square1.draw()
        square2.draw()
        core.wait(speed)
        win.flip()
        if event.getKeys(['q']):
            break

'''because screen refresh is 60 Hz, it means that the refreshes 60 times / second. Therefore
I can't do the rotation in increments of 1 degree (1/360) because that would not match the refresh rate.
Instead, it makes the most sense to use the speed of 1/60 with orientation shifts of 360/60)'''

win = visual.Window([400,400],color="black", units='pix')
red_square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[-50,0])
blue_square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100],pos=[50,0])
event.clearEvents()
square_revolution(red_square,blue_square,360.0/60,1.0/60)
win.close() 
sys.exit()

