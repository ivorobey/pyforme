nums=[7,4,2,1,9,4,4,2,0]

for i in range(len(nums)):
    lower=i

    for j in range(i+1,len(nums)):
        if nums[j]<nums[lower]:
            lower=j
    
    nums[i], nums[lower]=nums[lower],nums[i]


print(nums)