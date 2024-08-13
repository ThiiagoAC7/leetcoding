# 12/08
# https://www.dailycodingproblem.com/
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def solve(arr, k):
    
    map = {}

    for i in range(0, len(arr)):
        
        rest = k - arr[i]

        if rest == 0 or map.get(arr[i]):
            return True
        
        map[rest] = arr[i]

    print(map)
    return False


def test_answ_1():
    arr = [10,15,3,7]
    k = 17
    assert solve(arr,k)

def test_answ_2():
    arr = [10,15,3,7]
    k = 18
    assert solve(arr,k)

def test_answ_3():
    arr = [10,15,3,7]
    k = 10
    assert solve(arr,k)

def test_answ_4():
    arr = [10,15,3,7]
    k = 25
    assert solve(arr,k)

def test_answ_5():
    arr = [10,15,3,7]
    k = 13 
    assert solve(arr,k)

def test_answ_6():
    arr = [10,15,3,7]
    k = 22 
    assert solve(arr,k)

def test_error():
    arr = [10,15,3,7]
    k = 5 
    assert solve(arr,k) == False
