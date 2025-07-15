def max_end3(nums):
  # We are given an array, and we have to determine
  # whether the last or first element is bigger 
  # Lastly, we have to make every element in the 
  # list that exact number
  newnums = []
  for num in nums:
    if nums[0] < nums[-1]:
      newnums.append(nums[-1])
    elif nums[0] > nums[-1]:
      newnums.append(nums[0])
    elif nums[0] == nums[-1]:
      newnums.append(nums[0])
    # else:
    #   return nums
  return newnums   