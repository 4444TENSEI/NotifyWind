from .service.gotify import nw_gotify
from .service.ntfy import nw_ntfy
from .service.pushplus import nw_pushplus
from .service.wechat import nw_wechat
from .modules.config import env_config
from .utils.nw_print import nw_print


# 根据配置文件存在的信息, 分别调用多个推送函数
# 启动!
def NotifyWind(message, title=None):
    nw_print(
        "[*** NotifyWind] 开始推送...",
    )
    # 载入NotifyWind推送配置
    # 遍历配置文件，读取各个结构体的配置，并逐个推送
    for service_name, service_info in env_config.items():
        if not isinstance(service_info, dict):
            continue
        config_server_url = service_info.get("server_url")
        config_priority = service_info.get("priority")
        config_token = service_info.get("token")
        try:
            if service_name == "pushplus":
                nw_pushplus(
                    message,
                    title,
                    token=config_token,
                )
            elif service_name == "ntfy":
                nw_ntfy(
                    message,
                    title,
                    server_url=config_server_url,
                    priority=config_priority,
                    token=config_token,
                )
            elif service_name == "gotify":
                nw_gotify(
                    message,
                    title,
                    server_url=config_server_url,
                    priority=config_priority,
                    token=config_token,
                )
            elif service_name == "wechat":
                nw_wechat(
                    message,
                    title,
                    server_url=config_server_url,
                )
        except Exception as e:
            nw_print(
                f"[XXX {service_name}] 推送失败, 大概率是你的推送服务信息写错 or 所填写的接口瘫了\n错误详情: {e}",
            )
