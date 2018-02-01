#Square Exercise 1
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square.draw()
win.flip()
core.wait(.5) #pause for 500 ms (half a second)
win.close() 
sys.exit()
