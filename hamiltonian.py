import numpy as np

#Pauli matrixes
sx = np.array([[ 0, 1],[ 1, 0]])
sy = np.array([[0,-1j],[1j, 0]])
sz = np.array([[ 1, 0],[0, -1]])
s = [sx, sy, sz]

#identity
Id = np.array([[1, 0],[0, 1]])    

#ladder operators
Sp = np.array([[0, 1],[0, 0]])   
Sm = np.array([[0, 0],[1, 0]])

#neighbour part of ising
def H1(N,k=3):
    H = []
    for i in range(N-1):
        if i == 0:
            M, nxt = s[k-1], True
        else:
            M, nxt = Id, False
        for j in range(N-1):
            if nxt == True:
                M, nxt = np.kron(M, s[k-1]), False
            elif j+1==i:
                M, nxt = np.kron(M, s[k-1]), True
            else:
                M, nxt = np.kron(M, Id),     False
        H.append(M) 
    return H

#transverse X and Z parts of Ising
def Hi(N, k=1):
    H = []
    for i in range(N):
        if i == 0:
            M = s[k-1]
        else:
            M = Id
        for j in range(N-1):
            if j+1 == i:
                M = np.kron(M,s[k-1])
            else:
                M = np.kron(M,Id)
        H.append(M)
    return H

#Ising Hamiltonian
def ising_h(N, J, h, g, k=1):
    return -J*sum(H1(N))-h*sum(Hi(N,3))-g*sum(Hi(N,k))    

#t1 term of XX
def T1(N):
    Hi=[]
    for i in range(N-1):
        if i == 0:
            M, nxt = Sp, True
        else:
            M, nxt = Id, False

        for j in range(N-1):
            if nxt == True:
                M, nxt = np.kron(M,Sm), False
            elif j+1 == i:
                M, nxt = np.kron(M,Sp), True
            else:
                M, nxt = np.kron(M,Id), False
        Hi.append(M)
    H = sum(Hi)+sum(Hi).conj().T
    return H

#t2 term of XX
def T2(N):
    Hi = []
    for i in range(N-2):
        if i == 0:
            M, nxt = Sp, 1
        else:
            M, nxt = Id, 0

        for j in range(N-1):
            if nxt == 1:
                M, nxt = np.kron(M,Id), 2
            elif nxt == 2:
                M, nxt = np.kron(M,Sm), 0
            elif j+1 == i:
                M, nxt = np.kron(M,Sp), 1
            else:
                M,nxt = np.kron(M,Id), 0
        Hi.append(M)
    H = sum(Hi)+sum(Hi).conj().T
    return H

#XX hamiltonian
def XX_h(N, t1, t2):
    return t1*T1(N)+t2*T2(N)
