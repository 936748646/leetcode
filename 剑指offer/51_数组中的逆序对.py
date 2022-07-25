class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 将数组全部归并排序，排序过程中寻找逆序对
        # 思想：将nums从中点m分开，左子数组tmp[i]>右子数组tmp[j]时，构成逆序对m-i+1个
        # （左右子数组在一轮轮归并的过程中已经有序，因此左子数组tmp[i]>右子数组tmp[j]时，
        # tmp[i]后面到tmp[m]的元素都比tmp[i]大，因而也都大于tmp[j]）
        def merge_sort(l, r):
            if l >= r: return 0
            # 先两两分组
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 再两组归并，小的放到nums里
            i, j = l, m + 1
            tmp[l: r + 1] = nums[l: r + 1]
            for k in range(l, r + 1):
                if i == m + 1:  # 左子数组已经归并完，接下来添加j和j之后的元素即可
                    nums[k] = tmp[j]
                    j += 1
                # 右子数组归并完或i、j元素有序，则添加i元素
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:  # 遇到逆序对，添加j元素
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1
            return res
        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)
