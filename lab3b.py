#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: hiruthayathas

def sum_numbers(number1="Default", number2="Default"):
    # Make this function add number1 and number2 and return the value

    fin_num = int(number1) + int(number2)
    return fin_num

def subtract_numbers(number1="Default", number2="Default"):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments

    fin_num = int(number1) - int(number2)
    return fin_num

def multiply_numbers(number1="Default", number2="Default"):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments

    fin_num = int(number1) * int(number2)
    return fin_num

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
        