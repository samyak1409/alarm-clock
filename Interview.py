"""
Given an array of integers, please write a function that determines whether it is possible to rearrange it in following
fashion: a1 < a2 > a3 < a4 > a5 <

2 1 5 3 11 7
4 2 1 6 8 2
1 2 2 2 3
"""


def check(a):
    # DURING INTERVIEW - TRY 1: Failed ❌
    # return len(a) == len(set(a))

    # DURING INTERVIEW - TRY 2: Failed ❌
    """a.sort()
    for i in range(1, len(a)-1, 2):
        a[i], a[i+1] = a[i+1], a[i]
    # print(a)  # debug
    for i in range(0, len(a)-2, 2):
        if not (a[i] < a[i+1]) or not (a[i+1] > a[i+2]):
            return False
    if len(a) % 2:
        return True
    return True if a[-1] > a[-2] else False"""

    # AFTER INTERVIEW - TRY 1: Passed ✅ :) HURTS A LOT WHEN YOU FAILED TO DO AN EASY QUESTION BECAUSE OF NERVOUSNESS
    a.sort()
    i, j = 0, len(a)-1
    k = 0
    while i != j:
        # print(i, j)  # debug
        if k % 2 == 0:
            if not (a[i] < a[j]):
                return False
            i += 1
        else:
            if not (a[i] < a[j]):
                return False
            j -= 1
        k += 1
    return True


arr = list(map(int, input().split()))
print(check(arr))
