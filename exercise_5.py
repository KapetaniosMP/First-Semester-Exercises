popu =[] 
difwor=[]
def biggest(a):
    for i in range(a):
        a=difwor[i]
        b=popu[i]
        c=popu.index(max(popu[i:]))
        difwor[i]=difwor[c]
        popu[i]=max(popu[i:])
        difwor[c] = a
        popu[c]= b
        return 0
with open('two_cities_ascii.txt',mode='r') as text:
    alpha = ""
    for alfar in text:
        a =[i for i in alfar]
        for i in a:
            if not (i.isalpha() or i == " "):
              continue
            elif i.isalpha():
                i=i.lower()
          # to alpha exei mono mikra grammata kai space
            alpha += i
    words = alpha.split()
    # a)
    for i in words:
        if not(i in difwor):
            popu.append(words.count(i))
            difwor.append(i)
    biggest(10)
    print("the most popular words are: ",difwor[:10] )
    # b)
    popu =[] 
    difwor=[]
    for i in words:
        if not(i[:2] in difwor):
            popu.append(words.count(i[:2]))
            difwor.append(i[:2])
    biggest(3)
    print("the three most usual first two letters are: ",difwor[:3] )
    # c)
    popu =[] 
    difwor=[]
    for i in words:
        if not(i[:3] in difwor):
            popu.append(words.count(i[:3]))
            difwor.append(i[:3])
    biggest(3)
    print("the three most usual first three letters are: ",difwor[:3] )
    text.close()
