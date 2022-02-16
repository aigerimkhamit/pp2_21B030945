def has_33(nums):
    for i in range(len(nums)):
        if nums[i: i + 2] == [3,3]:
            return True
    return False
n = list(map(int, input().split(",")))
print(has_33(n))
