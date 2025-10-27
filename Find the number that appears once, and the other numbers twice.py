print("Enter the array:",end=" ")
arr=list(map(int,input().split()))
hash1={}
for i in arr:
    if i not in hash1:
        hash1[i]=1
    else:
        hash1[i]+=1
for i,j in hash1.items():
    if j==1:
        print(i)
        break
