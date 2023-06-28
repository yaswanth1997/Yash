ASSIGNMENTS:

1.	Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab" Explanation: "aba" is also valid.
Example 2:
Input: s = "cbbd"
Output: "bb"

Code:
def longest_palindrome(s):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # For odd-length palindromes
        pal_odd = expand_around_center(s, i, i)
        if len(pal_odd) > len(longest):
            longest = pal_odd

        # For even-length palindromes
        pal_even = expand_around_center(s, i, i + 1)
        if len(pal_even) > len(longest):
            longest = pal_even

    return longest

2.	Fibonacci Sequence Take length as input and give fib seq till that length
Example 1:
Input: 5
Output: 0,1,1,2,3
Example 2:
Input: 10
Output: 0,1,1,2,3,5,8,13,21,34

Code:
def fibonacci_sequence(length):
    sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    # Generate the Fibonacci sequence
    while len(sequence) < length:
        next_num = sequence[-1] + sequence[-2]  # Calculate the next Fibonacci number
        sequence.append(next_num)  # Add the next number to the sequence

    return sequence

# Example usage:
length = int(input("Enter the length of the Fibonacci sequence: "))
fib_seq = fibonacci_sequence(length)
print(fib_seq)

3.	Remove Duplicates from given Array 
Example 1:
Input: 1,2,3,2,5,4,1,4,5
Output: 1,2,3,5,4
Example 2:
Input: 1,5,8,6,5,1,2,4,2,4,8
Output: 1,5,8,6,2,4
AWS EC2 to practice Linux commands

Code:
def remove_duplicates(arr):
    unique_arr = list(set(arr))
    return unique_arr

# Example usage:
arr = [1, 2, 3, 2, 5, 4, 1, 4, 5]
unique_arr = remove_duplicates(arr)
print(unique_arr)

4.	Concatenate any 2 strings to give  smallest string from given array of srings
Example:
Input: S=[“aab”,”bcddbc”,”aa”,”aazef”]
Output: “aabaa”

Code:
def concatenate_smallest_string(S):
    smallest = min(S, key=len)  # Find the string with the minimum length
    S.remove(smallest)  # Remove the smallest string from the list

    # Concatenate the remaining strings to the smallest string
    for string in S:
        for i in range(len(string), 0, -1):
            if smallest.endswith(string[:i]):
                smallest += string[i:]
                break

    return smallest

# Example usage:
S = ["aab", "bcddbc", "aa", "aazef"]
result = concatenate_smallest_string(S)
print(result)