# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:49:26 2023

@author: ecalandrini
"""

import random
import time

def is_palindrome(num):
    # Helper function to check if a number is a palindrome
    return str(num) == str(num)[::-1]

def generate_palindromes3(N):
    
    nums = list(map(int, str(N)))
    # find the unique numbers appearing in nums
    unique = set(nums)
    unique_list = list(unique)
    unique_list.sort()
    
    # count their occurrence
    counts = []
    for i in unique_list:
        counts.append(nums.count(i))
    
    # if they appear only once, the result is the maximum
    if len(counts) == sum(counts):
        return max(unique_list)
    
    # build the edges of the palindrome 
    # with the numbers that appear an even number of times
    # build the centre of the palindrome
    # with the numbers that appear an odd number of times, but take the maximum
    even = []
    odd = []
    for i in range(len(unique_list)):
        if counts[i] % 2 == 0:
            for j in range(counts[i]//2):
                even.insert(0, unique_list[i])
                even.append(unique_list[i])
        else: 
            odd.append(int(counts[i]*str(unique_list[i])))
    
    # print(even, odd)
    # put the parts together
    test = even.copy()
    if len(odd) > 0:
        test.insert(len(even)//2, max(odd))
    pp = int(''.join(map(str, test)))
    
    if is_palindrome(pp) == False:
        # print("Error:", pp, nums)
        test = list(str(pp))
        while test[-1] == "0":
            test.pop()
        pp = int(''.join(map(str, test)))
    return pp

# Example usage:

for j in [10**k for k in range(8)]:
    list_int = []
    for i in range(j):
        list_int.append(random.randint(0, 100000))

    start = time.time()
    for i in list_int:
        result = generate_palindromes3(i)
    end = time.time()
    print(j, end - start)
# print(N, result)
