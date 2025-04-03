class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        value = 0
        diff = 0
        triplet = 0

        for i in nums:
            triplet = max(triplet, diff*i)
            value = max(value, i)
            diff = max (diff, value-i)

        return triplet