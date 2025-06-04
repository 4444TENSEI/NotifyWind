from plugin.NotifyWind import NotifyWind

title = "NotifyWind标题"
message = "NotifyWind内容"


def handler(event=None, context=None):
    # 关闭控制台语句只需额外传一个debug=False
    NotifyWind(title=title, message=message)


if __name__ == "__main__":
    handler()
