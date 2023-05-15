def max_bitwise_or(nums, k):
  """
  Returns the maximum possible value of nums[0] | nums[1] | ... | nums[n - 1]
  that can be obtained after applying the operation on nums at most k times.

  Args:
    nums: A list of integers.
    k: The number of times the operation can be applied.

  Returns:
    The maximum possible value of nums[0] | nums[1] | ... | nums[n - 1].
  """

  # Find the maximum power of 2 that is less than or equal to k.
  max_power_of_2 = 1
  while max_power_of_2 <= k:
    max_power_of_2 *= 2

  # Initialize the maximum possible value to 0.
  max_value = 0

  # Iterate over the elements of nums.
  for num in nums:
    # Find the highest power of 2 that divides num.
    power_of_2 = 1
    while num % power_of_2 == 0:
      power_of_2 *= 2

    # If the power of 2 is less than or equal to k, then we can multiply num by 2.
    if power_of_2 <= k:
      num *= 2

    # Update the maximum possible value.
    max_value |= num

  return max_value

nums = [8, 1, 2]
k = 2

max_value = max_bitwise_or(nums, k)

print(max_value)
