# 问题

比如随便打开一个项目，图片都挂掉了

F12打开控制台看一哈

呦，一堆红色×。主要报错是Failed to load resource: net::ERR_××××××

去查了一下，博主john-zeng这样解释道：

实际上，可以认为，ERR_××××××就是用一个错误的域名访问了某个节点的https资源。导致这个错误的原因，基本是：

    dns污染
    host设置错误
    官方更新了dns，但是dns缓存没有被更新，导致错误解析。
我觉得像是有点道理，解决方法就粗来了，hin简单，往下看。

二、解决方法
主要思路就是使用本地hosts文件对网站进行域名解析，一般的DNS问题都可以通过修改hosts文件来解决，github的CDN域名被污染问题也不例外，同样可以通过修改hosts文件解决，将域名解析直接指向IP地址来绕过DNS的解析，以此解决污染问题。

2.1 找到URL
打开github任意带有挂掉图片的网页，使用元素选择器（Ctrl+Shift+C）放在显示不了的图片上，或者在挂掉的图片上右键-检查元素，定位到该图片的标签，那么你得到了它的URL，叫做src属性。

比如介个
在右面把它的网址复制粗来：

<https://avatars2.githubusercontent.com/u/15832957?s=60&v=4>

2.2 获取IP地址
得到上述网址以后打开IPAddress.com这个网站，在搜索框输入它的域名，就是"https:"//到"com"那一部分， 俗称二级域名：

avatars2.githubusercontent.com

回车！！！下面你会看到该域名的信息和IP地址：

可以看出IP是：151.101.184.133，并且是2019.05.05最后更新的，alright，那么我们就可以使这个IP和域名映射起来。

（其他如果有挂掉的图片一样使用此方法进行一一映射即可。）

2.3 修改hosts
具体咋映射呢？修改hosts文件！！！本人使用的是windows系统，所以使用Sublime Text打开：C:\Windows\System32\drivers\etc\hosts

在文件末尾添加：

选中以下复制粘贴

    # GitHub Start 
    192.30.253.112    github.com 
    192.30.253.119    gist.github.com
    151.101.184.133    assets-cdn.github.com
    151.101.184.133    raw.githubusercontent.com
    151.101.184.133    gist.githubusercontent.com
    151.101.184.133    cloud.githubusercontent.com
    151.101.184.133    camo.githubusercontent.com
    151.101.184.133    avatars0.githubusercontent.com
    151.101.184.133    avatars1.githubusercontent.com
    151.101.184.133    avatars2.githubusercontent.com
    151.101.184.133    avatars3.githubusercontent.com
    151.101.184.133    avatars4.githubusercontent.com
    151.101.184.133    avatars5.githubusercontent.com
    151.101.184.133    avatars6.githubusercontent.com
    151.101.184.133    avatars7.githubusercontent.com
    151.101.184.133    avatars8.githubusercontent.com

    # GitHub End
然后保存文件就OK了，至于无法保存，没有修改权限，鼠标右键-属性-安全-修改权限；或将hosts文件复制一份，修改之后，复制到原文件夹替换。

PS：另外要注意的一点就是，如果图片再次挂掉，只需要及时更新IP就行啦，这波操作不麻烦，你看我头像回来了！！！
