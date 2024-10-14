from plugin.NotifyWind import NotifyWind

# 本文件需要移除当前目录到上一级, 也就是项目运行目录下否则导包路径对不上
# 关闭控制台语句只需额外传一个debug=False

NotifyWind(title="标题", message="内容喵")

# title = "一个标题"
# message = "测试内容"
# NotifyWind(title=title, message=message)
