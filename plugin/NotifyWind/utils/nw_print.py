from ..modules.config import env_config

# 控制台调试语句开关
debug_enable = env_config.get("debug")


def nw_print(msg):
    if debug_enable:
        print(msg)
    else:
        pass
