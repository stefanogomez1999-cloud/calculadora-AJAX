import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import jscode
    app.register_blueprint(jscode.bp)


    @app.route("/")
    def index():
        return render_template("home/index.html")
    
    return app