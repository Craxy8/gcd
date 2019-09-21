a,b = input().split()

a=int(a)
b=int(b)

gcd=a%b

while gcd:
	a=b
	b=gcd
	print("%s %% %s = %s" % (a,b,a%b))
	if a%b == 0:break
	gcd = a%b

print(gcd)
