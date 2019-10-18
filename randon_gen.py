def rand(n):
  a,m,x,c = 5,128,10,127
  den=list()
  for i in range(n): 
    den.append(x/m)
    x=(x*a+c)%m
  return den
