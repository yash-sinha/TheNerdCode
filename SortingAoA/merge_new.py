
n1=n2=inversions = 0
L = []
R = []

def merge(A,p,q,r):
	global n1,n2,inversions
	n1 = q - p
	print(n1)
	n2 = r - q -1
	print(n2) 
	for i in range(0,n1-1):
		L[i] = A[p + i - 1]
	for j in range(0,n2-1):
		R[j] = A[q+j]
	L[n1] = 10000
	R[n2] = 10000
	i=j=1
	for k in range(p,r):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
			inversions += len(L) - i

def mergesort(A,p,r):
	print("In mergesort, value of p:",p,"value of r:",r)
	if p < r:
		q = (p+r)/2
		print("q= ",q )
		mergesort(A,p,q)
		mergesort(A,q+1,r)
		print("Before merge function:", p, q, r)
		merge(A,p,q,r)

A=[9,1,3,2,0,5]
print(len(A) - 1)
mergesort(A,0,len(A)-1)