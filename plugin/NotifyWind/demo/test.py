from plugin.NotifyWind import nw_pushplus, nw_gotify, nw_ntfy


# 本文件需要移除当前目录到上一级, 也就是项目运行目录下否则导包路径对不上
# 为方便后续集成到个人项目做的单独调用, 其实没太大必要这样做
# 应该像目前的index.py那样从配置文件/环境变量里面读配置信息是才是最安全和便捷的
nw_title = "测试标题"
nw_message = "测试内容喵"

nw_gotify(
    title=nw_title,
    message=nw_message,
    server_url="https://example.com",
    token="xxxxxxxxxxxxxxxxxxxx",
    priority=8,
    method="post",
    debug=True,
)
nw_ntfy(
    title=nw_title,
    message=nw_message,
    server_url="https://example.com",
    token="xxxxxxxxxxxxxxxxxxxx",
    priority=4,
    method="put",
    debug=True,
)
nw_pushplus(
    title=nw_title,
    message=nw_message,
    token="xxxxxxxxxxxxxxxxxxxx",
    method="put",
    debug=True,
)
