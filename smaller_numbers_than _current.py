#!/usr/bin/env python
# coding: utf-8

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
#   
#   
# Return the answer in an array.

# Example 1:  
#     
# 
# Input: nums = [8,1,2,2,3]  
# Output: [4,0,1,1,3]  
# Explanation:   
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).  
# For nums[1]=1 does not exist any smaller number than it.  
# For nums[2]=2 there exist one smaller number than it (1).   
# For nums[3]=2 there exist one smaller number than it (1).   
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# Example 2:  
# 
# Input: nums = [6,5,4,8]  
# Output: [2,1,0,3]

# Example 3:  
# 
# Input: nums = [7,7,7,7]  
# Output: [0,0,0,0]

# In[1]:


class Solution:
    def smaller_numbers_than_current(self, nums: list) -> list:
        sorted_nums = sorted(nums, reverse=True)
        smaller_count = {}
        
        for i in range(len(sorted_nums) -1):
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i+1]
            if next_num < curr_num:
                remaining_values = len(sorted_nums) - (i + 1)
                smaller_count[curr_num] = remaining_values
                
        smaller_count[sorted_nums[-1]] = 0
        output = []
        
        for num in nums:
            output.append(smaller_count[num])
        
        return output


# In[4]:


sol = Solution()
print(sol.smaller_numbers_than_current([8,1,2,2,3]))

