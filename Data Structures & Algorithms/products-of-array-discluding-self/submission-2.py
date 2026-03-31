class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # need to keep an array that will store the multipler
        # [1, 2, 4, 6]
        
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        l_mult = 1
        r_mult = 1

        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)

        for i in range(len(nums)):
            j = -i - 1

            # update array
            l_arr[i] = l_mult
            r_arr[j] = r_mult

            # update loop control variable
            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l*r for l,r in zip(l_arr, r_arr)]
        