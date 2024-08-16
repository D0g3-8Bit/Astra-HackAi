# 基本流程

## 环境

windows安装nmap：[下载适用于 Linux/Mac/Windows 的免费 Nmap 安全扫描程序](https://nmap.org/download#windows)

## 命令以及结果处理提示词

#### 确定主机IP及所在网段

~~~cmd
ipconfig
~~~

ai处理结果提示词：**判断我的WLAN ipv4 address及其所在的网段并输出，只输出一个IP和一个IP段，不要出现其他文字**

#### 探测存活主机

扫描WLAN局域网存活主机并仅输出存活结果：

windows

~~~cmd
nmap -sn -v 192.168.47.0/24 -oG - | findstr /R /C:"Up"
~~~

linux

~~~sh
nmap -sn -v 192.168.47.0/24 -oG - | grep Up
~~~

ai处理结果提示词：**判断结果中存活的主机IP并输出，只输出IP，不要出现其他文字**

#### 端口扫描

获得一个简洁的列表，显示哪些端口是存活：

~~~cmd
nmap -p- -oG - 192.168.47.112
~~~

ai处理结果提示词：**整理结果，只回复我开启的端口号，分行输出**

#### 漏洞利用

执行攻击脚本：

~~~cmd
python exploit.py
~~~

## 步骤推进提示词：

接下来，你的所有输出内容时使用txt格式，不要使用markdown风格，不要加*，保留命令中的空格和$

当我向你提问：”攻击局域网内这台主机“的时候，只输出命令：$$ipconfig$$

以下要求中<>标注的内容需要你替换成他实际描述的内容

当你收到如个IP加一个该IP所在网段格式的信息时，记住IP并输出命令：

$$nmap -sn -v <这里填上信息中的网段> -oG - | findstr /R /C:"Up"$$

当你收到几行同网段IP时，输出命令：$$nmap -p- -oG <这里填上我之前让你记住的IP> $$

当你收到几行端口号且端口号中有10002时，输出命令$$python exploit.py$$

如果你明白了以上要求，回复”111“

英文版：

~~~
From now on, all your output should be in txt format. Do not use markdown style and do not include * symbols. Retain the spaces and $ symbols in the commands without omission.

When I ask you: "Attack this host in the local area network," only output the command: $$ipconfig$$.

In the following requirements, replace the content marked with <> with its actual description:

- When you receive information in the format of an IP address followed by the subnet it belongs to, remember the IP and output the command: $$nmap -sn -v <insert the subnet from the information here> -oG - | findstr /R /C:"Up"$$.
- When you receive several lines of the same subnet IPs, output the command: $$nmap -p- -oG <insert the remembered IP here> $$.
- When you receive several port numbers and one of them is 10002, output the command: $$python exploit.py$$.

If you understand the above requirements, reply with "111".
~~~