from random_gen import rand
import math
n = int(input("number of random no.: "))
R = rand(n)
R.sort()
# R = []
# for i in range(n):R.append(random.random())
I_N = [float(x/n) for x in range(1,n+1)]

D1 = [I_N[i]-R[i]  if I_N[i]-R[i] > 0 else 0 for i in range(n)]

D2 = [R[i]-float((i-1)/n) if R[i]-float((i-1)/n)> 0 else 0 for i in range(n)]
# print(D1)
# print(D2)
D = max(max(D1),max(D2))
D_alpha = float(1.36/math.sqrt(n))
print(R,I_N,D1,D2,sep="\n")
print("D : ",D)
print("D_alpha: ",D_alpha)
if D <= D_alpha:print("Hypothesis is not rejected")
else: print("Hypothesis is rejected")
