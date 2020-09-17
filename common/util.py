#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 11:52 下午
# @Author  : Tang Jiu Yang
# @Site    : https://tangjiuyang.com
# @File    : util.py
# @Software: PyCharm
from models import FirstNav, ToolsNav, ToolInfo, Changelog, app, Links


def nav(param):
    """

    :param param:
    :return:
    """
    first_nav = FirstNav.query.all()
    latest_log = Changelog.query.order_by(Changelog.id.desc()).first()
    ver_num = latest_log.ver_num
    first_nav[0].url = ""
    if param == "top":
        return {"first_nav": first_nav, "ver_num": ver_num}
    if param == "second":
        tools_nav = ToolsNav.query.all()
        tools_info = ToolInfo.query.all()
        links = Links.query.all()
        return {"first_nav": first_nav, "ver_num": ver_num,
                "tools_nav": tools_nav, "tools_info": tools_info,
                "links": links}
