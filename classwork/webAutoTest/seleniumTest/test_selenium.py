'''

1.安装
官网：https://www.selenium.dev/
前提 python  、 pip环境
安装插件：pip install selenium    或者pycharm 插件安装配置
下载drive：驱动，谷歌或者火狐等浏览器
解压后，配置环境变量
重启pycharm 以及cmd，执行命令chromedriver 如下则安装成功


2.selenium IDE用例录制


'''

import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")