from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/documentation'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/api/specs'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Flask API"})
