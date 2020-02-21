<!--
 * @Author: ZhXZhao
 * @Date: 2020-02-20 23:44:22
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2020-02-21 17:41:08
 * @Description: 
 -->

# 标准交易

---


- [标准交易](#%e6%a0%87%e5%87%86%e4%ba%a4%e6%98%93)
  - [P2PKH(Pay-to-Public-Key-Hash)](#p2pkhpay-to-public-key-hash)
  - [P2PK(Pay-to-Public-Key)](#p2pkpay-to-public-key)
  - [多重签名](#%e5%a4%9a%e9%87%8d%e7%ad%be%e5%90%8d)
  - [数据输出](#%e6%95%b0%e6%8d%ae%e8%be%93%e5%87%ba)
  - [P2SH(Pay-to-Script-Hash)](#p2shpay-to-script-hash)
    - [P2SH地址](#p2sh%e5%9c%b0%e5%9d%80)
    - [P2SH优点](#p2sh%e4%bc%98%e7%82%b9)
    - [赎回脚本和标准确认](#%e8%b5%8e%e5%9b%9e%e8%84%9a%e6%9c%ac%e5%92%8c%e6%a0%87%e5%87%86%e7%a1%ae%e8%ae%a4)

五大标准脚本：P2PKH, P2PK, MS(限15个密钥), P2SH和OP_RETURN。

## P2PKH(Pay-to-Public-Key-Hash)

比特币网络上的大多数交易都是**P2PKH交易**，此类交易都含有一个锁定脚本，该脚本**由公钥哈希实现阻止输出功能**，公钥哈希即为广为人知的比特币地址。由P2PKH脚本锁定的输出，可以通过输入公钥，由相应私钥创建的数字签名得以解锁。

锁定脚本为：

```
OP_DUP OP_HASH160 <Public Key Hash> OP_EQUAL OP_CHECKSIG
```

解锁脚本为：

```
<Signature> <Public Key> 
```

将两个脚本结合成有效的脚本：

```
<Signature> <Public Key> OP_DUP OP_HASH160 <Public Key Hash> OP_EQUAL OP_CHECKSIG
```

## P2PK(Pay-to-Public-Key)

在P2PK脚本模式中，公钥本身已经存储在锁定脚本中。

锁定脚本为：

```
<Public Key A> OP_CHECKSIG
```

解锁脚本为：

```
<Signature from Private Key A>
```

组合脚本为：

```
<Signature from Private Key A> <Public Key A> OP_CHECKSIG
```

## 多重签名

多重签名脚本设置了这样一个条件，假如记录在脚本中的公钥个数为N，则至少需提供其中的M个公钥才可以解锁，也被称为M-N组合。

锁定脚本为：

```
M <Public Key 1> <Public Key 2> ... <Public Key N> N OP_CHECKMULTISIG
```

解锁脚本为：

```
OP_0 <Signature 1> <Signature 2> ... <Signature M>
```

其中OP_0只是占位符，这为CHECKMULTISIG的一个小漏洞。

组合脚本为：

```
OP_0 <Signature 1> <Signature 2> ... <Signature M> M <Public Key 1> <Public Key 2> ... <Public Key N> N OP_CHECKMULTISIG
```

## 数据输出

比特币脚本不仅局限于支付领域，也可用于电子公证服务、证券认证和智能协议等领域。

OP_Return允许开发者在交易输出上增加40字节的非交易数据。OP_Return创造了一种明确的可复查的非交易型输出，此类数据无需存储于UTXO集。OP_Return的输出会被记录在区块链上，因此会导致磁盘空间的增加，因为不存储与UTXO集，所以不会增加内存的消耗。

OP_RETURN脚本样式：

```
OP_RETURN <data>
```

data被限制为不超过40字节。

## P2SH(Pay-to-Script-Hash)

多重签名脚本虽然强大，但是使用起来有许多不便：
1. 服务商需要在用户付款前将该脚本发送给用户，用户需要学会如何利用脚本完成交易。
2. 脚本中可能含有特别长的公钥，给用户造成额外的负担。
3. 一个长的交易脚本会一直记录在所有节点的内存中的UTXO集中，直到该笔资金被使用。

P2SH就是为解决这些问题而被引入的，目的是能使得这些复杂脚本的使用能够像直接付款到比特币地址一样简单。

在P2SH交易中，锁定脚本由哈希值取代，哈希指代的是赎回脚本。

P2SH脚本示例

| 赎回脚本(redeem script) | 2 PubKey1 PubKey2 PubKey3 PubKey4 PubKey5 5 OP_CHECKMULTISIG |
| ----------------------- | ------------------------------------------------------------ |
| 锁定脚本                | OP_HASH160 <20-byte hash of redeem script> OP_EQUAL          |
| 解锁脚本                | Sig1 Sig2 redeem script                                      |

锁定脚本中的20字节的哈希值是由整个赎回脚本先经过SHA256再经过RIPEMD160得到的。这样锁定脚本由一个长的脚本变成了一个短的脚本。

当服务商要花费这笔UTXO时，需要两步：
1. 将赎回脚本与锁定脚本对比确认其哈希值是否匹配：
   ```
   <2 PK1 PK2 PK3 PK4 PK5 5 OP_CHECKMULTISIG> OP_HASH160 <redeem scriptHash> OP_EQUAL
   ```
2. 如果赎回脚本的哈希值匹配，解锁脚本再执行以释放赎回脚本：
   ```
   <Sig1> <Sig2> 2 PK1 PK2 PK3 PK4 PK5 5 OP_CHECKMULTISIG
   ```

### P2SH地址

P2SH的另一重要特征是它能将脚本哈希编译为一个地址。**P2SH地址**是**基于Base58编码的一个含有20个字节哈希的脚本**，就像比特币地址是基于Base58编码的一个含有20个字节的公钥。

P2SH采用5作为前缀，导致基于Base58编码的地址以3开头。该地址与一个脚本相对应而非与一个公钥相对应，P2SH地址隐藏了所有的复杂性。

### P2SH优点

与直接使用复杂脚本以锁定输出的方式相比，P2SH具有以下特点：
1. 在交易输出中，复杂脚本由简短哈希值（电子指纹）代替，使得交易代码变短。
2. 脚本被编译为地址，支付者无需复杂工序即可执行P2SH。
3. P2SH将构建脚本的重担交给了接收方，而非发送方。
4. P2SH将长脚本的存储负担从输出方（存储于UTXO集，影响内存）转至了输入方（仅存储与区块链）。
5. P2SH将长脚本数据存储的重担从当前（支付时）转移至未来（花费时）。
6. P2SH将长脚本的交易费成本从发送方转移至接收方，接收方在使用该笔资金时必须含有赎回脚本。

### 赎回脚本和标准确认

不能将P2SH植入P2SH赎回脚本，因为P2SH不能自循环。也不能在赎回脚本中使用OP_RETURN，因为 OP_RETURN 的定义即显示不能赎回。P2SH交易即便在赎回脚本无效的情况下也会被认为有效。因为P2SH锁定脚本对于赎回脚本本身未提供任何描述。这样的处理机制也衍生出**一个风险**，你能将比特币锁定在一个未来不能被花费的P2SH中。
