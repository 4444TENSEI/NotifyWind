import json
from ..utils.nw_print import nw_print


def print_response(service_name, push_url, response):
    # 由于部分服务的接口实际处理结果的状态码在响应体中，所以对此分别处理错误判断
    code_from_content = {
        "pushplus": {"code_key": "code", "success_code": 200},
        "wechat": {"code_key": "errcode", "success_code": 0},
    }
    special_handler = code_from_content.get(service_name)
    # 真实响应头状态码
    header_code = response.status_code
    # 默认的成功判断状态码
    success_code = 200
    response_content = response.text
    # 特殊服务处理逻辑
    if special_handler:
        try:
            response_data = response.json()
            # 从 JSON 中提取业务状态码和成功码，键不存在时默认为 None
            header_code = response_data.get(special_handler["code_key"], None)
            success_code = special_handler["success_code"]
            # 替换为结构化数据便于日志展示
            response_content = response_data
        except json.JSONDecodeError:
            header_code = None  # 强制后续判断失败
    # 统一状态判断逻辑
    success = (
        (header_code == success_code)
        if special_handler
        else (response.status_code == 200)
    )
    # 构造日志输出
    status_symbol = "√√√" if success else "XXX"
    status_text = "成功" if success else "失败"
    nw_print(
        f"\n[>>> {service_name}-开始推送] 接口: {push_url}\n[<<< {service_name}-接口响应]: {response_content}\n[{status_symbol} {service_name}-推送结果]: {status_text} (状态码: {header_code or response.status_code})"
    )
