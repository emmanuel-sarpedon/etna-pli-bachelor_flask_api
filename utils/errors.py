class Auth:
    @staticmethod
    def throw_error_ressource_not_found():
        return {"error": {"message": "Not found"}}, 400

    @staticmethod
    def throw_error_email_already_validated():
        return {"error": {"message": "Email already validated"}}, 409

    @staticmethod
    def throw_error_user_already_exists():
        return {"error": {"message": "User already exists"}}, 409

    @staticmethod
    def throw_error_token_is_denied():
        return {"error": {"message": "Invalid or expired token"}}, 401

    @staticmethod
    def throw_error_bad_credentials():
        return {"error": {"message": "Bad credentials"}}, 401
