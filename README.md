

<p align="center"><img src="https://testingcf.jsdelivr.net/gh/4444TENSEI/CDN/img/avatar/AngelDog/AngelDog-rounded.png" alt="Logo"
    width="200" height="200"/></p>
<h1 align="center">NotifyWind</h1>
<h4 align="center">Python统一消息推送服务集成工具，皆在便捷集成第三方/开源自部署消息推送服务。例如你将自己的Python脚本集成本项目SDK，定时运行服务(器)监控、定时查成绩、定时签到、定时任务后，将运行状态直接发送微信or系统通知到你的手机上查看。</h4>
<p align="center">
<img src="https://img.shields.io/badge/Python-276DC3?style=for-the-badge&logo=python&logoColor=white" />
</p>    




> ## 简介

本SDK现已集成4个主流的消息服务（微信公众号pushplus、企业微信机器人、Gotify、ntfy）接口，配置简易、本体轻量，无需通过pip安装，只需clone本仓库至您的项目根目录下，修改根目录的`config.NotifyWind.json`配置文件为您的推送服务环境变量，引入推送函数即可一次性推送消息至多平台。

> ## 应用实例

1. ### v0.1.0版本已集成于：[由云函数实现的HTTP服务定时监控+消息推送定时任务](https://github.com/4444TENSEI/NotifyMonitor)


### 目前支持的推送服务：

1. 微信公众号（每日免费200次调用次数）：`pushplus`
2. 自部署服务（无调用限制，通过各自`APP`接收通知）：`ntfy`、`gotify`

`华为云函数`+`pushplus微信推送`两家服务的免费额度非常够用，现在只需在你的Python定时任务中集成这个项目，部署到云函数上，配置定时运行，即可被动等待运行状态推送到手机上，个人用户只需申请一个pushplus账号，一小会就注册好了。

### 基础调用：

```
from plugin.NotifyWind import NotifyWind

title = "自定义消息标题"
message = "自定义消息内容"

NotifyWind(title=title, message=message)
```

## 环境变量/配置文件

支持**同时推送**到多平台，下方示例中仅使用pushplus，实际还有ntfy和gotify的配置项，参考本仓库根目录下的`config.NotifyWind.json.example`

更推荐使用`环境变量`方式，而不是写在实际配置文件中（开发环境还是需要使用本地json文件，自行去除项目根目录的`config.NotifyWind.json.example`的`.example`后缀即可，可自行删除不需要的推送服务键值对，此处debug控制调试语句不要删除）。

```json
{
    "pushplus": {
        "token": "xxxxxxxxxxxxxxxxxxxx"
    },
    "ntfy": {
        "server_url": "https://xxxxxx.com",
        "token": "xxxxxxxxxxxxxxxxxxxx",
        "priority": 4
    },
    "gotify": {
        "server_url": "https://xxxxxx.com/message",
        "token": "xxxxxxxxxxxxxxxxxxxx",
        "priority": 8
    },
    "wechat": {
        "server_url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxx"
    },
    "debug": true
}
```

> # 免费部署到华为云函数

此时此刻，你完全可以在仅仅修改配置文件的情况下直接进行部署了（除了pushplus实名需要一元钱），下方是针对未使用过华为云函数的用户所写的示例，老玩家也许不需要看了（提醒老玩家：环境变量键名为`NOTIFYWIND`）。

> ## 图文教程

1. 拉取项目源码或者是直接点击[**前往下载**](https://github.com/4444TENSEI/NotifyMonitor/releases/latest)，找到`Source code(zip)`字样，下载最新版源码`ZIP`压缩包，用于上传到华为云函数
2. 查看**图文部署教程**：[华为云函数部署Python定时任务](https://blog.yokaze.top/archives/930)，
3. ※ 需要在**环境变量**中配置`键`为`NOTIFYWIND`，`值`就是下方json配置文件中的内容，关键部位自行修改

> ## 获取TOKEN
>

- ### 获取`pushplus`的token：

前往官网：[pushplus官网](https://www.pushplus.plus/push1.html)。注册、绑定微信公众号、实名，短短几分钟即可获取到token。

- ### 获取`gotify`的token：

什么？既然你都会部署了，在右上角APPS里面点`CREATE APPLICATION`创建一个不就出来了。

- ### 获取`ntfy`的token：

一般你部署下来是不需要的，如不需要可以在配置文件json中删掉这组键值对。

如果你真的在自己在部署时设定了角色权限，那么在你的服务器上面运行

- 如果你没有创建管理员，那么创建

```
ntfy user add --role=admin Admin123
```

- 如果你没有生成token，那么生成（这里是100年有效期...）

```
ntfy token add --expires=36500d --label="long-term-access" Admin123
```

