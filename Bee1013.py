import math
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maiorAB = (a+b+abs(a-b))/2
maiorBC = (b+c+abs(b-c))/2
if(maiorAB > maiorBC):
    print(f"{maiorAB:.0f} eh o maior")
else:
    print(f"{maiorBC:.0f} eh o maior")