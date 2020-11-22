<!--
 * @Author: ZhXZhao
 * @Date: 2020-07-30 10:23:46
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2020-11-18 19:40:33
 * @Description:
-->

# Settling Payments Fast and Private: Efficient Decentralized Routing for Path-Based Transactions

---

- [Settling Payments Fast and Private: Efficient Decentralized Routing for Path-Based Transactions](#settling-payments-fast-and-private-efficient-decentralized-routing-for-path-based-transactions)
  - [正文](#正文)
  - [先进的路由算法](#先进的路由算法)
    - [Landmark Routing](#landmark-routing)
      - [SilentWhispers存在的问题](#silentwhispers存在的问题)
    - [Embedding-based Routing](#embedding-based-routing)
      - [VOUTE](#voute)
  - [本文的方案](#本文的方案)

## 正文

本文提出了一种新型的用于基于路径的交易（Path-Based Transactions(PBT)）网络的路由算法。相较之前提出过的路由算法，本文提出的算法具有更高的隐私性，有效性，高效性和可扩展性。

## 先进的路由算法

### Landmark Routing

先在网络中标识一些landmark节点，即有着高连接度的节点。假设共有L个landmark节点，然后一笔交易的金额被划分成L份，每一份交易通过一个包含landmark节点的路径来传输。
在最初阶段，以landmark节点为根节点，采用两次广度优先遍历算法来遍历图，生成两个生成树，一次考虑forward边，一次考虑reverse边。然后发送者根据生成树来寻找交易路径到接收者。
landmark routing还分为两种，一种为landmark-centered，即从发送者到接受者的路径总是要经过landmark节点，另一种为tree-only，即从BFS树中寻找最短的路由路径，而不必包含landmark节点。

在SilentWhispers中采用的就是landmark-centered的方法。

#### SilentWhispers存在的问题

- 不能立即对网络中的变化做出改变，因为生成树是周期重建的。
- 因为SilentWhispers中的路由必须经过landmark节点，所以有可能存在比经过landmark节点更短的路由路径，但是不会选择更短的。
- 探测操作需要节点和所有的landmark节点交流分配的金额比，所以通信开销与landmark节点的数量成平方关系。
- SilentWhispers没有提供一个合适的解决并发问题的方案。

### Embedding-based Routing

Embeddings给每个节点都分配一个坐标，然后计算节点之间的距离时根据坐标来进行计算。在找路由路径时，以最短路径为目标，而不是依据生成树来找最短路径。

#### VOUTE

VOUTE就是利用Embedding来进行路由的。VOUTE更新生成树不是周期性地进行更新，而是按需进行更新，也就是可以及时更新生成树。

存在的问题：
- 与现有的PBT网络不兼容。
- VOUTE只考虑了无向图和无权边的情况，而实际上PBT网络是有向带权图。
- VOUTE只考虑了节点动态的加入和离开，但是在PBT网络中，最主要的动态变化是边的权值变化。
- VOUTE没有处理并发问题。

## 本文的方案

分为3步：1）setRoutes：构建embeddings；2）setCred：增加一个新的非零权重的连接或移除一个零权重的连接；3）routePay：接收者生成匿名接收地址发送给发送者，发送者划分交易金额为L份（landmark数量），然后用VOUTE的路由算法找到一条发送者到接收者的路径。


