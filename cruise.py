hours=int(input())
entry=list(map(int,input().split()))
exit=list(map(int,input().split()))

guest=entry[0]-exit[0]

for i in range(1,hours):
    guest = guest + (entry[i]-exit[i])

print(guest)