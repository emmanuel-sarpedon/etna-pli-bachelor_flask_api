from flask import Blueprint, request
from flask_expects_json import expects_json
import controllers.auth as controller
import validations.auth as validation

bp = Blueprint('auth', __name__, url_prefix="/auth")


@bp.route('/signup', methods=['POST'])
@expects_json(validation.sign_up)
def sign_up():
    """
    User registration
    ---
    tags:
        - auth
    parameters:
      - in: body
        name: body
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
    User email confirmation
    ---
    tags:
        - auth
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
    Token renewal
    ---
    tags:
        - auth
    parameters:
      - in: body
        name: body
        schema:
            properties:
                email:
                    type: string
    responses:
        205:
            description: Token renewed
        400:
            description: User not found
        409:
            description: User email already validated
    """
    email = request.get_json()['email']

    return controller.renew_validation_token(email)


@bp.route('/login', methods=['POST'])
def log_in():
    """
    User login
    ---
    tags:
        - auth
    parameters:
      - in: body
        name: body
        schema:
            properties:
                email:
                    type: string
                password:
                    type: string
    responses:
        200:
            description: Successful connection
        401:
            description: Bad credentials
    """
    return controller.log_in(request.get_json())
