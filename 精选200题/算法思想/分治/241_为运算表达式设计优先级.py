class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 分治：每个运算符op所连接算式的值集合=运算符左右两个子算式的值集合依次进行op，如此递归
        # X op Y的值集合=X的值集合 op Y的值集合（X、Y分别为表达式）
        if expression.isdigit(): return [int(expression)]
        res = []
        for i in range(0, len(expression)):
            if expression[i] in ['+', '-', '*']:  # 每遇到运算符，就开启递归计算左右子表达式X、Y的值集合
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:  # 根据op依次合并X、Y的值集合
                    for r in right:
                        if expression[i] == '+': res.append(l + r)
                        elif expression[i] == '-': res.append(l - r)
                        else: res.append(l * r)
        return res
