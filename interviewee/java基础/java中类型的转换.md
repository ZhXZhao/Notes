<!--
 * @Author: ZhXZhao
 * @Date: 2021-05-28 14:36:13
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2021-10-22 11:15:55
 * @Description:
-->

# java类型转换

java的8种基本数据类型：byte、short、int、long、float、double、char、boolean

在java中，boolean不可以与其他七种基本类型做运算。
数据表示范围的大小：byte < short < int < long < float < double
数据表示范围小的可以自动转成数据表示范围大的类型，反之不行。（隐式转换）
其中char、byte、short之间做运算返回的结果默认为int类型。
java中的数字常量默认都是int类型。

String类型可以与8种基本类型做连接运算（+），返回类型为String

