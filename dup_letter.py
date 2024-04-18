s="Define the winning combinations"
def dup_letter(s):
    s=s.split(" ")
    for i in s:
        if str(set(i))!=i:
            return False

        