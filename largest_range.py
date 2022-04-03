#!/usr/bin/env python
# coding: utf-8

# Find the largest range of values in array or list

# In[1]:


def largest_range(array):
    numbers = {x:0 for x in array}
    left = right = 0
    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1
            
            while left_count in numbers: # O(1)
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1
            
            while right_count in numbers:
                numbers[right_count] = 1
                right_count += 1
            right_count -= 1
            
            if (right-left) <= (right_count - left_count):
                right = right_count
                left = left_count
    return [left,right]


# In[5]:


x = [2,3,1,5,6, 12, 11, 10, 9]
print(largest_range(x))


# In[ ]:




