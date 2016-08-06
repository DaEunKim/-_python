primes=[]

for i in range(2,31):
    bPrime = True
    for j in range(2, i//2+1):
        if(i%j==0):
            bPrime = False
    if bPrime ==True:
        primes.append(i)
print (primes)
'''
import math
prime=[]
for i in range(2, 31):
    bPrime = True
    for j in range(2, int(math.sqrt(i))+1):
        if(i%j==0):
            bPrime = False
    if(bPrime ==True):
        primes.append(i)
print(primes)
'''
