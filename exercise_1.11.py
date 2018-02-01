#Square Exercise 11
'''Make the rectangle decrease/increase its width by 10% of its current width 
with each keypress instead of 10 pixels'''

import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
square.draw()
win.flip()
while True:
    if event.getKeys(['q']):
        break
    elif event.getKeys('left'):
        square.size *=1.1
        square.draw()
        win.flip()
    elif event.getKeys('right'):
        square.size *=0.9
        square.draw()
        win.flip()
win.close() 
sys.exit()