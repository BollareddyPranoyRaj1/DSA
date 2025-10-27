def subarrayCheck(arr, n, k) -> int:
    l = 0
    sum_ = 0
    maxi = 0

    for r in range(n):
        sum_ += arr[r]
        while sum_ > k and l <= r:
            sum_ -= arr[l]
            l += 1
        if sum_ == k:
            maxi = max(maxi, r - l + 1)
    return maxi


n = int(input())
k = int(input())
arr = list(map(int, input().split()))
print(subarrayCheck(arr, n, k))
