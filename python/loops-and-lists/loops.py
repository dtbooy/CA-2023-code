# spam = 0
# while spam < 5:
#     print("hello")
#     spam += 1

# print("done")

# for spam in range (1, 11, 3):
#     print(f"hello {spam}")

import random

count = int(input("How many random integers? "))
for i in range(count):
    print(random.randint(1,100))
    
