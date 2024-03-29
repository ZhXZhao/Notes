<!--
 * @Author: ZhXZhao
 * @Date: 2021-05-25 20:02:18
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2021-05-25 23:02:46
 * @Description:
-->

# Socket

## I/O模型

套接字中的输入操作可以分为两步：
1. 等待数据从网络中到达，将数据从网卡复制到内核缓冲区。
2. 将数据从内核缓冲区复制到用户进程缓冲区。

Unix五种I/O模型：
- 阻塞式I/O
- 非阻塞式I/O
- I/O复用
- 信号驱动式
- 异步I/O

### 阻塞式I/O
应用进程被阻塞，直到数据从内核缓冲区复制到应用进程缓冲区中才返回。

由于该进程被阻塞，其他进程还可以执行，不消耗CPU时间，CPU利用率较高。

recvfrom()用于接收Socket传来的数据，并复制到应用进程的缓冲区中。

![阻塞式I/O](img/阻塞式IO.png)

### 非阻塞式I/O
应用进程执行系统调用（recvfrom()）后，内核返回一个错误码，应用进程可以继续执行，但是需要不断地执行系统调用（recvfrom()）来获知I/O是否完成。

由于CPU要处理更多的系统调用，所以CPU利用率较低。

![非阻塞式I/O](img/非阻塞式IO.png)

### I/O多路复用
使用select/poll/epoll等待数据，并且可以等待多个套接字中的任何一个变为可读，这一过程会被阻塞，当某一个套接字可读后，使用recvfrom()把数据从内核复制到进程中。

可以使得单个进程具有处理多个I/O事件的能力。

![I/O多路复用](img/IO多路复用.png)

### 信号驱动I/O
应用进程使用sigaction系统调用，内核立即返回，应用程序可以继续执行，等待数据到达内核缓冲区之前，应用进程都是非阻塞的。内核在数据到达时，向应用程序发送SIGIO信号，应用进程收到信号后调用recvfrom()将数据从内核复制到应用进程中。

相比于非阻塞式I/O的轮询方式，信号驱动I/O无需不断执行系统调用，CPU利用率更高。

![信号驱动I/O](img/信号驱动IO.png)

### 异步I/O
应用进程执行aio_read系统调用后会立即返回，应用进程可以继续执行，不会被阻塞，内核会在所有操作完成后向应用进程发送信号。

异步I/O与信号驱动I/O的区别在于，异步I/O的信号是通知应用进程I/O完成，而信号驱动I/O的信号是通知应用进程可以开始I/O。

![异步I/O](img/异步IO.png)

### 五种I/O模型比较
- 同步I/O：将数据从内核缓冲区复制到应用进程缓冲区的阶段（第二阶段），应用进程会被阻塞。
- 异步I/O：第二阶段应用进程不会被阻塞。

同步I/O包括阻塞I/O，非阻塞I/O，I/O复用，信号驱动I/O，他们的主要区别在于数据从网卡到内核缓冲区的阶段（第一阶段）。
非阻塞I/O、信号驱动I/O、异步I/O在第一阶段不会阻塞。

![五种I/O模型比较](img/五种IO模型比较.png)

## I/O多路复用
select/poll/epoll都是I/O多路复用的具体实现，select出现得最早，之后是poll，再是epoll。

### select

```cpp
int select(int n, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout);
// n:监控的文件描述符集里最大文件描述符加1
// readfds：监控有读数据到达文件描述符集合，传入传出参数
// writefds：监控写数据到达文件描述符集合，传入传出参数
// exceptfds：监控异常发生达文件描述符集合, 传入传出参数
// timeout：定时阻塞监控时间，3种情况
//  1.NULL，永远等下去
//  2.设置timeval，等待固定时间
//  3.设置timeval里时间均为0，检查描述字后立即返回，轮询
// 成功调用返回结果大于0（返回就绪文件描述符的个数），出错返回结果为-1，超时返回结果为0
```

select允许应用程序监视一组文件描述符，等待一个或多个描述符成为就绪状态，从而完成I/O操作。

- select调用需要传入fd（文件描述符）数组，将fd数组拷贝一份到内核，高并发场景下这样的拷贝消耗的资源是惊人的。。
- 在内核中，select仍是以遍历的方式检查文件描述符的就绪状态，是一个同步过程，只是减少了系统调用切换上下文的开销。
- select仅返回就绪文件描述符的个数，具体哪个就绪仍需要用户自己遍历。

### poll
poll和select基本相同，也是等待一组文件描述符中一个或多个成为就绪状态。
与select的不同点：
1. select会修改文件描述符，而poll不会。
2. select文件描述符使用数组实现，默认大小为1024，而poll没有描述符数量的限制。

### epoll
epoll_ctl()用于向内核注册新的描述符或者是改变某个文件描述符的状态。已注册的文件描述符在内核中被维护在一棵**红黑树**上，通过回调函数内核会将I/O准备好的描述符加入到一个链表中管理，进程调用epoll_wait()便可以得到事先完成的描述符。

也就是说：
- 内核中保存一份文件描述符集合，无需用户每次都重新传入，只需要告诉内核修改的部分即可。
- 内核不再通过轮询的方式找到就绪的文件描述符，而是通过异步I/O事件唤醒。
- 内核仅会将有I/O事件的（就绪的）文件描述符返回给用户，用户也无需遍历整个文件描述符集合。

## 应用场景

### select应用场景
select的timeout参数精度为微秒，而poll和epoll为毫秒，select适用于实时性要求较高的场景。

select可移植性好，几乎被所有主流平台支持。

### poll应用场景
没有最大文件描述符数量限制，如果实时性要求不高，应该用poll

### epoll应用场景
有大量的文件描述符需要同时轮询，且这些连接都是长连接可以用epoll。

需要同时监控小于1000个描述符，没必要使用epoll。

需要监控的描述符状态变化多，而且都非常短暂，也没必要使用epoll。因为描述符状态的频繁变化会导致频繁地触发系统调用（epoll_ctl()），降低了效率。




