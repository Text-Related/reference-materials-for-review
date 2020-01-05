# 求100以内的素数
import math    
   
def isPrime(n):
	if  n <= 1:
		return False
	for i in range(2,int(math.sqrt(n) + 1)):
		if n % i == 0:
			return False
		return True

for i in range(2,100):
	if isPrime(i):
		print("{0} is a prime number.".format(i))