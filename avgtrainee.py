

scores = []
for rows in range(3):
    col=[]
    for cols in range(3):
        col.append(int(input()))
    scores.append(col)

avg=[0,0,0]

for i in range(3):
    for j in range(3):
        avg[i]+=(scores[j][i] / 3)
    m=max(avg)

for i in range(3):
    if avg[i]==m:
        print("Trainee num: " , (i+1))


