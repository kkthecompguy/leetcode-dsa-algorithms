#!/usr/bin/env python
# coding: utf-8

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from  
# cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.  
# 
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one  
# destination city.

# Example 1:  
# 
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]  
#     
# Output: "Sao Paulo"  
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip  
# consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

# Example 2:  
# 
# Input: paths = [["B","C"],["D","B"],["C","A"]]  
# Output: "A"  
# Explanation: All possible trips are:  
# "D" -> "B" -> "C" -> "A".  
# "B" -> "C" -> "A".  
# "C" -> "A".  
# "A".   
# Clearly the destination city is "A".

# In[1]:


class Solution:
    def destCity(self, paths: list) -> str:
        cityMap = {}
        for path in paths:
            cityMap[path[0]] = path[1]
        
        dest = paths[0][1]
        while True:
            if dest in cityMap:
                dest = cityMap[dest]
            else:
                return dest 


# In[3]:


sol = Solution()
print(sol.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))


# In[4]:


class Solution:
    def dest_city(self, paths:list) -> str:
        outgoing_count = {}
        for path in paths:
            city_a, city_b = path
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)
            
        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city


# In[6]:


sol = Solution()
print(sol.dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))


# In[7]:


class Solution:
    def dest_city(self, paths: list) -> str:
        exit_cities = set()
        for city in paths:
            exit_cities.add(city[0])
        for cities in paths:
            if cities[1] not in exit_cities:
                return cities[1]


# In[8]:


sol = Solution()
print(sol.dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))


# In[10]:


class Solution:
    def dest_city(self, paths: list):
        A, B = map(set, zip(*paths))
        return (B - A).pop()


# In[11]:


sol = Solution()
print(sol.dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

