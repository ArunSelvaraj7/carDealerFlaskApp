import os
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



db=SQLAlchemy()
bootstrap=Bootstrap()
login_manager=LoginManager()
login_manager.login_view='auth.do_the_login'
login_manager.login_message="Welcome!"
bcrypt=Bcrypt()



def create_app(config_type):
    app=Flask(__name__)
    configuration=os.path.join(os.getcwd(),'config',config_type+'.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    

    from bike.garage import main
    app.register_blueprint(main)

    from bike.auth import auth
    app.register_blueprint(auth)
    return app