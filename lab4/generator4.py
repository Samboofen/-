def s():
    n=int(input())
    i=int(input())
    while True:
        if i<=n:
            break
        yield i*i
        i+=1
for i in s():
    print(i)