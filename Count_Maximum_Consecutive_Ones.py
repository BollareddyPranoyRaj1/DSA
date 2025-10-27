print("Enter the array:",end=" ")
arr=list(map(int,input().split()))
c=0
for i in range(len(arr)-1):
    if arr[i]==1 and arr[i+1]==1:
        c+=1
    else:
        c=0
print(c+1)
