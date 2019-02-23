import math

def quick_sort(l,left,right):
    if left < right:
        partitionIndex = partition(l,left,right)
        quick_sort(l,left,partitionIndex-1)
        quick_sort(l,partitionIndex+1,right)
    return l

def partition(l,left,right):
    pivot = left
    index = left + 1
    for i in range(index,right + 1):
        if l[i] < l[pivot]:
            swap(l,i,index)
            index = index + 1
    swap(l,index-1,pivot)
    print(l)
    return index - 1

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def min_oil_pipeline(l):
    length = len(l)
    quick_sort(l,0,length-1)
    count = 0
    if length%2 == 1:
        mid = math.floor(length/2)
        for i in l:
            count += abs(i-l[mid])
    else:
        for i in range(int(length/2)):
            count += (l[length-1-i] - l[i])
    return count


sample = [2,2,3,-2,3]
sample2 = [10,7,9,4,16,-5,3,1,-2,8]
# expect output:6
print(min_oil_pipeline(sample))
print(min_oil_pipeline(sample2))