import numpy as np
import matplotlib.pyplot as plt

def listaElofordulas(lista):
    l=len(lista)
    tomb=np.zeros(l)
    for i in lista:
        tomb[i]+=1
    print(tomb)
    tobbseg=l/2
    max=0
    elem=0
    for i in range(l):
        if tomb[i]>max:
            max=tomb[i]
            elem=i

    if max>tobbseg:
        print(f"A(z) {elem}. elem többségében szerepel a listában, mivel {int(max)} alkalommal fordul elő")
    else:
        print(f"Nincs többségében előforduló elem a listában viszont a(z) {elem}. elem legtöbbször fordul elő, számszerint {int(max)} alkalommal")

    plt.bar(range(l), tomb)
    plt.title("Listaelem többség vizualizáció")
    plt.xlabel("A lista elemei")
    plt.ylabel("A lista elemeinek előfordulása")
    plt.show()

lista = [7,5,3,3,5,8,3,3,3,3,4]
v=listaElofordulas(lista)
print(v)

