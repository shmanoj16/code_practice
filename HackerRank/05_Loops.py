# #!/usr/bin/env python

# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

# Example

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# 0
# 1
# 4
# Input Format

# The first and only line contains the integer, .

# Constraints


# Output Format

# Print  lines, one corresponding to each .

# Sample Input 0

# 5
# Sample Output 0

# 0
# 1
# 4
# 9
# 16

# https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input("Enter the number\t"))
    
    if n >0:
        for i in range(0,n):
            print(i**2)
