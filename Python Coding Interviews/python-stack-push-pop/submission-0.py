from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        return arr
    reversed_arr = []
    for i in range(len(arr)):
        top_element = arr.pop()
        reversed_arr.append(top_element)
    return reversed_arr



# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
