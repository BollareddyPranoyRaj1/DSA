# ============================================================================
# SOLUTION 1: Longest Subarray with Sum K (Positives Only)
# ============================================================================
# This solution finds the length of the longest subarray with sum equal to K
# using the optimal sliding window (two pointer) approach for positive numbers.
# Time Complexity: O(n), Space Complexity: O(1)

def longest_subarray_with_sum_k(arr, k):
    """
    Find the length of the longest subarray with sum equal to K.
    Works only for arrays with positive numbers.
    
    Args:
        arr: List of positive integers
        k: Target sum
    
    Returns:
        Length of the longest subarray with sum K
    """
    left = 0
    right = 0
    current_sum = 0
    max_length = 0
    n = len(arr)
    
    while right < n:
        # Add the current element to the sum
        current_sum += arr[right]
        
        # Shrink the window from left if sum exceeds K
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1
        
        # Update max_length if we found sum equal to K
        if current_sum == k:
            max_length = max(max_length, right - left + 1)
        
        right += 1
    
    return max_length


# ============================================================================
# SOLUTION 2: Count of Subarrays with Sum K
# ============================================================================
# This solution counts the total number of subarrays with sum equal to K
# using the prefix sum and hashmap approach.
# Time Complexity: O(n), Space Complexity: O(n)

def count_subarrays_with_sum_k(arr, k):
    """
    Count the number of subarrays with sum equal to K.
    Works for arrays with positive, negative, and zero values.
    
    Args:
        arr: List of integers
        k: Target sum
    
    Returns:
        Count of subarrays with sum K
    """
    prefix_sum_map = {0: 1}  # Initialize with 0 sum occurring once
    current_sum = 0
    count = 0
    
    for num in arr:
        # Add current element to the running sum
        current_sum += num
        
        # Check if (current_sum - k) exists in the map
        # If yes, it means there are subarrays ending at current index with sum K
        if current_sum - k in prefix_sum_map:
            count += prefix_sum_map[current_sum - k]
        
        # Add current_sum to the map
        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1
    
    return count


# ============================================================================
# MAIN PROGRAM - Testing both solutions
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("LONGEST SUBARRAY WITH SUM K (Positives Only)")
    print("=" * 60)
    
    # Input for longest subarray problem
    n1 = int(input("Enter the number of elements in the array: "))
    arr1 = []
    print(f"Enter {n1} positive elements:")
    for i in range(n1):
        arr1.append(int(input(f"Element {i+1}: ")))
    
    k1 = int(input("Enter the target sum K: "))
    
    # Find and display result
    result1 = longest_subarray_with_sum_k(arr1, k1)
    print(f"\nLength of the longest subarray with sum {k1}: {result1}")
    
    print("\n" + "=" * 60)
    print("COUNT OF SUBARRAYS WITH SUM K")
    print("=" * 60)
    
    # Input for count subarrays problem
    n2 = int(input("\nEnter the number of elements in the array: "))
    arr2 = []
    print(f"Enter {n2} elements (can be positive, negative, or zero):")
    for i in range(n2):
        arr2.append(int(input(f"Element {i+1}: ")))
    
    k2 = int(input("Enter the target sum K: "))
    
    # Find and display result
    result2 = count_subarrays_with_sum_k(arr2, k2)
    print(f"\nNumber of subarrays with sum {k2}: {result2}")
    print("\n" + "=" * 60)
    print("Program completed successfully!")
    print("=" * 60)
