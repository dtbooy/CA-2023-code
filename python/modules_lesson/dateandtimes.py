#----------------------------------------------------------------------|
# Make a game for seeing how good people are at guessing when 10 
# seconds have elapsed. 
#     Tell them to hit enter key when ready
#     Get the first time in seconds
#     Get them to hit the enter key when they think 10 seconds have passed
#     Get the second time in seconds
#     Subtract first time from the second time
#     Tell them how close to 10 the answer was. 

import time

input("hit enter key when ready")
start = time.time()
input("hit enter key once 10 seconds have passed")
stop = time.time()
time_dif = stop - start
print(f"that was {time_dif} seconds!!")
print(f"You were {abs(time_dif - 10):.2f} seconds off!")