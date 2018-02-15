import random
states, rps = {"rs" : "Win", "sp" : "Win", "pr" : "Win", "sr" : "Lose", "ps" : "Lose", "rp" : "Lose", "rr" : "Tie", "pp" : "Tie", "ss" : "Tie"}, ["r", "p", "s"]
score = {"Win" : 0, "Lose" : 0, "Tie" : 0}
while True:
    inp, opp = input('Rock paper scissors (type r, p, or s)').lower(), random.randint(0, 2)
    if inp in rps:
        score[states[inp + rps[opp]]] += 1
        print(states[inp+rps[opp]], score)