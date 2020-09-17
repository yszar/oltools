#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 11:56 上午
# @Author  : Tang Jiu Yang
# @Site    : https://tangjiuyang.com
# @File    : developer.py
# @Software: PyCharm
from flask import render_template, Blueprint
from common.util import nav

developer_bp = Blueprint('developer', __name__)


@developer_bp.route('/developer')
def developer():
    sec_nav = nav("second")
    return render_template("home/tools/developer/index.html",
                           first_nav=sec_nav["first_nav"],
                           nav_index=0,
                           class_nav=sec_nav["tools_nav"],
                           class_nav_index=1,
                           tools=sec_nav["tools_info"],
                           ver_num=sec_nav["ver_num"],
                           links=sec_nav["links"])
