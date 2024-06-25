from typing import List
nums = int(input[List2])
target = int(input)

def solve(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

# Tests 
#nums = [2, 7, 11, 15]
#target = 9
#output = solve(nums, target)
#print(output)  # Вывод: [0, 1]
#109 <= target <= 104  s
#2 <= nums.length <= 109  
#109 <= nums[i] <= 109  
