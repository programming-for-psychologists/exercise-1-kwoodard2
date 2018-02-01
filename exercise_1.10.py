#Square Exercise 10
'''Display a blue square and increase its width (making it a rectangle) by 10 pixels
 whenever the user presses the left-arrow key. Decrease the width by 10 pixels
 when the user presses the right-arrow key'''

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
        square.size += 10
        square.draw()
        win.flip()
    elif event.getKeys('right'):
        square.size -= 10
        square.draw()
        win.flip()
win.close() 
sys.exit()