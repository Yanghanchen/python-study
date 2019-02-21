def maxium_sub_arr(arr,low,high):
    if low == high - 1:
        return (low,high,arr[low])
    mid = int((low + high)/2)
    left = maxium_sub_arr(arr,low,mid)
    right = maxium_sub_arr(arr,mid,high)
    cross = maxium_cross_sub_arr(arr,low,mid,high)
    if left[2] >= right[2] and left[2] >= cross[2]:
        return left
    elif right[2] >= left[2] and right[2] >= cross[2]:
        return right
    else:
        return cross

def maxium_cross_sub_arr(arr,low,mid,high):
    left_sum = float("-inf")
    sum = 0
    i = mid
    while i >= low:
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
        i = i - 1

    right_sum = float("-inf")
    sum = 0
    j = mid + 1
    while j <= high:
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
        j = j + 1
    return max_left,max_right,left_sum+right_sum

sample = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(maxium_sub_arr(sample,0,len(sample)-1))