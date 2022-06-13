import services.auth as service
from utils.errors import Auth
from itsdangerous import BadTimeSignature, SignatureExpired
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import config


def sign_up(request):
    firstname = request["firstname"]
    lastname = request["lastname"]
    email = request["email"]
    password = request["password"]

    if service.is_user_already_registered(email):
        return Auth.throw_error_user_already_exists()

    confirmation_token = service.generate_confirmation_token(email)

    service.send_confirmation_code(email, confirmation_token)

    return service.register_new_user(firstname, lastname, email, password, confirmation_token), 201


def confirm_email(token):
    try:
        email = service.check_confirmation_token(token)
        return service.validate_account_email(email), 201

    except (BadTimeSignature, SignatureExpired):
        return Auth.throw_error_token_is_denied()


def renew_validation_token(email):
    user = service.get_user_by_email(email)

    if not user:
        return Auth.throw_error_ressource_not_found()

    if user.is_email_validated:
        return Auth.throw_error_email_already_validated()

    new_token = service.generate_confirmation_token(user.email)

    user.confirmation_token = new_token
    service.send_confirmation_code(email, new_token)
    service.update_user_on_database(user),

    return {}, 205


def log_in(request):
    email = request['email']
    password = request['password']

    user = service.get_user_by_email(email)

    if not user or not check_password_hash(user.password, password):
        return Auth.throw_error_bad_credentials()

    return service.log_in(user.email), 200
