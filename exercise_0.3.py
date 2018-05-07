# -*- coding: utf-8 -*-


#Exercise 3: With list ['one', 'two','three','four'], print: 'one and a two and a three and a four'
numbers = ['one','two','three','four']

for number in numbers:
    print number,
    if number != "four":
        print "and a",
