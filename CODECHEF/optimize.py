from collections import Counter

def allsub(S,R):
    S1 = dict(Counter(S))
    R1 = dict(Counter(R))

    # Checking Substring possiblity
    check = 1
    for i, j in S1.items():
        if R1.get(i, 0) < j:
            check = 0
            break

    if check:
        Q = dict()
        for i, j in R1.items():
            if j - S1.get(i, 0) > 0:
                Q[i] = j - S1.get(i, 0)
        left, right = [], []

        if S < S[0]*len(S):
            for i, j in Q.items():
                if i < S[0]:
                    left.append(i*j)
                else:
                    right.append(i*j)
        else:
            for i, j in Q.items():
                if i <= S[0]:
                    left.append(i*j)
                else:
                    right.append(i*j)

        #left = ''.join(left)
        # print(left)
        left = sorted(left)
        # print(left)
        left = ''.join(left)
        #right = ''.join(right)
        # print(right)
        right = sorted(right)
        # print(right)
        right = ''.join(right)
        final = left + S + right

        print(final)

    else:
        print("Impossible")

##t = int(input())
##for _ in range(t):
##    S = input()
##    R = input()
##    allsub(S,R)

