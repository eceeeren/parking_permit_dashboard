from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:parola321@localhost/parking_permit_db'
migrate = Migrate(app, db)

class Plate(db.Model):
    plate = db.Column(db.String, primary_key=True)
    owner = db.Column(db.String, nullable = True)
    start_time = db.Column(db.DateTime, nullable = True)
    end_time = db.Column(db.DateTime, nullable = True)

    def __repr__(self):
        return f"Plate: {self.plate}"

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()