#Square Exercise 4
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix') #opens a window
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[0,0])
square.draw() #drawn to the backside but you can't see it
win.flip() #flip the screen to make what was drawn visible
core.wait(1.5) #pause for time (in seconds)
win.flip() #now screen is blank, #flip the screen to make what was drawn visible
core.wait(1)
for i in range(3):
    win.flip()
    square.draw()
    win.flip() #now show square again
    core.wait(0.03)
win.close() 
sys.exit()