from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum=0
    for element in nums:
        sum+=element
    return sum

def get_min(nums: List[int]) -> int:
    min_elemet=nums[0]
    for element in nums:
        if min_elemet> element:
            min_elemet=element
    return min_elemet

def get_max(nums: List[int]) -> int:
    max_element=nums[0]
    for element in nums:
        if max_element<element:
            max_element=element
    return max_element

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
