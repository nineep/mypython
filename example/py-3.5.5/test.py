#!/usr/bin/env python3

def area(width, height):
    return width * height

def print_welcome(name):
    print("welcome", name)

print_welcome("run")
w = 4
h = 5
print("width = ", w, " height = ", h, " area =", area(w, h))
