import services.auth as service


def sign_up(request):
    username = request["username"]
    email = request["email"]
    password = request["password"]

    if service.is_user_already_registered(username, email):
        return service.throw_error_user_already_exists(), 403

    return service.register_new_user(username, email, password), 201
