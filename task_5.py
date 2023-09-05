'''
Write an algorithm that takes an array
and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''


# 1st version
def move_zeros(lst):
    numbers_list = []    # stores numbers greater than zero
    zeros_list = []      # stores zeros

    for num in lst:
        if num == 0:
            zeros_list.append(num)
        else:
            numbers_list.append(num)

    sorted_list = numbers_list + zeros_list
    return sorted_list


lst = ([1, 0, 1, 2, 0, 1, 3])    # should return [1, 1, 2, 1, 3, 0, 0]
print(move_zeros(lst))


# 2nd version
