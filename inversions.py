def merge_count(left, right):
    results, curr_inv = [], 0
    while left and right:
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
            curr_inv += len(left)

    results.extend(left)
    results.extend(right)
    return (results, curr_inv)

print(merge_count([1,3,5], [2,4,6]))

def count_inversions(lst):
    if len(lst) == 1:
        return (lst, 0)
    else:
        mid = len(lst) // 2
        (left, left_inv) = count_inversions(lst[:mid])
        (right, right_inv) = count_inversions(lst[mid:])
        (sorted_lst, split_inv) = merge_count(left, right)
        return (sorted_lst, left_inv + right_inv + split_inv)

# def merge_sort(lst):
#     if len(lst) < 2:
#         return lst
#     mid = len(lst) // 2
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#     return merge(left, right)

a_file = open('IntegerArray.txt')
file_contents = a_file.read()
input_arr = list(map(int, file_contents.splitlines()))
# print(input_arr[:5])
print(count_inversions(input_arr))
