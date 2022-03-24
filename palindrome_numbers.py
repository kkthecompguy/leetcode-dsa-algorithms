#!/usr/bin/env python
# coding: utf-8

# Given an integer x, return true if x is palindrome integer.
# 
# An integer is a palindrome when it reads the same backward as forward.
# 
# * For example, 121 is a palindrome while 123 is not.
# 
# 
# Example 1:  
# 
# 
# * Input: x = 121
# * Output: true
# * Explanation: 121 reads as 121 from left to right and from right to left.
# 
# 
# Example 2:  
# 
# * Input: x = -121
# * Output: false
# * Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.  
#   
#   
# 
# Example 3:
# 
# * Input: x = 10
# * Output: false
# * planation: Reads 01 from right to left. Therefore it is not a palindrome.
#  
# 
# Constraints:
# 
# -231 <= x <= 231 - 1

# In[3]:


class Solution:
    def is_palindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str[::-1] == x_str


# In[4]:


sol = Solution()
print(sol.is_palindrome(121))


# In[9]:


class Solution:
    def is_palindrome(self, x: int) -> bool: 
        rev_n = self.reverse_digits(x) 
        print('rev_n',rev_n) 
        return rev_n == x
    
    def reverse_digits(self, num):
        rev_num = 0
        while (num > 0):
            rev_num = rev_num * 10 + num % 10
            num = num // 10 
        return rev_num


# In[12]:


sol = Solution()
print(sol.is_palindrome(331))


# In[ ]:




