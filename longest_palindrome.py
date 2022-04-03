#!/usr/bin/env python
# coding: utf-8

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome  
# that can be built with those letters.  
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:  
# 
# Input: s = "abccccdd"  
# Output: 7  
# Explanation:  
# One longest palindrome that can be built is "dccaccd", whose length is 7.  
# Example 2:  
# 
# Input: s = "a"  
# Output: 1  
# Example 3:  
# 
# Input: s = "bb"  
# Output: 2  
#  
# 
# Constraints:  
# 
# 1 <= s.length <= 2000  
# s consists of lowercase and/or uppercase English letters only.

# In[4]:


import collections
class Solution:
    def longest_palindrome(self, s: str) -> int:
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


# In[5]:


sol = Solution()
print(sol.longest_palindrome("abccccdd"))


# In[6]:


class Solution:
    def longest_palindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            
        final_count = 0
        odd_is_present = False
        for char in char_count:
            if char_count[char] % 2 == 0:
                final_count += char_count[char]
            else:
                final_count += (char_count[char]-1)
                odd_is_present = True
            
        if odd_is_present:
            final_count += 1
            
        return final_count


# In[7]:


sol = Solution()
print(sol.longest_palindrome("abccccdd"))

