class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, len(s_list) - 1
        while i < j:
            if s_list[i] in vowel and s_list[j] in vowel: 
                s_list[i], s_list[j] = s_list[j], s_list[i]  # 列表元素可以这样交换，拆开写就不行
                i += 1
                j -= 1
            elif s_list[i] not in vowel: i += 1
            else: j -= 1
        return ''.join(s_list)
