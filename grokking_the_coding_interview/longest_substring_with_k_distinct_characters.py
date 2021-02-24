"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""
def longest_substring_with_k_distinct(str1, k):
  left = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [left, right]
  for right in range(len(str1)):
    right_char = str1[right]
    if right_char not in char_frequency: 
        char_frequency[right_char] = 0
    char_frequency[right_char] += 1
    print(char_frequency)

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k: 
      left_char = str1[left]
      print(f'left char is {left_char}')
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      left += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, right-left + 1)
    print(f'max length is {max_length}')
  return max_length


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
