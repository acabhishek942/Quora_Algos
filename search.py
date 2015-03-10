def binary_search(array, number):
    """Takes sorted array and a number as input"""
    start=0
    end=len(array)-1
    while start<=end:
        mid=int((start+end)/2)
        if array[mid]==number:
            return mid
        elif array[mid]<number:
            start=mid+1
        else:
            end=mid-1
    return -1
