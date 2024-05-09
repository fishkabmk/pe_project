from flask import Flask
import jsonrpc.beer
from config import settings
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
jsonrpc.beer.jsonrpc.init_app(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "FLASK-JSONRPC",
        'tryItOutEnabled': "false"
    }
)

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)
