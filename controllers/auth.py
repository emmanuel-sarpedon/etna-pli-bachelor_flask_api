import services.auth as service


def sign_up(request):
    firstname = request["firstname"]
    lastname = request["lastname"]
    email = request["email"]
    password = request["password"]

    if service.is_user_already_registered(email):
        return service.throw_error_user_already_exists(), 403

    confirmation_token = service.generate_confirmation_token(email)
    service.send_confirmation_code(email, confirmation_token)

    return service.register_new_user(firstname, lastname, email, password, confirmation_token), 201
