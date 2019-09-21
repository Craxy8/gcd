a,b = input().split()

a = int(a)
b = int(b)


gcd = a%b
 

while True:
	if a%b == 0:break
	a = b
	b = gcd	
	gcd = a%b
	

print("gcd:%s" %(b))
