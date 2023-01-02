class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs：每个单词为节点，两个单词相差一个字符则存在边
        wordSet = set(wordList)  # 直接用list，不转为set会超时
        l = len(beginWord)
        if endWord not in wordSet: return 0

        queue = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)
        while queue:
            word, depth = queue.pop(0)
            if word == endWord: return depth
            for i in range(l):
                for n in range(97, 123):
                    w = word[:i] + chr(n) + word[i+1:]  # 一个个生成可能的下一节点
                    if w in wordSet and w not in visited:
                        queue.append((w, depth+1))
                        visited.add(w)
        return 0
      
      # 感觉这样写不太好，因为没用list而用set节省时间才能勉强通过
      # 还有一种优化版本是双向bfs，空了再看
