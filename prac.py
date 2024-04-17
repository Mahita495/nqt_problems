def can_segment(s,d):
    for i in range(1,len(s)+1):
        first = s[0:i]
        if first in d:
            second = s[i:]
            if not second or second in d or can_segment(second, d):
                return True
    return False

s="datacampfluf"
d=["data","can","camp","fluf"]
print(can_segment(s,d))