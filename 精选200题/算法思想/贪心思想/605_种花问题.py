class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 贪心：从头遍历只要满足[0,0,0]，就种
        cnt, l = 0, len(flowerbed)
        for i in range(0, l):
            if cnt >= n: break
            if flowerbed[i] == 1: continue
            pre = flowerbed[i - 1] if i > 0 else 0
            next = flowerbed[i + 1] if i < l - 1 else 0
            if pre == next == 0:
                cnt += 1
                flowerbed[i] = 1
        return cnt >= n
