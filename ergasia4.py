# Convert ASCII value to binary
def strtobinary(s):
    ar = []
    for c in s:
        ascval = ord(c)
        binval = bin(ascval)
        ar.append(binval[2:])
    return (' '.join(ar))
with open('textf.txt',mode='r') as text:
    alpha = ''
    for alfar in text:
       alpha += strtobinary(alfar) + ' '
    words = alpha.split()
    for i in range(len(words)):
        if len(words[i]) < 7:
            b = '0'*(7 - len(words[i])) + words[i]
            words[i] = b
    alpha = ''.join(words)
    rep1 = 0
    rep2 = 0
    for bi in ['0','1']:
        for i in alpha:
            if i == bi:
                rep1 += 1
            else:
                if rep1 > rep2:
                    rep2 = rep1
                rep1 = 0
        if rep1 > rep2:
            rep2 = rep1
        print("the largest ammount of continued",bi," \'s are",rep2)
        rep2 = 0
        rep1 = 0
    text.close()
