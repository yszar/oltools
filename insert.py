#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 10:08 上午
# @Author  : Tang Jiu Yang
# @Site    : https://tangjiuyang.com
# @File    : insert.py
# @Software: PyCharm
from flask import Flask

from models import FirstNav, ToolsNav, ToolInfo
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

first_nav1 = FirstNav(name="在线工具", url="/")
first_nav2 = FirstNav(name="心得技巧", url="article")
first_nav3 = FirstNav(name="软件推荐", url="software")
first_nav4 = FirstNav(name="网址推荐", url="website")
first_nav5 = FirstNav(name="关于本站", url="about")

db.session.add_all([first_nav1, first_nav2, first_nav3, first_nav4, first_nav5])
db.session.commit()

tools_nav1 = ToolsNav(name="开发工具", url="developer")
tools_nav2 = ToolsNav(name="站长工具", url="webmaster")
tools_nav3 = ToolsNav(name="加密解密", url="en-de-code")
tools_nav4 = ToolsNav(name="短视频类", url="video")
tools_nav5 = ToolsNav(name="其他", url="other")

db.session.add_all([tools_nav1, tools_nav2, tools_nav3, tools_nav4, tools_nav5])
db.session.commit()

tool_info1 = ToolInfo(pid=1, name="我是工具一", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info2 = ToolInfo(pid=1, name="我是工具二", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info3 = ToolInfo(pid=2, name="我是工具三", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info4 = ToolInfo(pid=2, name="我是工具4", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info5 = ToolInfo(pid=4, name="我是工具5", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info6 = ToolInfo(pid=4, name="我是工具6", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info7 = ToolInfo(pid=3, name="我是工具7", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info8 = ToolInfo(pid=5, name="我是工具8", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info9 = ToolInfo(pid=5, name="我是工具9", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                      image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                      tool_url="/ttt1")
tool_info10 = ToolInfo(pid=2, name="我是工具十", desc="我是简介紫薯布丁紫薯布丁紫薯布丁.",
                       image_url="https://cdn.tangjiuyang.com/other/icons8-tool-img-48.png",
                       tool_url="/ttt1")
db.session.add_all([tool_info1, tool_info2, tool_info3, tool_info4, tool_info5,
                    tool_info6, tool_info7, tool_info8, tool_info9,
                    tool_info10])
db.session.commit()


