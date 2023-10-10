#-------------------Max-line-length-is-72-characters-------------------|

# Write a function to calculate the score for one "frame" of ten-pin 
# bowling. An entire game consists of 10 frames, with up to 2 balls 
# bowled per frame.

# Due to how the scoring works, you will need to know how many pins 
# were knocked down by the last 3 balls bowled in order to calculate 
# the total score for the frame.

# The scoring rules are:
# - 1 point for each pin knocked down (so between 0 and 10)
# - If it's a strike (all 10 pins knocked down with 1 ball), add the 
#   total of the next 2 balls
# - If it's a spare (all 10 pins knocked down with 2 balls), add the 
#   next ball

# Example calls with output:
# ```py
# calc_frame(6, 2, 9)     # 8
# calc_frame(10, 6, 2)    # 18
# calc_frame(7, 3, 4)     # 14
# calc_frame(0, 10, 5)    # 15
# calc_frame(5, 0, 10)    # 5
# ```

    #frame0, frame1, frame2 should be lists with up to 2 values eg:
    # [3,0] - 3 points, 
    # [8,2] - spare, 
    # [10] - strike   
def calc_frame(frame0, frame1, frame2):
    #There will be 3 cases
    # 1. Normal bowl (for me) less than 10
    if sum(frame0) < 10: 
        return sum(frame0)
    # 2. Spare 
    elif sum(frame0) == 10 and frame0[0] != 10: 
        return sum(frame0) + frame1[0]
    # 3. Strike / double strike
    else:
        #double strike frame1 = [10]
        if frame1[0] == 10:
            #total of frame0 (10) plus total of frame1 (10) + first bowl of frame2
            return  frame0[0] + frame1[0] + frame2[0]
        else: 
            #frame 2 is not a strike, return sum of frame 2 + 10 points for frame 1
              return frame0[0] + sum(frame1)
    

#main
#tests
#test 1 - got nothing
test = [[0 , 0], [3, 5], [10]]
out = calc_frame(test[0], test[1], test[2])
print(test, out,"\nshould be 0?")

#test 2 - spare then strike then strike
test = [[5 , 5], [10], [10]]
out = calc_frame(test[0], test[1], test[2])
print(test, out,"\nshould be 20?")

#test 3 Strike, spare
test = [[10], [3, 5], [5, 2]]
out = calc_frame(test[0], test[1], test[2])
print(test, out, "\nshould be 18?")

#test 3 Strike, strike spare
test = [[10], [10], [1, 9]]
out = calc_frame(test[0], test[1], test[2])
print(test, out,"\nshould be 21?")

#test 3 Strike, strike strike
test = [[10], [10], [10]]
out = calc_frame(test[0], test[1], test[2])
print(test, out,"\nshould be 30?")
