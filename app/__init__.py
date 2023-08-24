from flask import Flask


def create_app():
    """ 
    Application factory function to create and configure the Flask app.
    Registers blueprints for main and product routes.
    """

    app = Flask(__name__, template_folder="./templates",
                static_folder="./static")

    # Register main blueprint
    from .routes.main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .routes.product.views import product as product_blueprint
    app.register_blueprint(product_blueprint)

    return app
