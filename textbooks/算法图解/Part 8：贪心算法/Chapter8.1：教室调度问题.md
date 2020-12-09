<!--
 * @Author: ZhXZhao
 * @Date: 2020-12-02 16:30:56
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2020-12-02 16:33:06
 * @Description: file content
-->
# 教室调度问题

教室调度问题适用于贪心算法。
做法：
1. 选出结束最早的课，添加到待上的课中。
2. 选出在上一节课结束之后，结束最早的课，添加到待上的课中。
3. 重复第2步。
