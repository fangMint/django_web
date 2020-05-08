from .setting_diff.env_specify import *

if get_env == "dev":
    from .setting_diff.setting_dev import *
elif get_env == "test":
    from .setting_diff.setting_test import *
elif get_env == "prod":
    from .setting_diff.setting_prod import *
