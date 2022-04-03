#!/usr/bin/env python
# coding: utf-8

# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or  
# "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as  
# the string "al". The interpreted strings are then concatenated in the original order.  
# 
# 
# Given the string command, return the Goal Parser's interpretation of command.

# Input: command = "G()(al)"  
# Output: "Goal"  
# Explanation: The Goal Parser interprets the command as follows:  
# G -> G  
# () -> o  
# (al) -> al  
# The final concatenated result is "Goal".

# In[1]:


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)","al")


# In[3]:


sol = Solution()
print(sol.interpret("G()(al)"))


# In[4]:


sol = Solution()
print(sol.interpret("G()()()()(al)"))


# In[5]:


class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i , l = 0 , len(command)
        while i<l:
            if command[i] == "G":
                ans+="G"
                i+=1
            elif command[i] == "(" and command[i+1] == ")":
                ans+="o"
                i+=2
            else:
                ans+="al"
                i+=4
        return ans


# In[6]:


sol = Solution()
print(sol.interpret("G()(al)"))


# In[ ]:




