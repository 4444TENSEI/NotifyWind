import json, os
from ..modules.log import debug_msg

# 环境变量名称
config_sys_name = "NOTIFYWIND"


# 载入配置, 优先级为1.环境变量2.配置文件
def config_loader(config_path=None, debug=None):
    config_sys = os.getenv(config_sys_name)
    debug_msg(
        debug,
        "\n------------------------\n[NotifyWind] 开始运行... \n------------------------\n",
    )
    if config_sys:
        try:
            config_data = json.loads(config_sys)
            debug_msg(
                debug, f"[√ 系统环境变量载入成功] 环境变量配置载入成功: {config_data}"
            )
            return config_data
        except json.JSONDecodeError as e:
            debug_msg(
                debug,
                f"[X 环境变量载入错误] 名为 '{config_sys_name}' 的环境变量未找到, 或是内部JSON数据无法解析: {e}",
            )
            return None
    else:
        debug_msg(
            debug,
            f"[提示] 系统环境变量 '{config_sys_name}' 未找到，尝试从本地配置文件载入配置, 本地测试环境可以无视这条输出。\n",
        )
    # 如果环境变量没有配置，尝试从本地文件载入配置
    try:
        with open(config_path, "r", encoding="utf-8") as config_file:
            config_data = json.load(config_file)
            debug_msg(debug, f"[√ 配置载入成功] 本地配置文件载入成功:\n{config_data}")
            return config_data
    except FileNotFoundError:
        debug_msg(
            debug,
            f"[X 配置载入错误] 本地配置文件 '{config_path}' 未找到, 请检查文件是否存在。\n如需更改默认配置文件路径请全局搜索 'config_path=', 或是直接为NotifyWind额外传递一个config_path参数。",
        )
    except json.JSONDecodeError as e:
        debug_msg(
            debug,
            f"[X 配置载入错误] 本地配置文件'{config_path}'包含的JSON数据无法解析: {e}",
        )
    return None
