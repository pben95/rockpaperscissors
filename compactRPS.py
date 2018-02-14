import random
states, nums = {"rs" : "Win", "sp" : "Win", "pr" : "Win", "sr" : "Lose", "ps" : "Lose", "rp" : "Lose", "rr" : "Tie", "pp" : "Tie", "ss" : "Tie"}, ["r", "p", "s"]
while True:
    inp = input('Rock paper scissors (type r, s, or p)').lower()
    if inp in nums:
        print(states[inp+nums[random.randint(0,2)]])