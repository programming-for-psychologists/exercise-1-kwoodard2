# -*- coding: utf-8 -*-


#Exercise 4: Print this sequence:
#0
#01
#012
#0123
#01234
#012345

for i in range(7):
    for i in range(i):
        print i,
    print
