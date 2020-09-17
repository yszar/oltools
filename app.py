from flask import render_template
from models import app, Links
from common.util import nav
from views.home import home_bp
from views.developer import developer_bp
from views.webmaster import webmaster_bp
from views.en_de_code import en_de_code_bp
from views.video import video_bp
from views.other import other_bp
from views.search import search_bp

app.register_blueprint(home_bp)
app.register_blueprint(developer_bp)
app.register_blueprint(webmaster_bp)
app.register_blueprint(en_de_code_bp)
app.register_blueprint(video_bp)
app.register_blueprint(other_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)
