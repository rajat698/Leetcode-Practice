nums = [0,0,1,1,1,1,2,3,3]
l, r = 1, 1
count = 0

while r < len(nums):

    if nums[r] == nums[r - 1]:
        count += 1

    else:
        count = 0

    if count < 2:
        nums[l] = nums[r]
        l += 1
    
    r += 1

# return l

print(nums)