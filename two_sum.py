def two_sum(nums : list, target : int):
    result = []
    for i in range(0, len(nums)):
        for k in range(i+1, len(nums)):
            if nums[i] + nums[k] == target:
                if len(result) < 2:
                    if nums[i] == nums[k]:
                        result.append(nums.index(nums[i]))
                        result.append(nums.index(nums[k], nums.index(nums[i]) + 1))
                    else:
                        result.append(nums.index(nums[i]))
                        result.append(nums.index(nums[k]))
    return result