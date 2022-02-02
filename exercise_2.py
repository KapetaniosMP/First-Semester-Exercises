with open('text.txt',mode='r') as text:
    alpha = ""
    for alfar in text:
        a =[i for i in alfar]
        for i in a:
            if not (i.isalpha() or i == " "):
              continue
          # to alpha exei mono grammata kai space
            alpha += i
    words = alpha.split()
    print(words)
    stat1 = [1]
    stat2 = [0]
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[j] == '1':
                break
            elif len(words[i]) + len(words[j]) == 20:
                words[j] = '1'
                words[i] = '1'
                print(words[i])
                break
        if words[i] == '1':
            continue
        if len(words[i]) in stat1:
            stat2[stat1.index(len(words[i]))] += 1 
        else:
            stat1.append(len(words[i])) 
            stat2.append(1)
    while('1' in words):
        words.remove('1')
    for i in range(len(stat1)):
        print(stat2[i],'words with',stat1[i],'letters')
    text.close()
