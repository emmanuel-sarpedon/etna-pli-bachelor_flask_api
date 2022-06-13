import services.auth as service
from utils.errors import Auth
from itsdangerous import BadTimeSignature, SignatureExpired
from werkzeug.security import check_password_hash


def sign_up(request):
    """
    "If the user is already registered, throw an error, otherwise generate a confirmation token,
    send the confirmation code, and register the new user."

    :param request: The request object that contains the data sent by the client
    :return: A tuple of the user object and a 201 status code.
    """
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
    """
    It takes a token, checks if it's valid, and if it is, it returns a success message

    :param token: The token that was sent to the user's email
    :return: The email address of the user.
    """
    try:
        email = service.check_confirmation_token(token)
        return service.validate_account_email(email), 201

    except (BadTimeSignature, SignatureExpired):
        return Auth.throw_error_token_is_denied()


def renew_validation_token(email):
    """
    It generates a new token and sends it to the user

    :param email: The email of the user to renew the validation token for
    :return: A message and a 205 status code.
    """
    user = service.get_user_by_email(email)

    if not user:
        return Auth.throw_error_ressource_not_found()

    if user.is_email_validated:
        return Auth.throw_error_email_already_validated()

    new_token = service.generate_confirmation_token(user.email)

    user.confirmation_token = new_token
    service.send_confirmation_code(email, new_token)
    service.update_user_on_database(user),

    return {'message': 'Token renewed'}, 205


def log_in(request):
    """
    It takes an email and password from the request, checks if the user exists and if the password is correct, and if so,
    returns a token

    :param request: The request object that contains the email and password
    :return: The user's email and a 200 status code.
    """
    email = request['email']
    password = request['password']

    user = service.get_user_by_email(email)

    if not user or not check_password_hash(user.password, password):
        return Auth.throw_error_bad_credentials()

    return service.log_in(user.email), 200
