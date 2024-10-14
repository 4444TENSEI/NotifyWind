import requests, random
from ..modules.log import log_response
from ..modules.verify import verify_method

# 服务名称, 单纯用于让调试语句输出直观
service_name = "pushplus"


# 推送到pushplus
def nw_pushplus(
    message,
    title=None,
    token=None,
    server_url=None,
    method=None,
    debug=None,
):
    # 这里是为了单独调用
    server_url = server_url or "https://www.pushplus.plus/send"
    params = {
        "token": token,
        "title": title,
        "content": insert_invisible_tags(message),
        "template": "html",
    }
    # 可有可无的请求头, 看心情
    headers = {"Content-Type": "application/json"}
    # 不同method使用不同请求函数, 顺便检查配置里的方法是否正确
    allow_method = {"get": _pushplus_get, "post": _pushplus_post, "put": _pushplus_put}
    # 检查method是否合规
    verify_method(method.lower(), service_name, allow_method)
    return allow_method[method.lower()](params, server_url, method, headers, debug)


# GET方法, 三种方法都一个形式请求同一个地址, token带着消息一起放到url里的params, 请求头无所谓
def _pushplus_get(params, server_url, method, headers=None, debug=None):
    response = requests.get(
        server_url,
        params=params,
        headers=headers,
    )
    return log_response(service_name, method, server_url, response, debug)


# POST方法, 三种方法都一个形式请求同一个地址, token带着消息一起放到请求体params拼接到url, 请求头无所谓
def _pushplus_post(params, server_url, method, headers=None, debug=None):
    response = requests.post(
        server_url,
        params=params,
        headers=headers,
    )
    return log_response(service_name, method, server_url, response, debug)


# PUT方法, 三种方法都一个形式请求同一个地址, token带着消息一起放到请求体params拼接到url, 请求头无所谓
def _pushplus_put(params, server_url, method, headers=None, debug=None):
    response = requests.put(
        server_url,
        params=params,
        headers=headers,
    )
    return log_response(service_name, method, server_url, response, debug)


# 由于pushplus会对于重复消息做频繁限制, 咱直接随机生成随机的不可见HTML标签, 每次推送时加入, 防止被检测到频繁发送消息导致的999状态码
def insert_invisible_tags(content):
    invisible_tag = '<span style="display:none;"/>'
    # 随机插入1到30个
    num_tags = random.randint(1, 30)
    for _ in range(num_tags):
        content += invisible_tag
    return content
