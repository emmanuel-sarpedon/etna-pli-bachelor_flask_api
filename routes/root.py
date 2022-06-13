from flask import Blueprint, request

bp = Blueprint('root', __name__)


@bp.route('/', methods=['GET'])
def index():
    return {
               "_doc": "{}api/documentation".format(request.host_url),
               "_specs": "{}api/specs".format(request.host_url)
           }, 200
