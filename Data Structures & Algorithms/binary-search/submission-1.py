class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def b_search(lo, hi):
            if hi == lo:
                if nums[hi] == target:
                    return hi
                else:
                    return -1
            else:
                mid = (hi + lo)//2
                if nums[mid] > target:
                    return b_search(lo, mid)
                if nums[mid] < target:
                    return b_search(mid+1, hi)
                else:
                    return mid
        return b_search(0, len(nums) - 1)