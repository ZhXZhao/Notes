# ACIDRain: Concurrency-Related Attacks on Database-Backed Web Applications

----

## 先验知识

### 数据库事务的四个特性(ACID)

1. 原子性(A: Atomicity)
事务是数据库的逻辑工作单位，事务中包括的诸操作要么都做，要么都不做。
2. 一致性(C: Consistency)
事务执行的结果必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
3. 隔离性(I: Isolation)
一个事务的执行不能被其他事务干扰。即一个事务的内部操作及使用的数据对其他并发事务是隔离的，并发执行的各个事务之间不能互相干扰。
4. 持久性(D: Durability)
一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。

<p style="text-indent:2em">事务是恢复和并发控制的基本单位，保证事务ACID特性是事务管理的重要任务。事务ACID特性可能遭到破坏的因素有：</p>

1. 多个事务并行运行时，不同事务的操作交叉执行；

2. 事务在运行过程中被强行停止。

### 并发操作带来的问题

1. 丢失修改(lost update)

<table>
    <tr>
        <th>T1</th>
        <th>T2</th>
    </tr>
    <tr>
        <td>(1)R(A)=16</td>
        <td></td>
    </tr>
    <tr>
        <td>(2)</td>
        <td>R(A)=16</td>
    </tr>
    <tr>
        <td>(3)A<-A-1</td>
        <td></td>
    </tr>
    <tr>
        <td>W(A)=15</td>
        <td></td>
    </tr>
    <tr>
        <td>(4)</td>
        <td>A<-A-1</td>
    </tr>
    <tr>
        <td></td>
        <td>W(A)=15</td>
    </tr>
</table>

2. 脏读(dirty read)

<table>
    <tr>
        <th>T1</th>
        <th>T2</th>
    </tr>
    <tr>
        <td>(1)R(C)=100</td>
        <td></td>
    </tr>
    <tr>
        <td>C<-C*2</td>
        <td></td>
    </tr>
    <tr>
        <td>W(C)=200</td>
        <td></td>
    </tr>
    <tr>
        <td>(2)</td>
        <td>R(C)=200</td>
    </tr>
    <tr>
        <td>(3)ROLLBACK</td>
        <td></td>
    </tr>
    <tr>
        <td>C恢复为100</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>读到的C与<br>数据库中<br>内容不一致</td>
    </tr>
</table>

3. 不可重复读(non-repeatable read)

<table>
    <tr>
        <th>T1</th>
        <th>T2</th>
    </tr>
    <tr>
        <td>(1)R(A)=50</td>
        <td></td>
    </tr>
    <tr>
        <td>R(B)=100</td>
        <td></td>
    </tr>
    <tr>
        <td>求和=150</td>
        <td></td>
    </tr>
    <tr>
        <td>(2)</td>
        <td>R(B)=100</td>
    </tr>
    <tr>
        <td></td>
        <td>B<-B*2</td>
    </tr>
    <tr>
        <td></td>
        <td>W(B)=200</td>
    </tr>
    <tr>
        <td>(3)R(A)=50</td>
        <td></td>
    </tr>
    <tr>
        <td>R(B)=200</td>
        <td></td>
    </tr>
    <tr>
        <td>求和=250</td>
        <td></td>
    </tr>
    <tr>
        <td>（验算不对）</td>
        <td></td>
    </tr>
</table>

4. 幻读(phantom row)
    1. 事务T1按一定条件从数据库中读取了某些数据记录后，事务T2删除了其中部分记录，当T1再次按相同条件读取数据时，发现某些记录神秘地消失了
    2. 事务T1按一定条件从数据库中读取了某些数据记录后，事务T2插入了一些记录，当T1再次按相同条件读取数据时，发现多了一些记录。

并发控制的主要技术：**封锁**、时间戳、乐观控制法和多版本并发控制。

### 封锁

<p style="text-indent:2em">基本的封锁类型：排他锁（X锁）和共享锁（S锁）</p>
<p style="text-indent:2em"><b>排他锁（写锁）</b>若事务T对数据对象A加上X锁，则只允许T读取和修改A，其他任何事务都不能再对A加任何类型的锁，直到T释放A上的锁为止。<b>这就保证了其他事务在T释放A上的写锁之前不能再读取和修改A。</b></p>
<p style="text-indent:2em"><b>共享锁（读锁）</b>若事务T对数据对象A加上S锁，则事务T可以读A但不能修改A，其他事务只能再对A加S锁，而不能加X锁，直到T释放A上的S锁为止。<b>这就保证了其他事务可以读A，但在T释放A上的S锁之前不能对A做任何修改。</b></p>

### 封锁协议

1. 一级封锁协议
一级封锁协议是指，事务T在修改数据R之前必须先对其加X锁，**直到事务结束**（正常结束COMMIT和非正常结束ROLLBACK）**才释放**。**一级封锁协议可防止丢失修改。**
2. 二级封锁协议
二级封锁协议是指，在一级封锁协议基础上增加事务T在读取数据R之前必须先对其加S锁，**读完后即可释放S锁**。**二级封锁协议除防止了丢失修改，还可进一步防止读脏数据。**
3. 三级封锁协议
三级封锁协议是指，在一级封锁协议的基础上增加事务T在读取数据R之前必须先对其加S锁，**直到事务结束才释放**。**三级封锁协议除了防止丢失修改和读脏数据外，还进一步防止了不可重复读。**

![使用封锁机制解决三种数据不一致性的示例](D:/gitRepo/Notes/papers/SIGMOD2017-ACIDRain/pic/pic1.jpg  "使用封锁机制解决三种数据不一致性的示例")

<center>上图：使用封锁机制解决三种数据不一致性的示例</center>

<br>

![不同级别的封锁协议和一致性保证](D:/gitRepo/Notes/papers/SIGMOD2017-ACIDRain/pic/pic2.jpg "不同级别的封锁协议和一致性保证")

<center>上图：不同级别的封锁协议和一致性保证</center>

### 隔离等级

1. 读未提交(Read Uncommitted)：对应一级封锁协议

2. 读已提交(Read Committed)：对应二级封锁协议

3. 可重复读(Repeatable Read)：对应三级封锁协议

4. 串行化(Serializable)：事务不可并发执行

![隔离等级对应解决的数据不一致性问题](D:/gitRepo/Notes/papers/SIGMOD2017-ACIDRain/pic/pic3.jpg "隔离等级对应解决的数据不一致性问题")

<center>上图：隔离等级对应解决的数据不一致性问题（N代表该隔离等级下不存在该数据一致性问题，Y代表存在）</center>
