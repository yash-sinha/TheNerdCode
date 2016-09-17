
def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def partition(array, start,end):
    x = array[end]
    i = start -1
    for j in xrange(start, end):
        if (array[j] <= x):
            i = i+1
            swap (array,i,j)
    swap(array,i+1,end)
    return i+1

def quicksort(array,p,r):
    if p<r:
        print("Before Partition:",array)
        q = partition(array,p,r)
        print("q:",q,"p:",p, "r:",r)
        print("After Partition:",array)
        
        print("Before first quicksort:",array)
        quicksort(array,p,q-1)
        print("After first quicksort:",array)
        print("Before second quicksort:", array) 
        quicksort(array,q+1,r)
        print("After second quicksort:", array)    

def main():
    unsortedArray = [2,8,7,1,3,5,6,4,9,0]
    quicksort(unsortedArray,0,len(unsortedArray)-1)
    print unsortedArray


if __name__ == '__main__':
    main()
