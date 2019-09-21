a,b = int(input().split())

while gcd:
	gcd = a%b
	a=b
	b=gcd

print(gcd)
