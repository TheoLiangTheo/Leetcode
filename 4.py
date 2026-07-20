class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        actual = sorted(nums1 + nums2)
        if len(actual)%2 == 0:
            return (actual[len(actual)//2]+actual[len(actual)//2-1])/2
        return actual[len(actual)//2]
