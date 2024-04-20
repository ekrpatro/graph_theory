def maxSubArray(nums):
    if not nums:
        return 0, -1, -1  # If array is empty, return 0 sum and invalid indices    
    max_sum = nums[0]  # Initialize max_sum to the first element
    current_sum = nums[0]  # Initialize current_sum to the first element
    start_index = end_index = 0  # Initialize start and end indices    
    # Initialize variables to keep track of the best start and end indices
    best_start = best_end = 0    
    # Iterate over the array starting from the second element
    for i in range(1, len(nums)):
        # Update current_sum to be the maximum of the current element and the current_sum plus the current element
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            start_index = i  # Update start index
        else:
            current_sum += nums[i]
        
        # Update max_sum if current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i  # Update end index
        
        # Update best_start and best_end if max_sum is updated
        if max_sum > current_sum:
            best_start = start_index
            best_end = end_index
    
    return max_sum, best_start, best_end,nums[best_start:best_end+1]

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("array : ",nums)
max_sum, start_index, end_index,sub_arr = maxSubArray(nums)
print("Maximum sum of subarray:", max_sum)
print("Start index:", start_index)
print("End index:", end_index)
print(sub_arr)


