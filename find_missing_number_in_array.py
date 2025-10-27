n=int(input())
arr=list(map(int,input().split()))
sum1=int(n*(n+1)/2)
print(abs(sum(arr)-sum1))
