d1,d2 = input().split()

a = int(d1)
b = int(d2)


gcd = a%b
 

while True:
	if a%b == 0:break
	a = b
	b = gcd
	print("%s %% %s = %s" % (a,b,a%b))	
	gcd = a%b
	
lcm=int(d1)*(int(d2)//b)

print("gcd:%s\nlcm:%s" %(b,lcm))
