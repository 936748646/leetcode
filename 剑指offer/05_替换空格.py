class Solution:
    def replaceSpace(self, s: str) -> str:
        s_list = []
        for i in s:
            if i == ' ':
                s_list.append('%20')
            else:
                s_list.append(i)
        return ''.join(s_list)
