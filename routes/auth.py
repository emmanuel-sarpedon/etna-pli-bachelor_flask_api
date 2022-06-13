from flask import Blueprint, request
from flask_expects_json import expects_json
import controllers.auth as controller
import validations.auth as validation

bp = Blueprint('auth', __name__, url_prefix="/auth")


@bp.route('/registration', methods=['POST'])
@expects_json(validation.sign_up)
def sign_up():
    """
    User registration
    ---
    tags:
        - Authentication
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
            schema:
                type: object
                example: {
                            'message': 'User created',
                            'user_created': {
                                '_id': 164,
                                'firstname': "John",
                                'lastnamed': "DOE",
                                'email': "john.doe@etna.io"
                            }
                }
        409:
            description: Email already used
            schema:
                type: object
                example: {"error": {"message": "User already exists"}}
    """
    return controller.sign_up(request.get_json())


@bp.route('/email-confirmation', methods=['PUT'])
def confirm(token):
    """
    User email confirmation
    ---
    tags:
        - Authentication
    parameters:
        - in : body
          name: body
          description: Token required for validation
          schema:
            properties:
                token:
                    type: string
    responses:
        201:
            description: Email validated
            schema:
                type: object
                example: {"message": "email validated"}
        401:
            description: Invalid or expired token
            schema:
                type: object
                example: {"error": {"message": "Invalid or expired token"}}
    """
    return controller.confirm_email(token)


@bp.route('/token-renewal', methods=['PUT'])
def renew():
    """
    Token renewal
    ---
    tags:
        - Authentication
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
            schema:
                type: object
                example: {'message': 'Token renewed'}

        400:
            description: User not found
            schema:
                type: object
                example: {"error": {"message": "Not found"}}
        409:
            description: User email already validated
            schema:
                type: object
                example: {"error": {"message": "Email already validated"}}
    """
    email = request.get_json()['email']

    return controller.renew_validation_token(email)


@bp.route('/login', methods=['POST'])
def log_in():
    """
    User login
    ---
    tags:
        - Authentication
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
            schema:
                type: object
                example: {
                    "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1N[...]VaM4-mIwwlNqI8stxoIxdQLEz_HC7vZkbuOdxfu0"
                }
        401:
            description: Bad credentials
            schema:
                type: object
                example: {
                    "error": {"message": "Bad credentials"}
                }
    """
    return controller.log_in(request.get_json())
