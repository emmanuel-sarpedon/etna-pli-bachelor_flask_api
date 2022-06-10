import services.auth as service
from utils.errors import User
from itsdangerous import BadTimeSignature, SignatureExpired


def sign_up(request):
    firstname = request["firstname"]
    lastname = request["lastname"]
    email = request["email"]
    password = request["password"]

    if service.is_user_already_registered(email):
        return User.throw_error_user_already_exists(), 409

    confirmation_token = service.generate_confirmation_token(email)

    service.send_confirmation_code(email, confirmation_token)

    return service.register_new_user(firstname, lastname, email, password, confirmation_token), 201


def confirm_email(token):
    try:
        email = service.check_confirmation_token(token)
        return service.validate_account_email(email), 201

    except (BadTimeSignature, SignatureExpired):
        return User.throw_error_token_is_denied(), 401


def renew_validation_token(email):
    user = service.get_user_by_email(email)

    if not user:
        return User.throw_error_ressource_not_found(), 400

    if user.is_email_validated:
        return User.throw_error_email_already_validated(), 409

    new_token = service.generate_confirmation_token(user.email)

    user.confirmation_token = new_token
    service.send_confirmation_code(email, new_token)
    service.update_user_on_database(user),

    return {}, 205
