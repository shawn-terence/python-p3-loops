#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    t=10
    while t>0:
        print(f"{t}")
        t-=1
        
    pass
    print("Happy New Year!")
#happy_new_year()
def square_integers(int_list):
    # code goes here!
    number_list= [number * number for number in int_list]
    return(number_list)
    pass

def fizzbuzz():
    # code goes here!
    for num in range(1,101):
        if ((num%3==0)and (num%5==0)):
            print("FizzBuzz")
        elif(num%3==0):
            print("Fizz")
        elif(num%5==0):
            print("Buzz")
        else:
            print(num)
    pass
fizzbuzz()