class User:
    @staticmethod
    def throw_error_ressource_not_found():
        return {"error": {"message": "Not found"}}

    @staticmethod
    def throw_error_email_already_validated():
        return {"error": {"message": "Email already validated"}}

    @staticmethod
    def throw_error_user_already_exists():
        return {"error": {"message": "User already exists"}}

    @staticmethod
    def throw_error_token_is_denied():
        return {"error": {"message": "Token expired"}}
