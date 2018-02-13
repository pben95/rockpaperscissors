import random  #for opponent's random choice
def rps(inp):
    states = {"rs" : 0, "sp" : 0, "pr" : 0, "sr" : 1, "ps" : 1, "rp" : 1, "rr" : 2, "pp" : 2, "ss" : 2}  #all possible game states, either win 0 lose 1 or tie 2
    nums = ["r", "p", "s"]  #converts random.randint into r p or s
    try:  #just in case you fat finger the wrong key and don't put r p or s :)
        if inp == "r" or inp == "p" or inp == "s":
            opp = nums[random.randint(0,2)]  #opponents choice
            if states[inp+opp] == 0:  #if win state 0 (your choice beats opps)
                print("You played " + inp + ", opponent played " + opp +", you win!")
            elif states[inp+opp] == 1: #if lose state 1 (opps choice beats yours))
                print("You played " + inp + ", opponent played " + opp + ", you lose!")
            elif states[inp+opp] == 2:  #if tie state 2 (same choices)
                print("You played " + inp + ", opponent played " + opp + ", you tie!")
    except ValueError:  #restarts loop if you don't put in a valid entry
        return
while True:
    rps(input('Rock paper scissors (type r, s, or p)').lower())  #loops forever, makes all inputs lowercase