from flask import render_template
from models import FirstNav, ToolsNav, ToolInfo, Changelog, app, Links


# app = Flask(__name__)
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


@app.route('/')
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


@app.route('/article')
def article():
    top_nav_list = nav("top")
    return render_template("home/article.html",
                           first_nav=top_nav_list["first_nav"],
                           nav_index=1, ver_num=top_nav_list["ver_num"])


@app.route('/software')
def software():
    top_nav_list = nav("top")
    return render_template("home/software.html",
                           first_nav=top_nav_list["first_nav"],
                           nav_index=2, ver_num=top_nav_list["first_nav"])


@app.route('/website')
def website():
    top_nav_list = nav("top")
    return render_template("home/website.html",
                           first_nav=top_nav_list["first_nav"],
                           nav_index=3, ver_num=top_nav_list["first_nav"])


@app.route('/about')
def about():
    top_nav_list = nav("top")
    return render_template("home/about.html",
                           first_nav=top_nav_list["first_nav"],
                           nav_index=4, ver_num=top_nav_list["first_nav"])


@app.route('/developer')
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


@app.route('/webmaster')
def webmaster():
    sec_nav = nav("second")
    return render_template("home/tools/webmaster/index.html",
                           first_nav=sec_nav["first_nav"],
                           nav_index=0,
                           class_nav=sec_nav["tools_nav"],
                           class_nav_index=2,
                           tools=sec_nav["tools_info"],
                           ver_num=sec_nav["ver_num"],
                           links=sec_nav["links"])


@app.route('/en-de-code')
def en_de_code():
    sec_nav = nav("second")
    return render_template("home/tools/en-de-code/index.html",
                           first_nav=sec_nav["first_nav"],
                           nav_index=0,
                           class_nav=sec_nav["tools_nav"],
                           class_nav_index=3,
                           tools=sec_nav["tools_info"],
                           ver_num=sec_nav["ver_num"],
                           links=sec_nav["links"])


@app.route('/video')
def video():
    sec_nav = nav("second")
    return render_template("home/tools/video/index.html",
                           first_nav=sec_nav["first_nav"],
                           nav_index=0,
                           class_nav=sec_nav["tools_nav"],
                           class_nav_index=4,
                           tools=sec_nav["tools_info"],
                           ver_num=sec_nav["ver_num"],
                           links=sec_nav["links"])


@app.route('/other')
def other():
    sec_nav = nav("second")
    return render_template("home/tools/other/index.html",
                           first_nav=sec_nav["first_nav"],
                           nav_index=0,
                           class_nav=sec_nav["tools_nav"],
                           class_nav_index=5,
                           tools=sec_nav["tools_info"],
                           ver_num=sec_nav["ver_num"],
                           links=sec_nav["links"])


if __name__ == '__main__':
    app.run(debug=True)
