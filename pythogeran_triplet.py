def pythogeran_triplet(nums):
    nums=[i*i for i in nums]
    nums.sort()
    for i in range(len(nums)+1):
        if nums[i]+nums[i+1] in nums:
            return True
            break
    else:
        return False
nums=[3, 2, 4, 6, 5] 
print(pythogeran_triplet(nums))


#other method
def pythogeran_triplet(nums):
    nums=[i*i for i in nums]
    nums.sort()

    for i in range(len(nums)-1,1,-1):
        s=set()
        for j in range(i-1,1,-1):
            if nums[i]-nums[j] in s:
                return True
        else:
            return False