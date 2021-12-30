<!--
 * @Author: ZhXZhao
 * @Date: 2021-12-30 20:33:14
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2021-12-30 20:47:21
 * @Description: file content
-->

# nginx.conf

三部分组成

1. 全局块
   从配置文件开始到events块之间的内容，主要会设置一些影响nginx**服务器整体运行**的配置指令，包括配置运行nginx服务器的用户组、允许生成的worker_process数、进程PID存放路径、日志存放路径和类型以及配置文件的引入。worker_processes值越大，可以支持的并发数越多。
2. events块
   events块涉及的指令主要影响nginx服务器与用户的**网络连接**，worker_connections表示每个workprocess支持的最大连接数。
3. http块
   配置最频繁的部分。
   1. http全局块
      指令包括文件引入include、MIME-TYPE定义、日志自定义、连接超时时间、单连接请求数上限等。
   2. server块
      1. server全局块
      2. location块
