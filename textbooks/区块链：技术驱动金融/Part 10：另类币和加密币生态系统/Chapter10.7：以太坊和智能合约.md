<!--
 * @Author: ZhXZhao
 * @Date: 2020-02-16 17:56:33
 * @LastEditors  : ZhXZhao
 * @LastEditTime : 2020-02-16 22:03:55
 * @Description: 
 -->
# 以太坊和智能合约

---

- [以太坊和智能合约](#%e4%bb%a5%e5%a4%aa%e5%9d%8a%e5%92%8c%e6%99%ba%e8%83%bd%e5%90%88%e7%ba%a6)
  - [智能合约编程模式](#%e6%99%ba%e8%83%bd%e5%90%88%e7%ba%a6%e7%bc%96%e7%a8%8b%e6%a8%a1%e5%bc%8f)
  - [燃料](#%e7%87%83%e6%96%99)
  - [其他应用](#%e5%85%b6%e4%bb%96%e5%ba%94%e7%94%a8)
    - [以太坊的状态和账户余额](#%e4%bb%a5%e5%a4%aa%e5%9d%8a%e7%9a%84%e7%8a%b6%e6%80%81%e5%92%8c%e8%b4%a6%e6%88%b7%e4%bd%99%e9%a2%9d)
    - [以太坊的数据结构](#%e4%bb%a5%e5%a4%aa%e5%9d%8a%e7%9a%84%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84)
  - [以太坊项目](#%e4%bb%a5%e5%a4%aa%e5%9d%8a%e9%a1%b9%e7%9b%ae)

以太币（Ethereum）是一种雄心勃勃的另类币，致力于提供一种满足图灵计算要求的可编程语言，用这种语言可以编写脚本或者合约。

## 智能合约编程模式

智能合约最初是用来指使用计算机系统（或者其他自动化方式）来执行合约。

在以太坊体系，一个合约就是一个存在区块链里的程序。任何人支付一点费用，就可以用特定的操作将他的程序上传，建立一个以太坊合约。这个合约是用字节码(bytecode)写的，可以被特殊的以太坊专用虚拟机（Ethereum-specific Virtual Machine，简称EVM）执行。一旦合约上传，便永远存在在区块链里。智能合约有它自己的资金账户，其他用户可以调用程序里面开放的应用程序编程接口(API)合约可以收发款项。

## 燃料

以太坊支持循环语句，这就意味着以太坊合约有可能会无限循环地执行。为防止合约无限循环执行，因此以太坊通过一种“燃料费用”的机制来实现这一点。简单来说，每执行一条虚拟机器的指令，需要花费一小部分的燃料费用。燃料费用是通过以太坊体系内部被称为以太（ether）的货币来支付的。它只是在用来支付合约操作的时候才叫燃料费用。每次调用之前，必须设定燃料费用的最高限，也就是愿意支付价格的最大值。当达到这个值（燃料用完了），程序就会终止，发生的所有程序状态的变化就会被重新设置到原始状态。

## 其他应用

市场预计、智能资产、托管支付、微支付渠道和混合服务，都可以在以太坊体系里实现。

### 以太坊的状态和账户余额

账本的两种方法：基于账户和基于交易。
比特币是一个基于交易的账本。比特币的币值是无法分割的，交易实际上是在全局状态表上操作的，这个表称为“未花费交易输出列表”。
以太坊是基于账户的模式，以太坊存储了合约地址和状态的对照表的数据结构，同时存储每个普通地址的账户余额。

### 以太坊的数据结构

基于账户的账本需要精心设计的数据结构来存储记录。以太坊中的每个区块包含每个地址的目前状态（账户余额和交易数）的摘要，同时也包含每个合约的状态（余额和存储空间）。
每个合约的存储树结构映射256比特的地址和256比特的字节。这样可以存储巨量的（$2^{256}×256=2^{264}$ ）信息。
数据结构里面提供的摘要，使验证一个地址有多少余额或者空间变得相对容易。比如，不需要鲍勃从头到尾扫描整个区块链，爱丽丝就可以向鲍勃证明她有多少余额。

## 以太坊项目

与比特币相比，以太坊增加了以太坊专用虚拟机（EVM），一个全新编程模式，一个全新的数据结构。此外，以太坊中每个区块产生的时间间隔是12秒，以太坊的工作量证明采用的是一个混合的哈希方程。
