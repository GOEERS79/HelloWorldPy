import random
import sys
import os


from myModules.methods import mysum


#print('Hello World from Python 3')

#single line comment

'''

multi line comment

Types: Numbers Strings Lists Tuples Dictionaries

operators: + - * / % **  //
'''

#quote = '\"Single line quote\"'
#multi_line = ''' This is a multi line quote'''

#new_string = quote + multi_line
#print("new string = ",new_string)

#print('%s %s %s' %('I like it',quote,multi_line))


if __name__ == '__main__':

    print('hello python ....')

    print('sum is ', mysum(1, 1))

    print('FLOOR: 5//2 = ', 5 // 2)

    # LISTS
    grocery_list = ['juice', 'cerial', 'bananas']
    s = grocery_list[1:3]
    print('Modified list = ', s)
    other_list = ['Get Car', 'Shopping']

    list_events = [grocery_list, other_list]
    print(list_events)
    print(list_events[0][1])
    print(len(list_events))
    print(len(grocery_list))

    # TUPLES

    py_tuple = (1, 2, 3, 4, 'T')
    print('py tuple = ', py_tuple)
    print('py tuple [4]= ', py_tuple[4])
    py_tuple2 = (5, 2, 3, 4, 'U')
    py_tuple3 = py_tuple + py_tuple2
    print(py_tuple3)

    # conditionals: if else elif

    age = 16
    if age > 16:
        print('You can drive')
    else:
        print('You are not 16 yet')

    # logical operators:  and or not

    if ((age >= 1) and (age <= 18)):
        print('You are sonewhere between 1 and 18')

