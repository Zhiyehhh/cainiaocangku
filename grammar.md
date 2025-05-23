# 语法一：标题
## 1、使用 #
使用 # 可以表示一到六级标题
## 2、使用 = 或 -
2-1 使用 = 表示一级标题
如：
这是一级标题
==============
这是二级标题
--------------

# 语法二：段落格式
## 1、换行
空一行

## 2、字体
2-1 斜体
*斜体字*
_斜体字_

2-2 粗体
**粗体字**
__粗体字__

2-3 粗斜体
***粗斜体***
___粗斜体___

## 3、分隔线
使用三个以上的星号*、减号-、底号_建立分割线，行内不能存在其他东西
***
---
___

## 4、删除线
~~删除线~~

## 5、下划线
<u>下划线</u>

## 6、脚注
这是脚注[^要注明文本]
[^要注明文本]: 这是脚注

# 语法三：列表
## 1、无序列表
使用星号*、加号+、减号-作为标记，要有空格
* 第一行

+ 第一行
 
- 第一行
  
## 2、有序列表
数字加点.
1. 第一行

## 3、列表嵌套
在子列表前添加两个或四个空格
1. 第一行
    - 元素一
  
# 语法四：区块
段落开头用 > 和空格
> 这是区块
> 1. 这是区块嵌套列表

# 语法五：代码
## 1、代码片段
用反引号包起来
`print()`

## 2、代码区块
用三个反引号 ` 包起来，可以指定语言
```CPP
class markdown(){
   pass;
};
```

# 语法六：链接
> 1. [菜鸟仓库MARKDOWN](https://www.runoob.com/markdown/)
> 2. <https://www.runoob.com/markdown/>
> 3. 高级链接：用变量设置链接，在文档结尾为变量赋值（地址）
>   这是链接[菜鸟仓库][Runoob]
> 
>   [Runoob]: https://www.runoob.com/markdown

# 语法七：图片
> 语法为`![alt 属性文本](图片地址)`
> ![RUNOOB 图标](https://static.jyshare.com/images/runoob-logo.png)
> 也可以对图片网址使用变量

> 可以用 `<img>` 标签指定图片高宽
> <img src="https://static.jyshare.com/images/runoob-logo.png" width="50%">

# 语法八：表格
> 可以用 `|` 分隔不同单元格
> 可以用 `-` 分隔表头和其他行
> | class | 1 | 2 |
> |-------|---|---|
> | car   |   |   |

> 对齐方式
> `-:` 右对齐
> `:-` 左对齐
> `:-:` 居中对齐
> |右对齐|左对齐|居中对齐|
> |-----:|:------|:------:|
> |car|car|car|

# 语法九：高级技巧
1. > 支持的HTML元素
   > 使用<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd>重启电脑
2. > 转义，用于显示特定符号
   > \*, \+, \-, \\, \{
3. > 数学公式
   > * `$...$`或`\(...\)`表示行内公式
   >   $sin(x)=sqrt(1-cos(x)^2)$
   > * `$$...$$`或`\[...\]`表示块内公式
   >   $$sin(x)=sqrt(1-cos(x)^2)$$