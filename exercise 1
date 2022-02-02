import random as rad
mov=0
# winnimg conditions
def win (a,b,c):
    if (a==b and b==c) or (b==a+1 and c==b+1) or (b==c+1 and a==b+1):
        return 0
    return 1
# checking winning conditions 
def check(squ):
    for i in range(2):
        if win(squ[i],squ[i+3],squ[i+6]) == 0:
            return 0
    for i in range(0,7,3):
        if win(squ[i],squ[i+1],squ[i+2]) == 0:
            return 0
    if win(squ[0],squ[4],squ[8]) == 0:
        return 0
    if win(squ[2],squ[4],squ[6]) == 0:
        return 0
    return 1
# game
def game ():
    squ = [i for i in range (5,5*10,5)]
    dis = [0]*9 + [1]*9 +[2]*9
    global mov 
    for i in range(27):
        mov += 1
        b = rad.randrange(len(dis))
        while True:
            a = rad.randrange(9)
            if squ[a] != dis[b]:
                squ[a] = dis[b]
                dis.remove(dis[b])
                break
            else:
                continue
        if check(squ) == 0:
            break
    return 0
#play the game
for i in range(100):
    game()
print("The average moves for the game to finish are: ",mov / 100)
