class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in numMap:
                return [numMap[remain], i]
            numMap[nums[i]] = i

        return []
