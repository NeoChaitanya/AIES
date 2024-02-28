import time
import itertools

def solution1():
    letters = ('s','e','n','d','m','o','r','y')
    digits = range(10)
    
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters,perm))
        if sol['s'] == 0 or sol['m'] == 0:
            continue
        
        send = 1000*sol['s'] + 100*sol['e'] + 10*sol['n'] + 1*sol['d']
        more = 1000*sol['m'] + 100*sol['o'] + 10*sol['r'] + 1*sol['e']
        
        money = 10000*sol['m'] + 1000*sol['o'] + 100*sol['n'] + 10*sol['e'] + 1*sol['y']
        
        if send + more == money:
            print("  S E N D\n+ M O R E\n----------\nM O N E Y")
            return send, more, money
        
print(solution1())
        
        
        
def solution2():
    letters = ('c','r','o','s','a','d','n','g','e')
    digits = range(10)
    
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters,perm))
        if sol['c'] == 0 or sol['r'] == 0:
            continue
        
        cross = 10000*sol['c'] + 1000*sol['r'] + 100*sol['o'] + 10*sol['s'] + 1*sol['s']
        roads = 10000*sol['r'] + 1000*sol['o'] + 100*sol['a'] + 10*sol['d'] + 1*sol['s']
        
        danger =  100000*sol['d'] + 10000*sol['a'] + 1000*sol['n'] + 100*sol['g'] + 10*sol['e'] + 1*sol['r']
        
        if cross + roads == danger:
            print("  C R O S S\n+ R O A D S\n----------\nD A N G E R")
            return cross, roads, danger
        
print(solution2())
        