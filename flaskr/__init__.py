import os
from flask import Flask
from . import db
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown


flaskr_root  = '/Users/liaoshousan/Desktop/Github/Serendipity/flaskr'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    PageDown(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(flaskr_root, 'db.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)   
    
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
