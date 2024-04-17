nums=[1,1,2,3,4,4,5,5,5,6,7,8,8]
def sortind(nums):
    insert=1
    for i in range(1,len(nums)):
        if nums[i-1]!=nums[i]:
            nums[insert]=nums[i]
            insert+=1
    return insert

print(sortind(nums))    