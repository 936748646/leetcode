class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs回溯
        if not digits: return []
        res = []
        phoneMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(combination, nextdigits):  # 算回溯，但没有回退
            if not nextdigits: 
                res.append(combination)
            else:
                for letter in phoneMap[nextdigits[0]]:
                    backtrack(combination + letter, nextdigits[1:])
        backtrack("", digits)
        return res
