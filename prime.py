def seiveoferatosthenes(n):
    p=2
    arr=[True]*(n+1)
    while p*p <= n:
        if arr[p]==True:
            for i in range(p*p,n+1,p):
                arr[i]=False
        p=p+1
    for i in range(2,n+1):
        if arr[i] :
            print(i)

seiveoferatosthenes(200)
