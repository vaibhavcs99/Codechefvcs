import brute
import optimize as opti
import itertools as it

z = ['a','b']
p = []
for i in range(5):
    p.extend(list(it.combinations_with_replacement(z,i)))
p.pop(0)
for i in range(len(p)):
    p[i] = list(p[i])
    p[i] = ''.join(p[i])

q = []
for i in range(5,20):
    q.extend(list(it.product(z,repeat=i)))
for i in range(len(q)):
    q[i] = list(q[i])
    q[i] = ''.join(q[i])

for i in p:
    for j in q:
        try:
            if brute.allsub(i,j)!=opti.allsub(i,j):
                print(i,'',j)
                print('answer of brute',brute.allsub(i,j))
                print('answer of opti',opti.allsub(i,j))
        except:
            print('ERROR',i,j)
