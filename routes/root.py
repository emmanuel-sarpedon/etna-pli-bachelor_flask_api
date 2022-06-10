from flask import Blueprint, request

bp = Blueprint('root', __name__)


@bp.route('/', methods=['GET'])
def index():
    return {
               "headers": str(request.headers).split("\r\n"),
               "_documentation": "https://github.com/emmanuel-sarpedon/etna-pli-bachelor_flask_api/blob/main/README.md"
           }, 200
