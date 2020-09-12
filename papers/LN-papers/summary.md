<!--
 * @Author: ZhXZhao
 * @Date: 2020-09-01 11:29:26
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2020-09-11 21:23:43
 * @Description: file content
-->
# 闪电网络中存在的问题

闪电网络中仍存在几方面的问题：安全和并发性问题、隐私问题、路由问题、效率问题以及网络的鲁棒性问题。

## 安全和并发性问题

**虫洞攻击**：在一条支付路径中，有两个合作的恶意用户，协作将诚实的中间用户排除在成功的支付外，进而窃取本该属于诚实用户的交易费。（详见论文《Anonymous Multi-Hop Locks for Blockchain Scalability and Interoperability》）

**拥塞攻击**：有两种方式：1）攻击者发送一笔支付者和收款者都是自己的交易，该交易的路由路径要尽可能的长。2）攻击者发送一笔交易，同样支付者和收款者都是自己，但交易的路由总是反复经过一个hub节点。
拥塞攻击的目的可以有两种：一种是耗尽HTLCs，一种是耗尽通道余额。（详见论文《Congestion Attacks in Payment Channel Networks》）

**并发性带来的死锁**：当有两个通道的HTLCs的数量都耗尽时，而有两笔支付都需要用到这两个通道来进行路由的时候，此时两笔支付都无法进行下去，产生了死锁。（详见论文《Concurrency and Privacy with Payment-Channel Networks》）

***瞭望塔***

## 隐私问题

**交易金额隐私**（value privacy）：当一个支付涉及的用户都是诚实的时候，支付路径外的恶意用户是无法知晓任何有关支付金额的信息的。（详见论文《Concurrency and Privacy with Payment-Channel Networks》）

**关系隐私**（sender/receiver anonymity）：当有两个交易通过同一条支付路径进行路由时，当支付路径中至少有一个诚实的中间节点时，恶意的中间节点无法以大于1/2的概率确定一笔交易的发送者和接收者$(s_i,r_i)$，即无法确定交易是哪个发送者发给哪个接收者。（详见论文《Concurrency and Privacy with Payment-Channel Networks》）

**通道余额隐私**：论文《On the Difficulty of Hiding the Balance of Lightning Network Channels》中提出了一种揭露闪电网络中通道余额的攻击方法。

## 路由问题

路由效率低，路由带来的通信开销大、路由路径不是最优的。（详见论文《Settling Payments Fast and Private: Efficient Decentralized Routing for Path-Based Transactions》）

## 鲁棒性问题


