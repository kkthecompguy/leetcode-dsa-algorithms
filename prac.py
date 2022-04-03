def smaller_numbers_than_current(nums: list) -> list:
    sorted_nums = sorted(nums, reverse=True)
    print('sorted_nums', sorted_nums)
    smaller_count = {}
    
    for i in range(len(sorted_nums) -1):
        curr_num = sorted_nums[i]
        next_num = sorted_nums[i+1]
        print('curr_num', curr_num)
        print('next_num', next_num)
        if next_num < curr_num:
            remaining_values = len(sorted_nums) - (i + 1)
            print('remaining_values', remaining_values)
            smaller_count[curr_num] = remaining_values
            print('smaller_count[curr_num]', smaller_count)
            
    smaller_count[sorted_nums[-1]] = 0
    output = []
    print('smaller_count', smaller_count)
    for num in nums:
      print(num)
      output.append(smaller_count[num])
    
    return output


print(smaller_numbers_than_current([8,1,2,2,3]))

[-1,0,3,5,9,12]
9
[-1,0,3,5,9,12]
2