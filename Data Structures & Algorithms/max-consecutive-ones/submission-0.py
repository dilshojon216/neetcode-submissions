class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_rec=rec=0
        for num in nums:
            if num==0:
                best_rec=max(best_rec,rec)
                rec=0
            else:
                rec+=1
        return max(best_rec,rec)