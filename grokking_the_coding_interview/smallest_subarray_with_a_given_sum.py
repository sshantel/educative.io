"""
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
"""
#Time Complexity #
#The time complexity of the above algorithm will be O(N)O(N). The outer for loop runs for all elements, and the inner while loop processes each element only once; therefore, the time complexity of the algorithm will be O(N+N)O(N+N), which is asymptotically equivalent to O(N)O(N).

#Space Complexity #
#The algorithm runs in constant space O(1)O(1).
import math


def smallest_subarray_with_given_sum(s, arr):
  window_sum = 0
  min_length = math.inf
  left = 0

  for right in range(len(arr)):
    window_sum += arr[right]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while window_sum >= s:
      min_length = min(min_length, right - left + 1)
      window_sum -= arr[left]
      left += 1
  if min_length == math.inf:
    return 0
  return min_length


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
