'''
Assumptions
1. We will always have a positive shift
2. An empty list will return an empty list
3. Shifts will always be to the right
4. Shifts will always be less than length, otherwise return None
4. Items of the list don't have to be numbers
5. The list will be mutable

Pseudocode
example input [1, 2, 3], 2 
example output [2, 3, 1]

declare variable that stores empty list
declare variable to store last index len(list) - 1

use for...range to loop through list
add shift by to index and move element to index
'''
test_list = [2,5,6,8,9,7]

def rotate_list(list, shift_by):
    r_list = list.copy()
    end_of_list = len(list) - 1
    for idx in range(len(list)): 
        new_idx = (idx - shift_by) % end_of_list
        current_el = list[idx]
        # print(new_idx)
        # print(list[idx])
        print(f"{list=}")
        r_list[new_idx] = current_el
    print(f"{r_list=}")

rotate_list(test_list, 2)
# assert rotate_list([1,2,3], 2) == [2, 3, 1]