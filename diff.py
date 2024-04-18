s1="eueiieo"
s2="iieoedue"
def sort_str(s1,s2):
    s1=sorted(s1)
    s2=sorted(s2)
    i,j=0,0
    while i<len(s1) and j<len(s2):
        if s1[i]==s2[j]:
            i+=1
            j+=1
        else:
            return s2[j]
    
print(sort_str(s1,s2))
        