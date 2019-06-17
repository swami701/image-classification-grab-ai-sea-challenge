import flask
import flask_cors
import flask_restful
import utils

app = flask.Flask(__name__)
flask_cors.CORS(app)
api = flask_restful.Api(app)
utils.dynamically_register_resources(api)
