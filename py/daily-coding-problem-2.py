# 13/08
# https://www.dailycodingproblem.com/
# Given an array of integers, return a new array such that each element at index i of 
# the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def solve_with_division(arr):
    total = 1
    for num in arr:
        total *= num


    result = []
    for num in arr:
        result.append(int(total / num))

    return result


def solve_without_division(arr):

    prefx = [1] * len(arr)
    sufx = [1] * len(arr)

    for i in range(1, len(arr)):
        prefx[i] = prefx[i - 1] * arr[i - 1]

    
    for i in range(len(arr)-2, -1, -1):
        sufx[i] = sufx[i+1] * arr[i+1]


    result = [prefx[i] * sufx[i] for i in range(0,len(arr))]
    return result

def test_case_1():
    arr = [1,2,3,4,5]
    expected = [120,60,40,30,24]
    assert solve_with_division(arr) == expected


def test_case_2():
    arr = [3,2,1]
    expected = [2,3,6]
    assert solve_with_division(arr) == expected


def test_case_3():
    arr = [1,2,3,4,5]
    expected = [120,60,40,30,24]
    assert solve_without_division(arr) == expected


def test_case_4():
    arr = [3,2,1]
    expected = [2,3,6]
    assert solve_without_division(arr) == expected
