<!--
 * @Author: ZhXZhao
 * @Date: 2020-02-16 17:37:12
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2020-02-16 17:37:26
 * @Description: 
 -->
# 互换不同的货币

---



例：爱丽丝想卖掉a个另类币给鲍勃，换得鲍勃的b个比特币。通过如下协议可以做到：
1. 爱丽丝创建如下a个另类币的可以退还存款：
   1.1 爱丽丝创建一个随机的字符串x，计算哈希值h=H(x)
   1.2 爱丽丝创建如下图所示存储A区块，但是并不公开
   1.3 爱丽丝创建再融资A区块，并让鲍勃签名
   1.4 一旦鲍勃在再融资A区块签名，爱丽丝公开存储A区块（但是还没有公开再融资A区块）
2. 鲍勃创建如下可以退还的存款b比特币：
   2.1 鲍勃创建如下图所示存储B区块，但是不公开
   2.2 鲍勃创建再融资B区块，让爱丽丝签名。
   2.3 一旦爱丽丝在再融资B区块签名，鲍勃公开存储B区块（但是还没有公开再融资B区块）
3. 情景1：爱丽丝按照计划完成兑换
   3.1.1 在$T_1$爱丽丝索回比特币，把x给鲍勃（和其他所有人）
   3.1.2 在$T_2$索回另类币
   情景2：爱丽丝改变主意，不要比特币，也不要让鲍勃知道x值
   3.2.1 在$T_1$鲍勃索回他的比特币
   3.2.2 在$T_2$爱丽丝索回她的另类币
