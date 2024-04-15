n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))

if nums[0]==nums[n-1]:
    print(0)
else:
    x=nums[0]
    count=0
    for i in nums:
        if i!=x:
            count+=1

    print(count)