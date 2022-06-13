from flask import Blueprint, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_swagger import swagger
from flask import jsonify
from app import create_app

bp = Blueprint('root', __name__)

SWAGGER_URL = '/api/documentation'  # URL for exposing Swagger UI
SPECS_URL = '/api/specs'  # URL for getting Swagger specifications of the current API


@bp.route('/', methods=['GET'])
def index():
    print(request.host)
    return {
               "_documentation": request.host + SWAGGER_URL,
               "_swagger_specs": request.host + SPECS_URL
           }, 200


@bp.route('/api/specs')
def spec():
    """
    It returns a JSON object that contains the Swagger specification for the Flask app
    :return: The swagger specification for the API.
    """
    swag = swagger(
        create_app(),
        template={
            "info": {
                "version": "0.1.0",
                "title": "Flask"
            }
        })

    return jsonify(swag)


# Registering the blueprint for the Swagger UI.
swaggerui_bp = get_swaggerui_blueprint(SWAGGER_URL, SPECS_URL, config={'app_name': "Flask API"})
