# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string .

# Constraints


# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

# https://www.hackerrank.com/challenges/swap-case/problem

# **Approach 1 - Two lines of code**

def swap_case(s):
    final_char="".join([char.lower() if char.isupper() else char.upper() for char in s])
    return final_char
		
if __name__ == '__main__':
    s = input()



# **Approach 2 - Easily Understandable**

def swap_case(s):
    final_string=""
    for ele in s:
        if ele.islower():
            final_string=final_string+ele.upper()
        else:
            final_string=final_string+ele.lower()
    return final_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result) 

    result = swap_case(s)
    print(result)
