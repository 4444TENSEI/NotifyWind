import requests
from ..modules.log import log_response
from ..modules.verify import verify_method

# 服务名称, 单纯用于让调试语句输出直观
service_name = "ntfy"


# 推送到ntfy
def nw_ntfy(
    message,
    title=None,
    priority=None,
    tags=None,
    token=None,
    server_url=None,
    method=None,
    debug=None,
):
    # 默认带个🐱标签
    tags = tags or "smiley_cat"
    params = {"title": title, "message": message, "priority": priority}
    headers = {
        "authorization": (f"Bearer {token}" if token else None),
        "tags": tags,
    }
    # 不同method使用不同请求函数, 顺便检查配置里的方法是否正确
    allow_method = {"get": _ntfy_get, "post": _ntfy_post, "put": _ntfy_put}
    verify_method(method.lower(), service_name, allow_method)
    # 检查priority提醒级别数值规范
    if not isinstance(priority, int) or not (1 <= priority <= 5):
        raise ValueError(
            f"\n[X 配置错误] {service_name}配置信息/环境变量中的 'priority' 取值须为 '1-5的整数'!\n请检查json配置文件/环境变量, 否则会响应400状态码。\n数值越大级别越高, 设置为5会响铃。"
        )
    # 如果是post或者put则切换请求头为ascii_title, 请求头不允许中文, 如果包含中文, 则自动切换到默认的英文标题
    if method in ["post", "put"]:
        ascii_title = (
            str(title) if all(ord(c) < 128 for c in str(title)) else "NotifyWind"
        )
        params.update({"title": ascii_title})
    return allow_method[method.lower()](params, server_url, method, headers, debug)


# GET方法, token在请求头Authorization中, message信息在url中作为参数拼接
def _ntfy_get(params, server_url, method, headers=None, debug=None):
    ntfy_get_url = f"{server_url}/send"
    response = requests.get(
        ntfy_get_url,
        params=params,
        headers=headers,
    )
    return log_response(service_name, method, ntfy_get_url, response, debug)


# POST方法, token在请求头Authorization中, message信息在url中作为参数拼接
def _ntfy_post(params, server_url, method, headers=None, debug=None):
    response = requests.post(
        server_url,
        params=params,
        headers=headers,
    )
    return log_response(service_name, method, server_url, response, debug)


# PUT方法, token在请求头Authorization中, message信息在url中作为参数拼接
def _ntfy_put(params, server_url, method, headers=None, debug=None):
    response = requests.put(
        server_url,
        params=params,
        headers=headers,
    )
    return log_response(service_name, method, server_url, response, debug)
