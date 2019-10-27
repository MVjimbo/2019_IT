import numpy as np
import math
import matplotlib.pyplot as plt

def Paretto(X):
    y=[]
    for i,x1 in enumerate(X):
        indec=True
        for j,x2 in enumerate(X):
            if i!=j:
                if not(np.any(x1>x2)):
                    indec=False
                    break
        if indec:
            y.append(x1)
    return y




X=np.array([[1,1,3],
           [3,2,4],
           [2,3,1]],dtype=float)
P=np.array(Paretto(X))

n,m=np.shape(X)

corner=2*math.pi/3

Y=np.zeros_like(X,dtype=float)

for i in range(m):
    arr=np.array([Y[:,i],
                  X[:,i]])
    OrtT=np.array([[math.cos(i*corner), math.sin(i*corner)],
               [-math.sin(i*corner),math.cos(i*corner)]])
    arr=OrtT.dot(arr)
    X[:,i]=arr[0]
    Y[:,i]=arr[1]


X_out=np.zeros(shape=(n,m+1))
Y_out=np.zeros(shape=(n,m+1))
for i in range(m):
    X_out[:,i]=X[:,i]
    Y_out[:,i]=Y[:,i]
X_out[:,m]=X[:,0]
Y_out[:,m]=Y[:,0]

for i in range(n):
    plt.plot(X_out[i],Y_out[i],color="b",marker="o")



#Paretto
nP,mP=np.shape(P)

PY=np.zeros_like(P,dtype=float)

for i in range(mP):
    arr=np.array([PY[:,i],
                  P[:,i]])
    OrtT=np.array([[math.cos(i*corner), math.sin(i*corner)],
               [-math.sin(i*corner),math.cos(i*corner)]])
    arr=OrtT.dot(arr)
    P[:,i]=arr[0]
    PY[:,i]=arr[1]

P_out=np.zeros(shape=(nP,mP+1))
PY_out=np.zeros(shape=(nP,mP+1))
for i in range(mP):
    P_out[:,i]=P[:,i]
    PY_out[:,i]=PY[:,i]
P_out[:,m]=P[:,0]
PY_out[:,m]=PY[:,0]

for i in range(nP):
    plt.plot(P_out[i],PY_out[i],color="r",marker="o",linewidth=2)
plt.show()