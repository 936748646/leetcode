class Solution:
    def isNumber(self, s: str) -> bool:
        # states存储0-8状态，states[i]存储i状态能到达的状态
        # states[i]中的键值对(key,val)表示输入key能到达的状态val
        states = [  
            {' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. 开始的空格
            {'d': 2, '.': 4},                  # 1. （幂符号前的）正负号
            {'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 小数点前的数字
            {'d': 3, 'e': 5, ' ': 8},          # 3. 小数点、小数点后的数字(可以无，所以可以转到5、8)
            {'d': 3},                          # 4. 当小数点前为空格时，小数点后的数字（必须有，所以只能转到3）
            {'s': 6, 'd': 7},                  # 5. 幂符号
            {'d': 7},                          # 6. （幂符号后的）正负号
            {'d': 7, ' ': 8},                  # 7. 幂符号后的数字
            {' ': 8}                           # 8. 结尾的空格
        ]                                      # 合法结束2、3、7、8
        p = 0  # 初始状态0
        for c in s:
            if '0' <= c <= '9':
                t = 'd'
            elif c in '+-':
                t = 's'
            elif c in 'eE':
                t = 'e'
            elif c in ' .':
                t = c
            else:
                t = '?'
            if t not in states[p]:
                return False
            p = states[p][t]
        if p in [2, 3, 7, 8]:
            return True    
        return False
