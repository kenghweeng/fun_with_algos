a_file = open('QuickSort.txt')
file_contents = a_file.read()
input_arr = list(map(int, file_contents.splitlines()))
# print(input_arr[:5])
print(input_arr[:5])

def quickSort(arr, left_idx, right_idx):
    if right_idx - left_idx <= 0:
        return 0 # singleton case
    else:
        def partition(arr, left_idx, right_idx):
            '''
            3 ways to choose the pivot:
            1. First element
            2. Final element, preprocess by swapping final with first element
            3. Median of 3 choices: first, middle, last elements
            '''
            # 1st way:
            # pivot = arr[left_idx] # first element

            # 2nd way: swap final element with first element
            # arr[right_idx], arr[left_idx] = arr[left_idx], arr[right_idx]
            # pivot = arr[left_idx] # used to be the final element

            # 3rd way: 'Median of 3 pivot rule'
            mid = left_idx + (right_idx - left_idx) // 2
            first, middle, last = arr[left_idx], arr[mid], arr[right_idx]
            sorted_lst = sorted([first, middle, last])
            if sorted_lst[1] == first:
                pass
            elif sorted_lst[1] == middle:
                arr[mid], arr[left_idx] = arr[left_idx], arr[mid]
            else:
                arr[right_idx], arr[left_idx] = arr[left_idx], arr[right_idx]

            pivot = arr[left_idx]
            i = left_idx + 1
            for j in range(left_idx + 1, right_idx + 1):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i] # redundant swap initial
                    i += 1
            arr[left_idx], arr[i-1] = arr[i-1], arr[left_idx]
            return (right_idx - left_idx, i-1) # comparisons, idx
        comparisons, pivot_idx = partition(arr, left_idx, right_idx)
        return quickSort(arr, left_idx, pivot_idx - 1) + comparisons + \
        quickSort(arr, pivot_idx + 1, right_idx)

print(quickSort(input_arr, 0, len(input_arr) - 1))
