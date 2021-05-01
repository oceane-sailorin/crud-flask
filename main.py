import os

from app import create_app

FLASK_CONFIG = "dev"
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


@app.route("/")
def home():
    return "My flask app"


if __name__ == '__main__':
    app.run()
