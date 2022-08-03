class Solution {
    // 两二进制数a，b相加规律：a+b=无进位和n+进位c。n=a异或b；进c=a并b左移一位
    // 由于不能用+，因此不停转换n和c（a+b=n+c=n'+c'=n''+c''...）直到c为0
    // 因为实在是搞不懂python的负数处理方法，以后涉及的都用java了
    public int add(int a, int b) {
        while(b != 0) {
            int c = (a & b) << 1;  // 进位
            // 又把无进位和进位赋值给a、b，如此循环操作
            a ^= b;  // 无进位
            b = c;
        }
        return a;
    }
}
