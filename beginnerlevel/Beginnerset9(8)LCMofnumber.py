N=int(input())
M=int(input())
if(N>M):
  g=N
else:
  g=M
while(True):
  if((g%N==0)and(g%M==0)):
    lcm=g
    break
  g+=1
print(g)
