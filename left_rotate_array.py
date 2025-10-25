# cook your dish here
arr=list(map(int,input().split()))
num=int(input("Enter number below array length : "))
rotatedArr=arr[num:]+arr[:num]
print(rotatedArr)
