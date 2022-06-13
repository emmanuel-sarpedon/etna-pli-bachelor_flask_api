_email_pattern = "[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$"

registration = {
    'type': 'object',
    'properties': {
        'firstname': {'type': 'string', "minLength": 1},
        'lastname': {'type': 'string', "minLength": 1},
        'email': {'type': 'string', 'pattern': _email_pattern},
        'password': {'type': 'string'}
    },
    'required': ['firstname', 'lastname', 'email', 'password']
}

email_confirmation = {
    'type': 'object',
    'properties': {
        'token': {'type': 'string'}
    },
    'required': ['token']
}

token_renewal = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string', 'pattern': _email_pattern}
    },
    'required': ['email']
}

login = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string', 'pattern': _email_pattern},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password']
}
