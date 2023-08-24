
from app import create_app
import os

app = create_app()

# Set secret key from environment variable or a configuration file
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

if __name__ == '__main__':
    app.run(debug=True)
