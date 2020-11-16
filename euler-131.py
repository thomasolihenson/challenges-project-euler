from project_euler_all_functions import *
import time
Primes = []
PrimeCubes = []
PrimeCubeCount = 0
loops = 0

def LoopValueN(Prime):
    global loops
    for n in range(0,577):
        if (((n+1)**3)-(n**3)) == Prime:
            print("Found value P:",Prime,"N:",n)
            PrimeCubes.append("P: "+str(Prime)+",N: "+str(n))
            MinimumN = n
            n = 100000000000000000000000000000000000000000
        loops += 1
        n += 1

def Main(MaxVal):
    for x in range(0,MaxVal):
        if isPrime(x) == True:
            Primes.append(x)
    for p in Primes:
        LoopValueN(p)
    print("There are",len(PrimeCubes),"primes below",MaxVal,"that meet the conditions. These are:")
    print(PrimeCubes)
    print("Loops:",loops)
