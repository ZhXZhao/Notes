<!--
 * @Author: ZhXZhao
 * @Date: 2020-11-14 15:41:46
 * @LastEditors: ZhXZhao
 * @LastEditTime: 2020-11-14 16:43:47
 * @Description:
-->
# java获取Array中最大最小值以及与List的转换

## java获取Array中最大最小值

### 使用stream

```java
int max = Arrays.stream(array).max().getAsInt();
```

### 使用collection
使用collection首先需要把**数组**转换为**对象数组**。即int[] 转换 为Integer[]，然后调用collection中的max和min。

```java
int array[] = {18 ,23 ,21 ,19 ,25 ,29 ,17};
Integer newarray[] = new Integer[array.length];
for(int i = 0;i<array.length;i++){
    newarray[i] = (Integer)array[i];
}
int max = Collections.max(Arrays.asList(newarray));
```

### 手动获取（推荐使用，效率最高）

```java
int array[] = {18 ,23 ,21 ,19 ,25 ,29 ,17};
int max = array[0];
for(int i = 1;i<array.length;i++){
    if(array[i] > max){
        max = array[i];
    }
}
```

## array与List的转换

### int[] 转 Integer[]

解析：
1. 使用Arrays.stream将int[]转换成IntStream。
2. 使用IntStream中的boxed()装箱，将IntStream转换成Stream<Integer>。
3. 使用Stream的toArray，传入IntFunction<A[]> generator，这样会返回Integer数组，否则默认是Object[]。

```java
Integer[] integers1 = Arrays.stream(array).boxed().toArray(Integer[]::new);
```

### Integer[] 转 int[]

解析：
1. 先将Integer[]转成Stream<Integer>。
2. 然后用mapToInt()方法，将Stream<Integer>转成IntStream。
3. 最后用toarray()方法，转成int[]。

```java
int[] arr2 = Arrays.stream(integers1).mapToInt(Integer::valueOf).toArray();
```

### Integer[] 转 List<Integer>

```java
List<Integer> list2 = Arrays.asList(integers1);
```

### List<Integer> 转 Integer[]

```java
Integer[] integers2 = list1.toArray(new Integer[0]);
```

### int[] 转 List<Integer>

解析：
1. 首先将int[]转成IntStream，可使用Arrays.stream(arr)或者IntStream.of(arr)。
2. 使用IntStream中的boxed()装箱，将IntStrean转成Stream<Integer>。
3. 使用Stream的collect()，将Stream<T>转换成List<T>。

```java
List<Integer> list1 = Arrays.stream(data).boxed().collect(Collectors.toList());
```

### List<Integer> 转 int[]

解析：
1. 想要转成int[] ，就要先转成IntStream，然后用toArray()方法转成int[]。
2. 过程同Integer[] 转 int[]。

```java
int[] arr1 = list1.stream().mapToInt(Integer::valueOf).toArray();
```

上述转成stream的方法效率都不高，如果数据量很大的话，最好采用手动转换的方式即for循环的方式转换。

