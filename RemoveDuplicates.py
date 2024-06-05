def removeDuplicates(nums) -> int:
    size = len(nums)
    if size < 3:
        return size
    prevEle = nums[1]
    prevPrevEle = nums[0]
    iteration = 2
    while True:
        if iteration > size - 1:
            break
        num = nums[iteration]
        if num == prevEle and prevEle == prevPrevEle:
            nums.pop(iteration)
            size -= 1
            continue
        prevPrevEle = prevEle
        prevEle = num
        iteration += 1
    return size