def spy_game(nums):
    for i in range(0, len(nums)):
        if nums[i] == 0:
            for w in range(i + 1, len(nums)):
                if nums[w] == 0:
                    for k in range(w + 1, len(nums)):
                        if nums[k] == 7:
                            return True
        
    return False

n = list(map(int, input().split(',')))
print(spy_game(n))