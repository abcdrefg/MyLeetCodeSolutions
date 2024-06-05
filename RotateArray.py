def rotate(nums, k: int) -> None:
    nums_size = len(nums)
    elements_to_rotate = []
    if nums_size < k:
        k = k % nums_size
    for i in range(nums_size - k, nums_size):
        elements_to_rotate.append(nums[i])
    for i in reversed(range(nums_size - k)):
        nums[i + k] = nums[i]
    for i in reversed(range(k)):
        nums[i] = elements_to_rotate[i]

rotate([1,2], 3)