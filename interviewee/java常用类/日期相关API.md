<!--
 * @Author: ZhXZhao
 * @Date: 2022-01-07 11:59:23
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2022-01-10 14:46:06
 * @Description: file content
-->
# 日期相关API

- System类中currentTimeMillis();方法
- java.util.Date和其子类java.sql.Date
- SimpleDateFormat类
- Calendar抽象类，实例化Calendar.getInstance()

上面API面临的问题：

- 可变性：像日期和时间这样的类应该是不可变的（应该去类似String）
- 偏移性：Date中年份从1900年开始，月份从0开始（例，
  ```java
  Date d = new Date(2020 - 1900, 9-1, 8)
  ```
  表示2020-09-08
- 格式化：格式化只对Date有用，Calendar不行（例，Date的格式化
  ```java
  SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss") //HH表示24小时进制，hh表示12小时进制
  ```
- 这些类都不是线程安全的，不能处理闰秒

## JDK8中新的日期时间API
> java.time
    >>java.time.format
    >>java.temporal

### LocalDate、LocalTime、LocalDateTime

- getXXX(): 获取相关属性 年月日时分秒毫秒纳秒
- withXXX(): 设置相关属性 年月日时分秒毫秒纳秒
- now()/of(): 实例化方法

### Instant

- now(): 实例化方法

### java.time.format.DateTimeFormatter

- ofPattern("yyyy-MM-dd")：实例化方法
- parse(): 解析
- format(): 格式化
格式化或解析日期、时间。


