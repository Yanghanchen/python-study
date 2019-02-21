# 算法导论 思考题 8-4
# 题目：有n个红色水壶和蓝色水壶，外表各不相同，同种颜色的水壶盛的水数量各不相同，并且总有一对红色和蓝色水壶盛的水一样多，需要找出每一对水量相同的水壶。同色水壶之间不能相互比较水量。
# 思路：类似快排，挑选一只红水壶，找到水量相同的蓝水壶，作为主元，然后分区，用红水壶进行蓝水壶的快排，用蓝水壶进行红水壶快排即可

def make_a_pair(red_kettle,blue_kettle,left,right):
    if left>=right:
        return
    index = partition(blue_kettle,red_kettle[left],left,right)
    partition(red_kettle,blue_kettle[index],left,right)
    make_a_pair(red_kettle,blue_kettle,left,index-1)
    make_a_pair(red_kettle,blue_kettle,index+1,right)

def partition(kettle,pivot,left,right):
    index = left - 1
    for i in range(left,right+1):
        if kettle[i] < pivot:
            index += 1
            swap(kettle,i,index)
    for i in range(index+1,right+1):
        if kettle[i] == pivot:
            index += 1
            swap(kettle,i,index)
            break
    return index

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

red_kettle = [1,5,12,34,2,17,79]
blue_kettle = [17,34,1,2,79,5,12]
make_a_pair(red_kettle,blue_kettle,0,len(red_kettle)-1)
print(red_kettle,blue_kettle)