#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 8:21 下午
# @Author  : Tang Jiu Yang
# @Site    : https://tangjiuyang.com
# @File    : models.py
# @Software: PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)
# app.config[
#     "SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class FirstNav(db.Model):
    """
    一级导航分类表：
    0.编号
    1.分类名称
    2.分类地址
    """
    __tablename__ = "first_nav"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(20), nullable=False)  # 分类名称
    url = db.Column(db.String(20), nullable=False)  # 分类url

    # tools_nav = db.relationship('ToolsNav', backref='first_nav')  # 工具分类外键关系关联

    def __repr__(self):
        return "<FirstNav %r>" % self.name


class ToolsNav(db.Model):
    """
    工具导航分类表：
    0.编号
    1.工具分类名称
    2.工具分类地址
    """
    __tablename__ = "tools_nav"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(20), nullable=False)  # 工具分类名称
    first_id = db.Column(db.Integer, db.ForeignKey('first_nav.id'),
                         default=1, nullable=False)
    url = db.Column(db.String(20), nullable=False)  # 工具分类url
    first_nav = db.relationship('FirstNav', backref='tools_nav')  # 工具详情外键关系关联

    def __repr__(self):
        return "<ToolsNav %r>" % self.name


class ToolInfo(db.Model):
    """
    工具详情表：
    0.编号
    1.工具分类父id
    2.工具名称
    3.工具简介
    4.工具图标url
    5.工具分类url
    6.工具url
    """
    __tablename__ = "tool_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pid = db.Column(db.Integer, db.ForeignKey('tools_nav.id'))  # 父id
    name = db.Column(db.String(20), nullable=False)  # 工具名称
    desc = db.Column(db.String(200), nullable=False)  # 工具简介
    image_url = db.Column(db.String(100), nullable=False)  # 工具图标url
    # p_name = db.Column(db.String(20), db.ForeignKey('tools_nav.id'))
    tool_url = db.Column(db.String(20), nullable=False)  # 工具url
    class_url = db.relationship('ToolsNav', backref='tool_info')

    def __repr__(self):
        return "<ToolInfo %r>" % self.name


class Changelog(db.Model):
    """
    更新日志表：
    0.编号
    1.版本号
    2.更新日期
    3.更新内容
    """
    __tablename__ = "changelog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ver_num = db.Column(db.String(20), nullable=False)  # 版本号
    date = db.Column(db.String(20), nullable=False)  # 更新日期
    changelog = db.Column(db.String(200), nullable=False)  # 内容

    def __repr__(self):
        return "<Changelog %r>" % self.name


class Links(db.Model):
    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(20), nullable=False)  # 分类名称
    url = db.Column(db.String(100), nullable=False)  # 分类url

    def __repr__(self):
        return "<Links %r>" % self.name

# class SiteInfo(db.Model):
#     """
#     一级导航分类表：
#     0.编号
#     1.分类名称
#     2.分类地址
#     """
#     __tablename__ = "first_nav"
#     id = db.Column(db.Integer, primary_key=True)  # 编号
#     name = db.Column(db.String(20), nullable=False)  # 分类名称
#     url = db.Column(db.String(20), nullable=False)  # 分类url
#     tools_nav = db.relationship('tools_nav', backref='first_nav')  # 工具分类外键关系关联
#
#     def __repr__(self):
#         return "<FirstNav %r>" % self.name
