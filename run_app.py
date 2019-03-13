import os
from app import create_app, db
from flask_cors import CORS


app = create_app(os.getenv('APP_SETTINGS'))
CORS(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
