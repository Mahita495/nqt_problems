#in given matrix, find the row that has max no of 1's

mat =[]
rows=int(input())
cols=int(input())

for i in range(rows):
    m=[]
    for j in range(cols):
        m.append(int(input()))
    mat.append(m)

ones=[]
for i in mat:
    ones.append(i.count(1))

ma = max(ones)
print(ones.index(ma) + 1)