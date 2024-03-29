<!--
 * @Author: ZhXZhao
 * @Date: 2020-02-22 20:57:34
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2020-02-22 21:33:26
 * @Description: 
 -->

# 去中心化共识和交易的独立验证

---

- [去中心化共识和交易的独立验证](#%e5%8e%bb%e4%b8%ad%e5%bf%83%e5%8c%96%e5%85%b1%e8%af%86%e5%92%8c%e4%ba%a4%e6%98%93%e7%9a%84%e7%8b%ac%e7%ab%8b%e9%aa%8c%e8%af%81)
  - [去中心化共识](#%e5%8e%bb%e4%b8%ad%e5%bf%83%e5%8c%96%e5%85%b1%e8%af%86)
  - [交易的独立检验](#%e4%ba%a4%e6%98%93%e7%9a%84%e7%8b%ac%e7%ab%8b%e6%a3%80%e9%aa%8c)

## 去中心化共识

比特币的去中心化共识由所有网络节点的4种独立过程相互作用产生：
- 每个全节点依据综合标准对每个交易进行独立验证。
- 通过完成工作量证明算法的验算，挖矿节点将交易记录独立打包进新区块。
- 每个节点独立地对新区块进行校验并组装进区块链。
- 每个节点对区块链进行独立选择，在工作量证明机制下选择累计工作量最大的区块链。

## 交易的独立检验

节点在收到网络中传播来的交易时，要对每一笔交易进行验证，验证标准如下：
- 交易的语法和数据结构必须正确。
- 输入与输出列表不能为空。
- 交易的字节是小于MAX_BLOCK_SIZE的。
- 每一个输出值，以及总量，必须大于0小于2100万个币。
- 没有哈希等于0，N等于负1的输入，即币基交易不能被中继。
- nLockTime是小于或等于INT_MAX的。
- 交易的字节大小是大于等于100的。
- 交易中的签名数量应小于签名操作数量上限。
- 解锁脚本只能将数字压入栈，锁定脚本应符合isStandard格式。
- 池中的一个匹配交易必须存在。
- 对于每一个输入，如果引用的输出存在于池中任何的交易，该交易将被拒绝。
- 对于每一个输入，若交易缺少任何一个输入，则放入孤立交易池。
- 对于每一个输入，如果引用的输出交易是币基交易，该输入必须至少获得COINBASE_MATURITY（100）个确认。
- 对于每一个输入，引用的输出必须存在且没被花费。
- 检查每一个输入值和总值是否大于0小于2100万。
- 如果输入值的总和小于输出值的总和，则交易中止。
- 若交易费用太低以至于无法进入一个空区块，交易将被拒绝。
- 每一个输入的解锁脚本必须依据相应输出的锁定脚本来验证。
