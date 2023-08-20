
# 介绍
Hlang是一款基于Python编写的支持中英文混合编程的动态语言。其简单易上手，适合作为新手入门的第一个计算机语言。

# Hlang基本使用

## 下载
前往：[https://gitee.com/Huterox/hlang](https://gitee.com/Huterox/hlang) 下载最新发行版本，就可以下载得到最新的Hlang。
![在这里插入图片描述](https://img-blog.csdnimg.cn/9c618c3e4e7b42f5ba83ef7cb4fda0c2.png)

下载解压，得到完整的目录。
![在这里插入图片描述](https://img-blog.csdnimg.cn/9306ba8a2eb946ae94ddc0a9807c9fb5.png)
点击：
![在这里插入图片描述](https://img-blog.csdnimg.cn/000e69d248e34c3ca9e8012bb9cd2ddb.png)
就可以打开Hlang。
接下来，我们就可以来一个最经典的"Hello world"。
![在这里插入图片描述](https://img-blog.csdnimg.cn/b04a192b7f274213925e858e2b090965.png)

## 配置环境变量
为了能够跟好的使用Hlang,因此在下载Hlang之后，可以为此配置环境变量。这样一来在终端就能快速打开Hlang。

打开高级系统设置：

![在这里插入图片描述](https://img-blog.csdnimg.cn/360faed233524cff8dedb0c3ddcffb0a.png)
点击环境变量配置：
![在这里插入图片描述](https://img-blog.csdnimg.cn/26279b5d89b7432a9e0cfc64a1cd416c.png)
然后点击添加环境变量即可：
![在这里插入图片描述](https://img-blog.csdnimg.cn/7fd418c86389499380f72ccb9350bd67.png)

之后打开终端输入 Hlang.exe即可进入Hlang终端：
![在这里插入图片描述](https://img-blog.csdnimg.cn/c00032c65c6d45419fdf3146cf231488.png)
# 特性


Hlang作为一个教学语言，因此，为了大大降低入门门槛，支持在支持英文编程的同时，支持中文编程。
接下来请看到这几个案例。
## 中文关键字
![在这里插入图片描述](https://img-blog.csdnimg.cn/dee8e8bc22854aff813fafee890a6e23.png)
通过关键字 `设` 就可以创建一个变量。同时也支持英文：
![在这里插入图片描述](https://img-blog.csdnimg.cn/8b98e0e2336549fea5e19dd0507943ef.png)

## 支持中文符号

此外，支持多个关键字混合编程，同时支持中文标点：
这是一个数学运算案例：
![在这里插入图片描述](https://img-blog.csdnimg.cn/465b10180d8b45b5adbf768404494c03.png)
之后的话，切换为中文：
![在这里插入图片描述](https://img-blog.csdnimg.cn/00b78c3db4ef47febe3188aa79dfb574.png)
可以发现依然可以正常工作，并且中英文字符同时出现在一个表达式当中
## 混合编程
在实际编程当中，中文关键字和英文关键字可以同时出现：

![在这里插入图片描述](https://img-blog.csdnimg.cn/84edb1874d7a4d3c85943401cbbf6f3d.png)
## 中文错误提示
为了更加方便学习和定位错误，Hlang支持中文报错：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2ab6e215f56c42138f48f87b209298fd.png)
## 终端多行输入
此外，Hlang在终端也支持多行输入语句。通过 ; 进行间隔。（在代码文本当中，也支持;进行语句隔断，也可以直接通过换行）

![在这里插入图片描述](https://img-blog.csdnimg.cn/d5a0dd7f41df46658d618c70ac2c2b99.png)

# 基本数据类型
Hlang支持如下数据结构：
## 整数
![在这里插入图片描述](https://img-blog.csdnimg.cn/1dc0e565bc2b4420b7cfdd81610e997e.png)
## 浮点数
![在这里插入图片描述](https://img-blog.csdnimg.cn/47d1bc50e16c461fa476559f78449805.png)
## 列表
![在这里插入图片描述](https://img-blog.csdnimg.cn/6d810f0876d946cc89427abd5bed7039.png)
## 字符串
![在这里插入图片描述](https://img-blog.csdnimg.cn/59e443cb17414853a88d3acc3adb3e68.png)
# 基本操作

在Hlang当中支持如下关键字：

```
KEYWORDS = [
    'var',
    '设',
    'and',
    '且',
    'or',
    '或',
    'not',
    '否',
    'if',
    '如果',
    'elif',
    '再者',
    'else',
    '不然',
    'for',
    '遍历',
    'to',
    '到',
    'step',
    '步长',
    'while',
    '循环',
    'fun',
    '函数',
    'then',
    '就',
    'end',
    '结束',
    'return',
    '返回',
    'continue',
    '继续',
    'break',
    '终止'
]
```

同时支持如下内置函数：

IO函数：

> 1. print()  输出函数
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/3fe026cda0ef4eb4a4ec89425193d40d.png)
>
> 2. print_ret() 带返回值的输出函数
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/53867da71bdf40199ec62e26784fe0f1.png)
>
> 3. input() 输入函数
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/7f23a9e3b1cc4b8291a11cdfe27794f5.png)
>
> 
> 4. input_int()  与输入函数类型，只是将其转化为整数类型
> 5. clear()  在终端当中，清空输出
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/a942e197a37545f1afea48a559c616cf.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/344c8cf87d7641a9b18e1f2179589d71.png)


类型判断函数：
只需要将目标变量传入函数即可

> 1. is_num() 
> 2. is_stri()
> 3. is_list()
> 4. is_fun()

示例：
![在这里插入图片描述](https://img-blog.csdnimg.cn/8131babf20ba40628c42cc8c7a81b85f.png)

对数据的操作函数：

> 1. append()
> 2. pop()
> 3. extend()
> 4. len()

脚本执行函数：

> 1. run_file()

编写Hlang脚本：

```python
print("Hello world")
```
执行成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/d8e9105d8d7f4d04841c43396c92eb88.png)

## 变量定义

通过关键字 var a=3 就可以快速创建一个关键字。
同时也可以通过 设 a=3 来快速创建关键字。

## 逻辑判断
在Hlang没有专门的True，False的Boolean类型。而是返回实数0,1来表示。当返回为0是表示假，为1时表示为真。
例如：
![在这里插入图片描述](https://img-blog.csdnimg.cn/303419587ff24c8eaa0a51f72acbb32c.png)
同时这里支持not关键字：
![在这里插入图片描述](https://img-blog.csdnimg.cn/fcc4f70ba49945c6929c31813997e823.png)

## 基本运算
Hlang支持基本运算：
![在这里插入图片描述](https://img-blog.csdnimg.cn/a818795431fd4238917cff3475f3dfc7.png)
同时支持次幂运算：
![在这里插入图片描述](https://img-blog.csdnimg.cn/4ba801cbe9034df5b85f0534f5918af6.png)

## 条件判断
基本语法如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/3ecdb39029434b1daef9a6da1c8aac27.png)
运行结果如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/95e664966b3e4bdfa119a8f33c8f2960.png)

注意在这里依然支持中文：
![在这里插入图片描述](https://img-blog.csdnimg.cn/6d2777e6e9374f09bde12b3007b54a93.png)

## 循环
Hlang支持for循环和while循环：

![在这里插入图片描述](https://img-blog.csdnimg.cn/59b835fd419749fab805196abafd0f4e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/fc751e0b6ce841ce8106b06309264658.png)
注意这里的结果是从1到5但是不包括5.同时你还可以指定步长。

```python
for i=1 to 5 step 1 then
    print("Hello")
end
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/858c483425e946fd955a7659b419924f.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/2fda76a13ca04f40aa72329f1c84e498.png)
## 函数
之后是Hlang的函数定义：
![在这里插入图片描述](https://img-blog.csdnimg.cn/8a2bc8f38011445480ecec8d67abf6d6.png)

执行结果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/d3f5343dfa9447bbb00c3aa0cb008ceb.png)

注意在终端的话，也可以这样定义函数：
![在这里插入图片描述](https://img-blog.csdnimg.cn/c417beab9b484c8fb87c5649a8dd6a97.png)

同理，我们依然可以使用中文进行编程
![在这里插入图片描述](https://img-blog.csdnimg.cn/f138c30342be4dc881eea3ea7d2924f5.png)
