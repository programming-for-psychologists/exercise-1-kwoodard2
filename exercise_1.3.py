#Square Exercise 3
import time
import sys
from psychopy import visual,event,core
 
def draw_square(object_to_draw, time):
    object_to_draw.draw() #drawn to the backside but you can't see it
    win.flip() #flip the screen to make what was drawn visible
    core.wait(time)
    

win = visual.Window([400,400],color="black", units='pix') #opens a window
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[0,0])
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100],pos=[0,0])
draw_square(square_red,1)
draw_square(square_blue,1)
win.flip()
win.close() 
sys.exit()
