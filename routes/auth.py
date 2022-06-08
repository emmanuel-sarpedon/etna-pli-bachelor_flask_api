from flask import Blueprint, request
from flask_expects_json import expects_json
import controllers.auth as controller
import validations.auth as validation

bp = Blueprint('auth', __name__, url_prefix="/auth")


@bp.route('/signup', methods=['POST'])
@expects_json(validation.sign_up)
def sign_up():
    return controller.sign_up(request.get_json())


@bp.route('/confirm/<token>', methods=['GET'])
def index(token):
    return controller.confirm_email(token)

