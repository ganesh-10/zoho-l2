def pypart2(s):
	n=len(s)
	mid=int(len(s)/2)
	k = 2*n - 2
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 2
		for j in range(0, i+1):
		
			if(j+mid)<n:
			    print(s[j+mid], end="")
			else:
			    print(s[j-mid-1],end="")
	
		print("\r")
n = input()
pypart2(n)