class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = [0, 0]

        for i in range(0, len(nums)-1, 1):
            for j in range(i+1, len(nums), 1):
                if(nums[i] + nums[j] == target):
                    output[0] = i
                    output[1] = j
        
        return output