from flask import Blueprint, request
from flask_expects_json import expects_json
import controllers.auth as controller
import validations.auth as validation

bp = Blueprint('users', __name__, url_prefix="/users")


@bp.route('/signup', methods=['POST'])
@expects_json(validation.sign_up)
def sign_up():
    return controller.sign_up(request.get_json())


@bp.route('/confirm-email/<token>', methods=['GET'])
def confirm(token):
    return controller.confirm_email(token)


@bp.route('/signup/renew-validation-token', methods=['PUT'])
def renew():
    email = request.get_json()['email']

    return controller.renew_validation_token(email)
