import json, os


# 本地配置文件路径（相对于项目根目录）
config_path = "./config.NotifyWind.json"
# 环境变量名称
config_sys_name = "NOTIFYWIND_CONFIG"


# 载入配置, 优先级为1.环境变量2.配置文件
def init_config():
    config_sys = os.getenv(config_sys_name)
    if config_sys:
        try:
            config_data = json.loads(config_sys)
            print(
                f"[√√√ NotifyWind] 配置载入成功，环境变量配置载入成功: {config_data}\n"
            )
            return config_data
        except json.JSONDecodeError as e:
            raise ValueError(
                f"[XXX NotifyWind] 配置载入失败，系统环境变量 '{config_sys_name}' 内容非标准JSON格式：{e}\n"
            )
    else:
        # 如果环境变量没有配置，尝试从本地文件载入配置
        print(
            f"[### NotifyWind] 未找到系统环境变量 '{config_sys_name}'，正在尝试载入本地配置文件...",
        )
        try:
            with open(config_path, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)
                print(f"[√√√ NotifyWind] 配置载入成功，当前已成功载入本地文件配置!\n")
                return config_data
        except FileNotFoundError:
            raise ValueError(
                f"[XXX NotifyWind] 配置载入失败，本地配置文件 '{config_path}' 未找到, 请检查文件是否存在。\n如需更改默认配置文件路径请全局搜索 '本地配置文件路径', 或是直接为NotifyWind额外传递一个config_path参数。",
            )
        except json.JSONDecodeError as e:
            raise ValueError(
                f"[XXX NotifyWind] 配置载入失败，本地配置文件 '{config_path}' 内容非标准JSON格式：{e}\n"
            )


# 初始化配置
env_config = init_config()
