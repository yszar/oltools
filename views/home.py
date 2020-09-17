#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 11:44 下午
# @Author  : Tang Jiu Yang
# @Site    : https://tangjiuyang.com
# @File    : home.py
# @Software: PyCharm
from flask import render_template, Blueprint
from models import Links
from common.util import nav

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    sec_nav = nav("second")
    links = Links.query.all()
    return render_template("home/index.html", first_nav=sec_nav["first_nav"],
                           nav_index=0,
                           class_nav=sec_nav["tools_nav"],
                           class_nav_index=0,
                           tools=sec_nav["tools_info"],
                           ver_num=sec_nav["ver_num"],
                           links=links)


@home_bp.route('/article')
def article():
    top_nav_list = nav("top")
    return render_template("home/article.html",
                           first_nav=top_nav_list["first_nav"],
                           nav_index=1, ver_num=top_nav_list["ver_num"])


@home_bp.route('/software')
def software():
    top_nav_list = nav("top")
    return render_template("home/software.html",
                           first_nav=top_nav_list["first_nav"],
                           nav_index=2, ver_num=top_nav_list["first_nav"])


@home_bp.route('/website')
def website():
    top_nav_list = nav("top")
    return render_template("home/website.html",
                           first_nav=top_nav_list["first_nav"],
                           nav_index=3, ver_num=top_nav_list["first_nav"])


@home_bp.route('/about')
def about():
    top_nav_list = nav("top")
    return render_template("home/about.html",
                           first_nav=top_nav_list["first_nav"],
                           nav_index=4, ver_num=top_nav_list["first_nav"])