s= "Robert000Smith000123"

def encode(s):
    s=s.split("000")
    return s
print(encode(s))

def encode(s):
    l=''
    num=''
    last_name=''
    for i in s:
        if i.isalpha():
            l+=i
        elif i.isdigit() and i!='0':
            num+=i
    for i in range(1,len(l)):
        if l[i].isupper():
            last_name=l[i:]
            first_name=l[0:i]
    return (first_name, last_name, num)

print(encode(s))