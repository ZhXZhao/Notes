<!--
 * @Author: ZhXZhao
 * @Date: 2020-02-14 21:24:55
 * @LastEditors  : ZhXZhao
 * @LastEditTime : 2020-02-14 21:45:39
 * @Description: 
 -->
# 多方参与的安全博彩系统

---

- [多方参与的安全博彩系统](#%e5%a4%9a%e6%96%b9%e5%8f%82%e4%b8%8e%e7%9a%84%e5%ae%89%e5%85%a8%e5%8d%9a%e5%bd%a9%e7%b3%bb%e7%bb%9f)
  - [在线掷硬币系统](#%e5%9c%a8%e7%ba%bf%e6%8e%b7%e7%a1%ac%e5%b8%81%e7%b3%bb%e7%bb%9f)
  - [公平性](#%e5%85%ac%e5%b9%b3%e6%80%a7)

各自都有敏感数据的互不信任的一群参与者，共同来执行一个程序，不仅仅是为了控制数据，还可以控制与之关联的资金。

## 在线掷硬币系统

假设有三个参与者：A，B，C。三人想以相同的概率选择一个号码0，1，2。我们可以尝试这种方法，A，B，C三人各选取一个大的随机数x，y，z，然后计算（x+y+z）%3。但我们没有办法保证三个人同时发出数据，若一个人等待其他两个人发出数据后再选择数据发出，这样最后发出数据的人可以任意的操控最后的结果。

为解决这个问题，我们规定每一个人选一个大的随机数，然后发布大的随机数的哈希值，然后公布所选的随机数，接着每个人可以查证哈希值是否匹配，最后计算三个数的结果。

## 公平性

若有人在发现自己可能会输掉这一局的时候，选择假装掉线而不公布自己的随机数，这样其他两人也没有办法进行追查。

我们做出这样的设计：A设置一定量的保证金，这个保证金的输出对象为参与游戏的其他人B和C，若在规定时间内A公布了自己的随机数，则A可以赎回保证金，否则保证金将会转给B和C，A会损失这笔保证金。
