# 功能

**实现每日晚归打卡的自动打卡(需要提前登录电脑QQ)**

实现步骤:自动登录, 输入姓名,学号, 自动定位(定位失败时尝试重新定位)





# **使用方法**



### 直接双击运行main.exe即可 $_{(大概率报毒, 需要点击仍要运行)}$

第一次运行需要输入姓名,学号,打卡的链接(不要输入短网址) 之后就不需要了

如果**输入错误**直接修改data.txt(第一行是姓名,第二行是学号,第三行是打卡网址)

所以如果要移动文件, 请把data.txt 和 main.exe一起移动

如果打卡成功/打卡失败, 终端的最后一行会输出“自动打卡成功/自动打卡失败”

#### 如果打卡成功, 那其余报错不用管



# 每日打卡

运行main.exe只能实现**单次打卡**, 每天都点击还是比较麻烦.

所以可以添加**windows任务计划**, 实现每日自动打卡(但是第一次还是得双击运行, 目的是初始化data.txt, 当然你也可以直接修改data.txt).

参考<a href="https://blog.csdn.net/Tangcutudou/article/details/118706448">这篇博客</a>设置windows任务计划. 具体参数的可以参照我的来设置.

<br>

### 触发器选项

起始时间选择当天的晚上8:00(只要晚于打卡收集表开始收集的时间即可)

![img1](\image\img1.png)



#### 操作选项

![img2](\image\img2.png)

程序或脚本: 你的main.exe的路径

添加参数: 同上(或者不写也行)

起始于: 你的main.exe所在目录,即main.exe的路径去掉最后的main.exe即可



## 下载

下载可以到<a href="https://github.com/Ni-Sun/Auto-clock-in/tree/v1.1.0">我的github仓库</a>下载, 下载最新版本即可

下载大概率会报毒, 需要点击**保留文件**. 如果无法下载需要去windows安全中心关闭实时保护. 具体操作参考<a href="https://blog.csdn.net/m0_74188229/article/details/137543471?fromshare=blogdetail&sharetype=blogdetail&sharerId=137543471&sharerefer=PC&sharesource=qq_73781710&sharefrom=from_link">下载文件检测到病毒 无法被下载 程序被阻止 解决办法.</a> 或者可能需要关闭其他防毒软件.

运行时也需要点**仍要运行**





