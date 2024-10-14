from .service.gotify import nw_gotify
from .service.ntfy import nw_ntfy
from .service.pushplus import nw_pushplus
from .config.loader import config_loader
from .modules.log import debug_msg
import threading


# 根据配置文件存在的信息, 分别调用多个推送函数
def nw_start(service_name, service_info, title, message, debug=None):
    try:
        if service_name == "pushplus":
            nw_pushplus(
                message=message,
                title=title,
                server_url=service_info.get(
                    "server_url", "https://www.pushplus.plus/send"
                ),
                token=service_info.get("token"),
                method=service_info.get("method", "get"),
                debug=debug,
            )
        elif service_name == "ntfy":
            nw_ntfy(
                message=message,
                title=title,
                server_url=service_info.get("server_url"),
                priority=service_info.get("priority", 4),
                method=service_info.get("method", "get"),
                token=service_info.get("token"),
                debug=debug,
            )
        elif service_name == "gotify":
            nw_gotify(
                message=message,
                title=title,
                server_url=service_info.get("server_url"),
                priority=service_info.get("priority", 8),
                method=service_info.get("method", "post"),
                token=service_info.get("token"),
                debug=debug,
            )
    except Exception as e:
        debug_msg(
            debug,
            f"\n[X {service_name} 推送失败, 大概率是你的配置信息写错了or服务器瘫了]\n{e}",
        )


# 启动(多线程)!
def NotifyWind(title, message, config_path="notifywind.json", debug=True):
    config = config_loader(config_path, debug)
    if config is None:
        return
    threads = []
    try:
        for service_name, service_info in config["NotifyWind"].items():
            thread = threading.Thread(
                target=nw_start,
                args=(service_name, service_info, title, message, debug),
            )
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    except KeyError:
        debug_msg(
            debug, "[X 配置信息错误] 配置文件中需要一个 'NotifyWind' 作为顶级键。"
        )

    debug_msg(
        debug,
        "\n----------------------\n[NotifyWind] 运行完毕! \n----------------------",
    )
