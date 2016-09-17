inversions=[]
sum = 0
def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    m = len(arr) / 2
    l = mergesort(arr[:m])
    r = mergesort(arr[m:])

    if not len(l) or not len(r):
        return l or r
        
    result = []
    i = j = 0
    global sum
    while (len(result) < len(r)+len(l)):        
        if l[i] < r[j]:
            result.append(l[i])
            # print l, r
            i += 1
        else:
            result.append(r[j])
            inversions.append(len(l)-i)
            sum += len(l)-i
            # print l,r 
            # print inversions 
            j += 1            
        if i == len(l) or j == len(r):            
            result.extend(l[i:] or r[j:])
            break

    return result

 

x=[9,10,4,2,1,3]
print (mergesort(x))
# sum=0
# for i in inversions:
# 	sum=i+sum
# print sum
print sum
