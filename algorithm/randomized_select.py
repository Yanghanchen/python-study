import random

def randomized_select(arr,left,right,x):
    if left == right:
        return arr[left]
    index = randomPartition(arr,left,right)
    i = index - left + 1
    if i == x:
        return arr[index]
    elif i < x:
        return randomized_select(arr,index+1,right,x-i)
    else:
        return randomized_select(arr,left,index-1,x)

def partition(l,left,right):
    pivot = left
    index = left + 1
    for i in range(index,right + 1):
        if l[i] < l[pivot]:
            swap(l,i,index)
            index = index + 1
    swap(l,index-1,pivot)
    return index - 1

def randomPartition(l,left,right):
    pivot = random.randint(left,right)
    swap(l,left,pivot)
    return partition(l,left,right)

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

sample = [5,2,4,6,1,3]
print(randomized_select(sample,0,len(sample)-1,3))