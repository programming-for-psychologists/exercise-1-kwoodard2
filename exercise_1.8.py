#Square Exercise 8
import time
import sys
from psychopy import visual,event,core
        
def square_revolution(square_to_rotate,angle,speed):
    square_to_rotate.draw()
    win.flip()
    core.wait(speed)
    while True:
        square_to_rotate.ori+=angle
        square_to_rotate.draw()
        core.wait(speed)
        win.flip()
        if event.getKeys(['s']):
            break

'''because screen refresh is 60 Hz, it means that the refreshes 60 times / second. Therefore
I can't do the rotation in increments of 1 degree (1/360) because that would not match the refresh rate.
Instead, it makes the most sense to use the speed of 1/60 with orientation shifts of 360/60)'''

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
event.clearEvents()
square_revolution(square,360.0/60,1.0/60)
win.close() 
sys.exit()

