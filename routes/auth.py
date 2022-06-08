from flask import Blueprint, request
from flask_expects_json import expects_json
from flask_mail import Message, Mail
import controllers.auth as controller
import validations.auth as validation

bp = Blueprint('auth', __name__, url_prefix="/auth")


@bp.route('/signup', methods=['POST'])
@expects_json(validation.sign_up)
def sign_up():
    return controller.sign_up(request.get_json())
