t=int(input())
a=str(4)
for i in range(t):
    x=str(input())
    cnt=0
    for j in x:
        if j==a:
            cnt=cnt+1
    print(cnt)