class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        value = 0
        diff = 0
        triplet = 0

        for num in nums:
            triplet = max(triplet, diff*num)
            value = max(value, num)
            diff = max(diff, value - num)
        
        return triplet