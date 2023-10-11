#main.py

#to use a relative directory to find modules use . indtead of /
import stuff.functions as funky

import sys

print("And the answer to the equation is...")

answer = funky.sum(3, 6)
print(answer)

print("The paths that Python looks for modules is...")
print(sys.path)