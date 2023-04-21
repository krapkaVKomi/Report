from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///report.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return 'Web App with Python Flask!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
