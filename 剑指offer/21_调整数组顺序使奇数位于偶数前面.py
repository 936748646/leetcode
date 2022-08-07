class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for n in nums:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)
        return odd + even
