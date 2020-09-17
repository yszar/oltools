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

tool_info1 = ToolInfo(pid=1, name="短视频去水印", desc="短视频完美去水印.",
                      image_url="https://cdn.oltools.net/img%E7%9F%AD%E8%A7%86%E9%A2%91%E5%89%AA%E8%BE%91.png",
                      tool_url="short-video")

db.session.add_all([tool_info1])
db.session.commit()


