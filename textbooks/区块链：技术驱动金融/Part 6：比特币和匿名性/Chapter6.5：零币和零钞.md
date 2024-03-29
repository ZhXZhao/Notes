<!--
 * @Author: ZhXZhao
 * @Date: 2020-02-12 17:02:07
 * @LastEditors  : ZhXZhao
 * @LastEditTime : 2020-02-12 20:43:03
 * @Description: 
 -->
# 零币和零钞

---

- [零币和零钞](#%e9%9b%b6%e5%b8%81%e5%92%8c%e9%9b%b6%e9%92%9e)
  - [零币](#%e9%9b%b6%e5%b8%81)
    - [零知识验证](#%e9%9b%b6%e7%9f%a5%e8%af%86%e9%aa%8c%e8%af%81)
    - [铸造零币](#%e9%93%b8%e9%80%a0%e9%9b%b6%e5%b8%81)
  - [零钞](#%e9%9b%b6%e9%92%9e)

零币和零钞在协议层融合了匿名化处理，并且它们可以达到的匿名性非常强大有效。
**兼容性**。零币需要通过软分叉的比特币协议方式去实施。零钞只能以一种另类币（altcoin）的方式存在。
**加密学保证**。零币和零钞在协议层已经融入了混币功能，其匿名属性来自加密学的保证。

## 零币

为解释零币，需先介绍一下**基础币**（Basecoin）。基础币是一种类似于比特币的另类币，而零币是这种数字货币的一种延伸，其所提供的匿名性的核心特点在于，你可以将基础币与零币进行来回的转换。在系统中，基础币是你需要进行交易的币，零币只是提供了一种交易基础币的机制，这种机制可以确保新币和旧币之间毫无关联。
**零币就是一个证明**（类似于赌场的一个筹码），证明你拥有一个零币，稍后可以用这个零币来赎回这个证明并取得一个新的基础币。

### 零知识验证

**零知识验证**可以证明一个声明是正确的，而不需要展示可推导该声明正确性的任何其他信息。**零知识证明的本质**就是在不揭晓我所知道或拥有的某样东西的前提下，向别人证明我有很大几率（这点很重要，零知识证明说到底是一个概率上的证明）确实知道或拥有这个东西。（有关零知识证明的简单原理可以参照[一个数独引发的惨案——零知识证明](https://zhuanlan.zhihu.com/p/34072069)这篇文章。）**零币**就是利用**零知识验证**来实现其功能的。

### 铸造零币

任何人都可以铸造一个零币，每一个零币价值一个基础币，只有把零币放到区块链网络上，并通过消耗一个基础币的方式，它才能具备价值。
**铸造零币的过程**：
1. 生成一个序列号S和一个随机密钥r。
2. 计算一个函数Commit(S, r)，这是序列号S的承诺。
3. 消耗一个基础币，在区块链上发布该承诺，进而创建了一个零币。（此时S和r仍然是保密的）

为了消耗一个零币并赎回新的基础币，你需要证明你之前已经铸造了一个零币，为了不揭示你的旧的基础币与新的基础币之间的关联，需要用到零知识验证。

**消耗一个序列号S的零币赎回一个新基础币的步骤**：
1. 创建一个特殊的“花费”交易，这个交易包含序列号S和一个具备零知识验证的声明：“我知道在承诺对象(S, r)中的r在以下的集合里：{c1, c2,..., cn}”。
2. 矿工验证你的零知识验证，这会给予你打开区块链中一个零币承诺的能力，而你并不需要真正的打开它。
3. 矿工查询序列号S，确认这个零币没有在之前被使用过。
4. 你的花费交易输出将会形成一个新的基础币，可使用你拥有的一个地址来作为输出地址。

**匿名性**：无论是铸币交易还是花费交易都没有展示过r，这就意味着没有人知道哪一个序列号对应哪一个具体的零币。

## 零钞

零钞使用的是zk-SNARKS的密码学技术，这种技术可以使得零知识验证更加简洁、更加高效。在零钞系统中，交易的金额大小被封装在一个承诺中，在区块链上不再可见，密码学证据会确保拆分与合并的正确性，用户不能凭空创造出零钞。
账本公开记录的唯一内容就是交易的存在性，以及矿工们用来验证系统正常运行所需要的关键属性的证明。区块链网络上既不显示交易地址，也不显示交易价值。唯一需要知道交易金额的用户，是本次交易的发送方和接收方，矿工们是不需要知道的。
零钞系统也需要一个“公开参数”来设置零知识验证系统，不同于零币系统，零钞系统中所需的公开参数大小超过1G字节，而零币中只需几百个字节长度。
