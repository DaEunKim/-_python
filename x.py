import sys
print(sys.platform)
print(2**100)
S = 'Spam'
L=[123,'spam',1.23]
print(len(L))
print(L[0])
print(L[:-1])
print(L[2])
M = ['bb','aa','cc']
M2=[[1,2,3],[4,5,6],[7,8,9]]

D = {'food':'Spam','quantity':4,'color':'pink'}
print(D['food'])
print(D)

L2 = [1,2,3,4]
print(L2+[5,6])
print(L.append(8))
L3 = {1:'a',2:'b',3:'c'}
print([x for x in L3])


if 1:
    print('true')

x=10
while x:
    x-=1
    if x%2!=0: continue
    print(x, end=' ')

