sign_up = {
    'type': 'object',
    'properties': {
        'firstname': {'type': 'string', "minLength": 1},
        'lastname': {'type': 'string', "minLength": 1},
        'email': {'type': 'string', 'pattern': "[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$"},
        'password': {'type': 'string'}
    },
    'required': ['firstname', 'lastname', 'email', 'password']
}
