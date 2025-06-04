import requests
from ..modules.print_response import print_response

# 服务名称, 单纯用于让调试语句输出直观
service_name = "ntfy"


# 推送到ntfy
def nw_ntfy(
    server_url,
    message,
    title=None,
    priority=4,
    token=None,
):
    # 参数
    params = {"title": title, "message": message, "priority": priority}
    # 请求头
    headers = {"authorization": (f"Bearer {token}")} if token else None
    # 检查priority提醒级别数值规范
    if not isinstance(priority, int) or not (1 <= priority <= 5):
        raise ValueError(
            f"\n[X 配置错误] {service_name}配置信息/环境变量中的 'priority' 取值须为 '1-5的整数'!\n请检查json配置文件/环境变量, 否则会响应400状态码。\n数值越大级别越高, 设置为5会响铃。"
        )
    # 对于ntfy，如果使用post或者put则切换请求头为ascii_title, 请求头不允许中文, 如果包含中文, 则自动切换到默认的英文标题
    ascii_title = str(title) if all(ord(c) < 128 for c in str(title)) else "NotifyWind"
    params.update({"title": ascii_title})
    # 发出请求
    response = requests.post(
        server_url,
        params=params,
        headers=headers,
    )
    # 输出请求结果
    return print_response(service_name, server_url, response)
