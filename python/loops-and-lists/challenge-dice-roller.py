#----------------------------------------------------------------------|
## Dice Roll

# In role-playing games, the standard notation for dice rolls is 
# [n]d[s], where `n` is the number of die to roll and `s` is how 
# many sides each die has. For example `2d6` means roll two six-sided 
# dice, `1d12` means roll one 12-sided die. 

# Write a function to simulate a role-playing game dice roll. The 
# function should accept a parameter which must conform to the standard 
# notation. Return `None` if the format is invalid. The function should
# generate a random roll for each die and return a list containing the 
# results.

# Example:
# ```py
# roll('2d6')     # [5, 2]
# roll('3d10')    # [1, 9, 7]
# ```
# ### Extra

# Modify the function so that, in addition to the list of rolls, it 
# also returns the sum of the rolled dice and the highest roll.

# Example:
# ```py
# roll('2d6')    # if result was [6, 3], returns [6,3] and 9 (sum) and
# 6 (highest)
# ```
import random

#define a function that will "roll a dice" of n number of faces
def roll(num_dice, dice_sides):
    #list roll outcome to be returned
    outcome = []
    for _ in range(num_dice):
        outcome.append(random.randint(1, dice_sides))
    return outcome

def get_valid_roll():
    #Infinite loop broken by return
    while True:
        #set valid code to True until invalid format found
        valid_code=True
        #roll request
        roll_requested = input(
            "enter dice to roll (format = [n]d[s])").lower()
        #Split multiple rolls into a [list] of rolls 
        roll_requested = roll_requested.split(",")
        #set an empty list to store our output (rolls)
        roll_list = []
        #validity test for each roll 
        for roll_code in roll_requested:
            #Find d in roll code 
            d_index = roll_code.find("d")
            #find outputs -1 if there is no "d" in string
            if d_index == -1:
                #if there's no d, send error msg 
                print(f"invalid format A: '{roll_code}'")
                #set invalid code tag
                valid_code=False
                continue
            #append roll code in format [num_dice, dice_sides] 
            # to roll_list
            try:
                roll_list.append([
                    int(roll_code[:d_index]),
                    int(roll_code[d_index+1:])])

            #if the results aren't integers the format is wrong
            except ValueError:
                print(f"invalid format B: '{roll_code}'")
                #set invalid code tag
                valid_code=False
                continue
        #check if no invalid code flags
        if valid_code:
            #return valid roll
            return roll_list
        #if invalid rolls detected restart loop

#---------------------------Main---------------------------------------|
#Print Instructions
print(
    '''Welcome to dice roller!!
    Instructions:
    Enter your dice roll in the form [n]d[s], where: 
        * [n] is the number of die to roll, and 
        * [s] is how many sides each die has. 
    For example :
        2d6 means roll two six-sided dice, 
        1d12 means roll one 12-sided die

    For multiple rolls seperate them with a comma[,]
    For example:
        2d6, 1d12, 6d4 will roll two six-sided dice, then one 12-sided
        dice, then six four-sided dice.

    '''
    )

#get a list of valid rolls in roll_code format from user input
roll_list = get_valid_roll()

#iterate over list of rolls to make
for roll_ind, roll_code in enumerate(roll_list):
    #roll_code in format [roll_num, dice_faces]
    output = roll(roll_code[0], roll_code[1])
    print(
        f"""{roll_ind+1}. You rolled {roll_code[0]}d{roll_code[1]}.
        Results: {output} = {sum(output)} 
        """)



