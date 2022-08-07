class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left != right:
            index = (left + right) // 2
            if numbers[index] > numbers[right]:
                left = index + 1
            elif numbers[index] < numbers[right]:
                right = index
            else:
                # 说明有相等的数字，缩小判断范围
                right -= 1
        return numbers[left]
