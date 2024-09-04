


def merge(arr, s, e):
    mid = (s+e)//2
    left_arr = arr[s:mid+1]
    right_arr = arr[mid+1:]

    left_index, right_index, main_index = 0 , 0, s

    while(left_index<len(left_arr) and right_index<len(right_arr)):
        if(left_arr[left_index]<right_arr[right_index]):
            arr[main_index] = left_arr[left_index]
            left_index+=1
        else:
            arr[main_index] = right_arr[right_index]
            right_index+=1
        main_index+=1

    while(left_index<len(left_arr)):
        arr[main_index] = left_arr[left_index]
        left_index+=1
        main_index+=1

    while(right_index<len(right_arr)):
        arr[main_index] = right_arr[right_index]
        right_index+=1
        main_index+=1

def merge_sort(arr, s, e):
    if s>=e:
        return
    mid = (s+e)//2

    merge_sort(arr, s, mid)
    merge_sort(arr, mid+1,e)

    merge(arr, s, e)


if __name__ == "__main__":
    arr = [2, 1, 6, 9, 4, 5]
    size = len(arr)
    s = 0
    e = size - 1

    print("Before merge sort:")
    print(" ".join(map(str, arr)))

    # Perform merge sort on the entire array
    merge_sort(arr, s, e)

    print("After merge sort:")
    print(" ".join(map(str, arr)))