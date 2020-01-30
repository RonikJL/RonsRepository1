def minSubArrayLen(self, s, nums):

    if len(nums) == 0: return 0
    start = end = 0
    sumn = nums[0]
    el = float('inf')
    while start <= end and end < len(nums):
        if sumn >= s:
            el = min(el, end - start + 1)
            sumn -= nums[start]
            start += 1
        else:
            end += 1
            if end < len(nums):
                sumn += nums[end]
    if el == float('inf'):
        el = 0
    return el
