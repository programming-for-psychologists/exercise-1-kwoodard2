#Square Exercise 13
'''Four squares rotate and can change in size and can stop and start.'''

import time
import sys
from psychopy import visual,event,core
        
def square_revolution(square_to_rotate,angle,speed):
    for i in square_to_rotate:
        i.draw()
    win.flip()
    core.wait(speed)
    while True:
        for i in square_to_rotate:
            i.ori+=angle
            i.draw()  
        win.flip()
        core.wait(speed)
        if event.getKeys(['q']): #quits screen
            break
        elif event.getKeys(['s']): #pause
            event.waitKeys(['r']) #unpause
        elif event.getKeys('left'): #make bigger
            for i in square_to_rotate:
                i.size *=1.1
                i.draw()
            win.flip()
        elif event.getKeys('right'): #make smaller
            for i in square_to_rotate:
                i.size *=0.9
                i.draw()
            win.flip()


win = visual.Window([400,400],color="black", units='pix')
red_square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[-50,0])
blue_square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100],pos=[50,0])
white_square = visual.Rect(win,lineColor="black",fillColor="white",size=[100,100],pos=[0,50])
pink_square = visual.Rect(win,lineColor="black",fillColor="pink",size=[100,100],pos=[0,-50])
event.clearEvents()
square_list =[red_square,blue_square,white_square,pink_square]
square_revolution(square_list,360.0/60,1.0/60)
win.close() 
sys.exit()

