from flask_restful import Api
from flask import Blueprint
from app.auth.controllers.login import LoginView
from app.auth.controllers.signup import SignUpView

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
api=Api(auth_blueprint)

from flask import Blueprint




api.add_resource(LoginView,"/login/")
api.add_resource(SignUpView,"/signup/")
