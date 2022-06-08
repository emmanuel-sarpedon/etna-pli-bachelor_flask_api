import services.auth as service


def sign_up(request):
    firstname = request["firstname"]
    lastname = request["lastname"]
    email = request["email"]
    password = request["password"]

    if service.is_user_already_registered(email):
        return service.throw_error_user_already_exists(), 403

    return service.register_new_user(firstname, lastname, email, password), 201
