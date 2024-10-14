from plugin.NotifyWind import NotifyWind

title = "NotifyWind标题"
message = "NotifyWind内容"


def handler(event, context):
    # 关闭控制台语句只需额外传一个debug=False
    NotifyWind(title=title, message=message)


# 开发环境时保留这句, 但是请注意在部署时要注释或移除这行, 因为云函数会自动运行一次handler, 不注释掉会造成连续推送2次
handler(0, 0)
