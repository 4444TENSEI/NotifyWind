import requests
from ..modules.log import log_response
from ..modules.verify import verify_method

# 服务名称, 单纯用于让调试语句输出直观
service_name = "gotify"


# 推送到gotify
def nw_gotify(
    message,
    title=None,
    priority=None,
    token=None,
    server_url=None,
    method=None,
    debug=None,
):
    params = {"token": token if token else None}
    data = {"title": title, "message": message, "priority": priority}
    # 不同method使用不同请求函数, 顺便检查配置里的方法是否正确
    allow_method = {"post": _gotify_post}
    verify_method(method.lower(), service_name, allow_method)
    # 检查priority提醒级别数值规范
    if not isinstance(priority, int):
        raise ValueError(
            f"\n[X 配置错误] {service_name}配置信息/环境变量中的 'priority' 取值须为整数！\n范围 priority<=0: 无通知, 需要手动查看\n范围 1<=priority<=4: 无弹窗, 但是在通知栏里有信息\n范围 5<=priority<=7: 虽然是官方分级, 但是依然和上面一样, 没有弹窗\n范围 8<=priority: 没有范围限定, 可以是无限大, 反正设为8就有弹窗通知"
        )

    return allow_method[method.lower()](params, server_url, method, data, debug)


# POST方法, token在请求头Authorization中, message信息在url中作为参数拼接
def _gotify_post(params, server_url, method, data=None, debug=None):
    gotify_post_url = f"{server_url}/message"
    response = requests.post(
        gotify_post_url,
        params=params,
        data=data,
    )
    return log_response(service_name, method, gotify_post_url, response, debug)
