def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
           count = count + 1
    return count
Print(list_count_4([1,4,6,7,4]))
