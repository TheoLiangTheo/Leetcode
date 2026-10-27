class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if abs(current - target) < abs(closest - target):
                    closest = current
                if current == target:
                    return current
                elif current < target:
                    left += 1
                else:
                    right -= 1
        return closest   