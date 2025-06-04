import requests
from ..modules.print_response import print_response

# 服务名称, 单纯用于让调试语句输出直观
service_name = "Gotify"


# 推送到gotify
def nw_gotify(
    server_url,
    message,
    title=None,
    priority=8,
    token=None,
):
    # 参数
    params = {"token": token}
    # 请求体
    data = {"title": title, "message": message, "priority": priority}
    # 检查priority提醒级别数值规范
    if not isinstance(priority, int):
        raise ValueError(
            f"\n[X 配置错误] {service_name}配置信息/环境变量中的 'priority' 取值须为整数！\n范围 priority<=0: 无通知, 需要手动查看\n范围 1<=priority<=4: 无弹窗, 但是在通知栏里有信息\n范围 5<=priority<=7: 虽然是官方分级, 但是依然和上面一样, 没有弹窗\n范围 8<=priority: 没有范围限定, 可以是无限大, 反正设为8就有弹窗通知"
        )
    # 发出请求
    response = requests.post(
        server_url,
        params=params,
        data=data,
    )
    # 输出请求结果
    return print_response(service_name, server_url, response)
