# django_web

*[English](/docs/README-en.md) ∙ [简体中文](README.md)*

基于`python3.6.8`和`Django3.0`的web模板。 
 
 
## 介绍
django项目模板，主要项目架构的规范。有uwsgi，supervisor，docker-file，apt换源等脚本。包含有mqtt，定时任务，时间转换等常用库封装。app实现了基于token的users

#### app_root

`setting_diff`文件夹用于区分不同环境的配置，文件夹下的`env_specify.py`文件用于区分不同环境，`setting_base`是不同环境共有配置，其余是不同环境特有配置。已经提供了开发，测试和生产环境配置文件，可根据情况进行增减。

`django_setup.py`提供一个外挂应用的启动入口，可以使用该脚本启动一个独立于web应用的服务，可以使用django的大多数功能。

`apps`建议存放所有的application，并且建议按一张表的增删改查常见不同的application，目前已经有一个users，users实现了基于token的认证。
  
  
---
 ## 致大家🙋‍♀️🙋‍♂️
 如果本项目帮助到了你。 

🙏🙏🙏
