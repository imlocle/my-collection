from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from src.route.home import home_api
from src.route.item import item_api
from src.route.location import location_api
from src.model.entity import Base, engine
from argparse import ArgumentParser
from src.util.constant import URL_PREFIX

def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    Base.metadata.create_all(engine)

    app.config['SWAGGER'] = {
        'title': 'My Collection Flask Swagger API',
    }
    swagger = Swagger(app)

    # API Routes
    app.register_blueprint(home_api, url_prefix=URL_PREFIX)
    app.register_blueprint(item_api, url_prefix=URL_PREFIX)
    app.register_blueprint(location_api, url_prefix=URL_PREFIX)

    return app


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app = create_app()
    app.run(host='0.0.0.0', port=port)