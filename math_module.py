import math


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b


def power_numbers(a, b):
    return a ** b


def square_root(a):
    return math.sqrt(a)


def modulus(a, b):
    return a % b


def get_two_numbers(prompt):
    user_input = input(prompt)
    parts = user_input.split()
    return map(float, parts)


def get_one_number(prompt):
    user_input = input(prompt)
    return float(user_input)
