# wow 
## 在终端上输出ANSI图案

#### Demo


![demo1](https://github.com/chiwent/wow/blob/master/demo/demo1.png)<br>

![demo2](https://github.com/chiwent/wow/blob/master/demo/demo2.png)<br>

## 请注意，执行带-ixt的参数选项前请自行编译好img2xterm并且创建软链接

```bash
sudo ln -s img2xterm /usr/bin
```

注：<br>
下面这两个demo是通过直接调用编译好的`img2xterm`输出的，所以没有文字(当然，你也可以直接通过`imgxterm xxx.jpg`来实现，本身`imgxterm`就是一个可以输出图案的可执行文件）
<br>

![demo3](https://github.com/chiwent/wow/blob/master/demo/demo3.png)<br>

![demo4](https://github.com/chiwent/wow/blob/master/demo/demo4.png)<br>



## 关于本项目
fork自 [doge](https://github.com/thiderman/doge)和 [img2xterm](https://github.com/kfei/img2xterm?1525165239505)
<br>
大致介绍二者的联系：<br>

### doge
doge依赖于img2xterm,它需要后者输出的文件内容来确定图案(通过`img2xterm -p xxx.jpg xxx.txt`来导出文件，文件后缀还可以是.cow)
<br>


官方说明文档：<br>
[doge Readme](https://github.com/chiwent/doge/blob/master/README.md?1525165756047)
<br>

另外一个汉化的fork项目有中文翻译：<br>
[quin Readme](https://github.com/journey-ad/quin/blob/master/README.md?1525165932370)
<br>
 
### img2xterm

[Readme](https://github.com/kfei/img2xterm/blob/master/README.md?1525166071620)<br>

img2xterm依赖于 [ImageMagick](http://www.imagemagick.org/script/index.php) and [Ncurses](http://www.gnu.org/software/ncurses/ncurses.html)
<br>

本人在Ubuntu16.04上编译通过，通过下面命令安装：<br>

```bash
sudo apt-get install libmagickwand4 libncurses5-dev
```

补充说明：<br>
本人在Ubuntu16.04中无法通过上述命令直接安装`libmagickwand4`，可以到Ubuntu软件中心下载：<br>
https://launchpad.net/ubuntu/precise/amd64/libmagickwand4
<br>

使用上的问题可以通过终端提示内容查看，或者可以到`doc`文件夹下查看说明文档<br>
