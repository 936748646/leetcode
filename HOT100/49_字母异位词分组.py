class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = dict()
        for s in strs:
            key = ''.join(sorted(s))  # 字符串排序后作为hash表的key；对应的值为原始字符串
            if key not in h.keys():
                h[key] = []
            h[key].append(s)
        return list(h.values())
