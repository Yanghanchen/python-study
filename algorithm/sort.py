import math

def bucket_sort(l,bucketSize=5):
    minValue = min(l)
    bucket = []
    for i in range(bucketSize):
        bucket.append([])
    for i in l:
        index = math.floor((i-minValue)/bucketSize)
        if index > bucketSize - 1:
            index = bucketSize - 1
        bucket[index].append(i)
    l.clear()
    for j in range(bucketSize):
        if len(bucket[j]) > 0:
            insertion_sort(bucket[j])
            l += bucket[j]
    return l

def count_sort(l):
    maxium = max(l)
    bucket = []
    sortedIndex = 0
    for i in range(maxium+1):
        bucket.append(0)
    for i in l:
        bucket[i] += 1
    for i in range(maxium+1):
        while bucket[i] > 0:
            l[sortedIndex] = i
            sortedIndex += 1
            bucket[i] -= 1
    return l

def heapify(arr,index,length):
    left = 2 * index + 1
    right = 2 * index + 2
    max = index
    if left < length and arr[left] > arr[max]:
        max = left
    if right < length and arr[right] > arr[max]:
        max = right
    if max != index:
        swap(arr,index,max)
        heapify(arr,max,length)

def buildHeap(l):
    length = len(l)
    for i in range(math.floor(length/2),-1,-1):
        heapify(l,i,length - 1)

def heap_sort(l):
    length = len(l)
    buildHeap(l)
    print(l)
    i = length - 1
    while i > 0:
        swap(l,0,i)
        length = length - 1
        heapify(l,0,length)
        i = i - 1
        print(l)
    return l

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

def shell_sort(l):
    length = len(l)
    gap = 1
    while gap < length/3:
        gap = 3 * gap + 1
    while gap > 0 :
        for i in range(0,length - gap):
            minIndex = i
            for j in range(i + gap,length,gap):
                if l[j] < l[minIndex]:
                    minIndex = j
            swap(l,i,minIndex)
        gap = math.floor(gap / 3)
        print(l)
    return l

def selection_sort(l):
    for i in range(0,len(l)-1):
        minIndex = i
        for j in range(i+1,len(l)):
            if l[j] < l[minIndex]:
                minIndex = j
        swap(l,i,minIndex)
        print(l)
    return l

def bubble_sort(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                swap(l,i,j)
                print(l)
    return l

def insertion_sort(l):
    for i in range(1,len(l)):
        temp = l[i]
        j = i - 1
        while (j>=0 and l[j]>temp):
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = temp
        print(l)

def merge_sort(l):
    length = len(l)
    if(length < 2):
        return l
    middle =  math.floor(length/2)
    left = l[0:middle]
    right = l[middle:]
    return merge(merge_sort(left),merge_sort(right))

def merge(left,right):
    result = []
    if left != None and right != None:
        while(len(left)>0 and len(right)>0):
            if(left[0]>right[0]):
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                left.pop(0)
    if left != None:
        while len(left)>0:
            result.append(left.pop())
    if right != None:
        while len(right)>0:
            result.append(right.pop())
    return result

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

sample = [5,2,4,6,1,3]
#insertion_sort(sample)
#print(merge_sort(sample))
#bubble_sort(sample)
#selection_sort(sample)
#shell_sort(sample)
#quick_sort(sample,0,len(sample)-1)
#heap_sort(sample)
#print(count_sort(sample))
#print(bucket_sort(sample,2))