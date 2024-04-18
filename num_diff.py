def num_diff(n):
    nums=[]
    while n>0:
        digit=n%10
        nums.append(digit)
        n=n//10
    n1=sorted(nums)
    n2=sorted(nums, reverse=True)
    n1=[str(i) for i in n1]
    n2=[str(i) for i in n2]
    s1=''.join(n1)
    s2=''.join(n2)
    return abs(int(s1)-int(s2))
print(num_diff(123))