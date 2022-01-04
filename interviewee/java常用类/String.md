<!--
 * @Author: ZhXZhao
 * @Date: 2022-01-04 13:51:00
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2022-01-04 15:44:49
 * @Description: file content
-->
# String

1. final的，不可被继承
2. 实现了Serializable，支持序列化
3. 实现了Comparable，可比较大小
4. 底层用final char[] value存储字符串，不可变
5. 通过字面量（区别于new）的方式给一个字符串赋值，此时的字符串值声明在字符串常量池中。字符串常量池中不会存储相同内容的字符串。
6. 通过new的方式会在对空间开辟一块空间存储对象结构，value指向字符串常量池中的char[]数组。
7. 常量与常量的拼接结果在常量池中，常量池中不会存储相同内容的常量。
8. 变量与常量（变量）的拼接结果在堆中。
9. 调用String.intern()，返回值在常量池中。
