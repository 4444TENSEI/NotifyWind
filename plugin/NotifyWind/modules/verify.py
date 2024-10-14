# 检查配置文件的method是否在各推送服务的支持范围内
def verify_method(method, service_name, allow_method):
    if not method:
        print(f"[{service_name}] 未指定请求方法, 请检查配置文件。")
        return
    if method not in allow_method:
        supported_methods = "/".join(allow_method.keys())
        error_msg = f"\n[X {service_name}推送错误] 原因是配置中定义的 '{method}' 请求方式不被支持。\n只支持以下方法: [{supported_methods}]。\n请检查配置文件中的 'method' 值。"
        raise ValueError(error_msg)
