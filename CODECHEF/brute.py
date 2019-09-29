def lex(s):
    s = sorted(s)
    s = ''.join(s)
    return s


def allsub(p,q):
    #q = lex(q)
    flag = True
    p = list(p)
    q = list(q)
    for i in p:
        if i in q:
            index = q.index(i)
            q.pop(index)
        else:
            flag = False
            break
    if flag == False:
        print('Impossible')
    else:
        p = ''.join(p)
        q.append(p)
        q = lex(q)
        print(q)

##t = int(input())
##while(t):
##    t-=1
##    p = input()
##    q = input()
##    allsub(p,q)

