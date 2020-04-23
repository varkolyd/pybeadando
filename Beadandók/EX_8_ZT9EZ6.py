N=7             #házi feladatok száma
B=3             #szünet ideje
M=10            #feladat megoldásának ideje
x=0             #feladat megoldásának végleges ideje
d=0             #kezdet, illetve szünet után megoldott feladatok száma
Nmaradek=N      #A megmaradt feladatok száma

for i in range(N):
    if i==0:
        print(f"Móriczka {N} feladatot fog megoldani, és most kezdi az elsőt.")
    if d>=Nmaradek:
        d=1
        Nmaradek-=1
        x+=M
        x+=B
        M*=2
        print(f"Móriczka megoldott {N-Nmaradek} feladatot. Még {Nmaradek} db feladat van hátra, és {x} perc telt el eddig.")
    else:
        d+=1
        Nmaradek-=1
        x+=M
        print(f"Móriczka megoldott {N-Nmaradek} feladatot. Még {Nmaradek} db feladat van hátra, és {x} perc telt el eddig.")


if Nmaradek==0:
    print(f"Nem maradt több feladat hátra, összesen {x} percnyi időt vett igénybe {N} feladat megoldása")