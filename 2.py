from sys import argv

d1=max(int(argv[1]),int(argv[2]))
d2=min(int(argv[2]),int(argv[2]))
a=d1
b=d2
gcd=a%b

if gcd==0 and a!=b:
	c=b
elif a==b:
	c=a

else:
	while 1:
		gcd=a%b
		if gcd==0:break
		print("%s %% %s = %s" % (a,b,gcd))	
		c=gcd
		tmp=b
		b=gcd
		a=tmp

print(abs(c))
