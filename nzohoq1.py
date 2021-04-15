def pypart2(s):
	n=len(s)
	mid=int(len(s)/2)
	k = n - 1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
		
			if(j+mid)<n:
			    print(s[j+mid], end="")
			else:
			    print(s[j-mid-1],end="")
	
		print("\r")
n = input()
pypart2(n)
