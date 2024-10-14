import json


# 根据debug布尔值显示和隐藏输出
def debug_msg(debug, message):
    if debug:
        print(message)


# 推送前输出
def log_print(service_name, method, push_url, message, debug=None):
    method = method.upper()
    debug_msg(debug, f"\n[{method}/{service_name}] 推送至: {push_url}\n{message}")


# 推送后输出, 根据响应头状态码判断是否推送成功, 注意pushplus的状态码应该从response.text取code而不是从响应头
def log_response(service_name, method, push_url, response, debug=None):
    if service_name == "pushplus":
        response_data = json.loads(response.text)
        pushplus_respond_code = response_data.get("code")
        if pushplus_respond_code == 200:
            log_message = (
                f"[√ {service_name}-推送成功({pushplus_respond_code})]: {response_data}"
            )
        else:
            log_message = (
                f"[X {service_name}-推送失败({pushplus_respond_code})]: {response_data}"
            )
    else:
        respond_code = response.status_code
        respond_message = response.text
        if respond_code == 200:
            log_message = (
                f"[√ {service_name}-推送成功({respond_code})]: {respond_message}"
            )
        else:
            log_message = (
                f"[X {service_name}-推送失败({respond_code})]: {respond_message}"
            )
    log_print(service_name, method, push_url, log_message, debug)
