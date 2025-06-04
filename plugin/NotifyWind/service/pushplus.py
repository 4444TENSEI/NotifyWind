import requests, random
from ..modules.print_response import print_response

# 服务名称, 单纯用于让调试语句输出直观
service_name = "PushPlus微信公众号"

# 官方固定推送接口
server_url = "https://www.pushplus.plus/send"


# 推送到pushplus
def nw_pushplus(
    message,
    title=None,
    token=None,
):
    # 可有可无的请求头
    headers = {"Content-Type": "application/json"}
    # 参数
    json = {
        "token": token,
        "title": title,
        "content": insert_invisible_tags(message),
        "template": "html",
    }
    # 发出请求
    response = requests.post(
        server_url,
        json=json,
        headers=headers,
    )
    # 输出请求结果
    return print_response(service_name, server_url, response)


# 由于pushplus会对于重复消息做频繁限制, 咱直接随机生成随机的不可见HTML标签, 每次推送时加入, 防止被检测到频繁发送消息导致的999状态码
def insert_invisible_tags(content):
    invisible_tag = '<span style="display:none;"/>'
    # 随机插入1到30个
    num_tags = random.randint(1, 30)
    for _ in range(num_tags):
        content += invisible_tag
    return content
