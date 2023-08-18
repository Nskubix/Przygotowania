M = 17
for N in range(1,1800):
    A = [N,]
    for k in range(100000):
        if(A[k] == 1):
            break
        elif(A[k] % 2 == 0):
            A.append(A[k]/2)
        elif(A[k] % 2 == 1):
            A.append(3*A[k] +1)   
    if(len(A) == M):
        print(N)
        break
    A = []