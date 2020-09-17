#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 11:56 上午
# @Author  : Tang Jiu Yang
# @Site    : https://tangjiuyang.com
# @File    : developer.py
# @Software: PyCharm
from flask import render_template, Blueprint, request
from common.util import nav
from models import ToolInfo

search_bp = Blueprint('search', __name__)


@search_bp.route('/search', methods=['post', 'get'])
def search():
    keyword = request.args.get('query')
    sec_nav = nav("second")
    search_res = ToolInfo.query.filter(ToolInfo.desc.like('%' + keyword + '%'))
    return render_template("home/search.html",
                           first_nav=sec_nav["first_nav"],
                           nav_index=0,
                           search_res=search_res)
