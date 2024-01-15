from flask import Flask
from config import config

# Routes
from src.routes import Languages

app = Flask(__name__)

def page_not_found(error):
    return "<h1>PAGINA NO ENCONTRADA :c</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BLUEPRINTS 
    app.register_blueprint(Languages.main, url_prefix="/api/languages")


    app.register_error_handler(404, page_not_found)
    app.run(port=5001)
