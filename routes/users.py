from flask import Blueprint, request
from flask_expects_json import expects_json
import controllers.auth as controller
import validations.auth as validation

bp = Blueprint('users', __name__, url_prefix="/users")


@bp.route('/signup', methods=['POST'])
@expects_json(validation.sign_up)
def sign_up():
    """
    Create a new user
    ---
    tags:
        - users
    parameters:
      - in: body
        schema:
            properties:
                firstname:
                    type: string
                lastname:
                    type: string
                email:
                    type: string
                password:
                    type: string
    responses:
        201:
            description: User created
        409:
            description: Email already used
    """
    return controller.sign_up(request.get_json())


@bp.route('/confirm-email/<token>', methods=['PUT'])
def confirm(token):
    """
    Validate user email
    ---
    tags:
        - users
    parameters:
        - in : path
          name : token
          description: Token required for validation
          required: true
          type: string
    responses:
        201:
            description: Email validated
        401:
            description: Invalid or expired token
    """
    return controller.confirm_email(token)


@bp.route('/signup/renew-validation-token', methods=['PUT'])
def renew():
    """
    Renew token
    ---
    tags:
        - users
    responses:
        205:
            description: Token renewed
        400:
            description: User not found
        409:
            description: Email user already validated
    """
    email = request.get_json()['email']

    return controller.renew_validation_token(email)
