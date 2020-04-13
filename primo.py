r =True
n = int(input("ingrese el numero: "))
d=0
while d<n and r:
  if n%2==0:
    r = False
  d=d+1
if(r):
  print("es primo")
else:
  print("no es primo")
