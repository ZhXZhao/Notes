<!--
 * @Author: ZhXZhao
 * @Date: 2022-01-04 20:55:44
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2022-01-04 21:47:28
 * @Description: file content
-->
# StringBuffer && StringBuilder

相同点：

- 都是可变的字符序列，底层使用char[]存储
- 空参char[]默认长度为16，带参数长度为 参数值+16
- 扩容后长度为 原长度*2 + 2




不同点：

- StringBuffer是线程安全的，StringBuilder是线程不安全的
- StringBuffer效率低，StringBuilder效率高

## StringBuffer

