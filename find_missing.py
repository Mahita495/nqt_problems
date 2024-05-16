
nums=[5,3,4,7,2,1,8]

def miss(nums):
    n=len(nums)+1
    act_sum = int((n*(n+1))/2)
    s=sum(nums)
    return act_sum-s
print(miss(nums))

