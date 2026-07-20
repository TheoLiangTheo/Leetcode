class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind1 = 0
        ind2 = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    ind1 = i
                    ind2 = j
                    break
            if [ind1,ind2] != [0,0]:
                break
        return [ind1,ind2]