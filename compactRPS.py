import random
states, rps = {"rs" : "Win", "sp" : "Win", "pr" : "Win", "sr" : "Lose", "ps" : "Lose", "rp" : "Lose", "rr" : "Tie", "pp" : "Tie", "ss" : "Tie"}, ["r", "p", "s"]
while True:
    inp = input('Rock paper scissors (type r, p, or s)').lower()
    if inp in rps:
        print(states[inp+rps[random.randint(0,2)]])