class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        nums = sorted(list(nums))
        if len(nums) == 1:
            return 1
        
        max_consec, curr_consec = 1, 1
        
        curr_val = [nums[0]]
        for n in nums[1:]:
            if n in range(curr_val[0],curr_val[-1]):
                curr_consec+=1
                continue
            if n == curr_val[0]-1: 
                curr_consec+=1
                curr_val.insert(0, n)
                continue
            if n == curr_val[-1]+1:
                curr_consec+=1
                curr_val.append(n)
                continue
            max_consec = max(max_consec, curr_consec)
            curr_consec = 1
            curr_val = [n]
        max_consec = max(max_consec, curr_consec)
        return max_consec