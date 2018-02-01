#Square Exercise 5
import time
import sys
from psychopy import visual,event,core

def draw_square_wait(object_to_draw, time, wait):
    object_to_draw.draw() #drawn to the backside but you can't see it
    win.flip() #flip the screen to make what was drawn visible
    core.wait(time)
    win.flip()
    core.wait(wait)

win = visual.Window([400,400],color="black", units='pix') #opens a window
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[0,0])
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100],pos=[0,0])
for i in range(3):
    draw_square_wait(square_blue,1,0.5)
    draw_square_wait(square_red,1,0.5)
win.close() 
sys.exit()