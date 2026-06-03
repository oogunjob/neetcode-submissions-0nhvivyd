class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            # my goal is compute the difference of the target and num
            # if the difference is in the hashmap it means that I can return that and the current number
            difference = target - num

            if difference in hashmap:
                return [hashmap[difference], i]

            else:
                hashmap[num] = i

        return []
        