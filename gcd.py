a,b = input().split()

a=int(a)
b=int(b)

gcd=a%b

while a%b != 0:
	a=b
	b=gcd
	print("%s %% %s = %s" % (a,b,a%b))
	gcd = a%b

print(gcd)
