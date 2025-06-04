import requests
from ..modules.print_response import print_response

# 服务名称, 单纯用于让调试语句输出直观
service_name = "企业微信机器人"


# 推送到企业微信
def nw_wechat(html_message, title, server_url, at_all=False):
    # 由于传入的消息是HTML格式，而微信无法使用HTML格式，所以要将<br/>替换为换行符
    message = html_message.replace("<br/>", "\n")
    # 最终消息
    finally_msg = f"{title}\n\n{message}" if title else message
    # 请求体
    content = {
        "msgtype": "text",
        "text": {
            "content": finally_msg,
            # 是否选择@全体群员，也可以选择单独@指定的用户列表
            "mentioned_mobile_list": ["@all"] if at_all else [],
        },
    }
    # 发出请求
    response = requests.post(server_url, json=content)
    # 输出请求结果
    return print_response(service_name, server_url, response)
