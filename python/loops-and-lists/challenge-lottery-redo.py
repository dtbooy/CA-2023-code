#a function that printed 6 random numbers until they got the correct set

import random

lottery_nums = set()
my_nums = {6, 21, 28, 5, 40, 10}
count = 0 # set the count
while len(lottery_nums & my_nums) != 6: # 4 numbers for a win
    count +=1
    lottery_nums.clear()
    while len(lottery_nums) < 6: #get a set() of 6 unique lottery numbers
        lottery_nums.add(random.randint(1,47))

print(count)