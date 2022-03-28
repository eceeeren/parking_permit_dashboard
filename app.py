from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:parola321@localhost/parking_permit_db'
migrate = Migrate(app, db)

class Plate(db.Model):
    plate = db.Column(db.String, primary_key=True)
    owner = db.Column(db.String, nullable = True)
    start_date = db.Column(db.DateTime, nullable = True)
    end_date = db.Column(db.DateTime, nullable = True)

    def __repr__(self):
        return f"Plate: {self.plate}"

    def __init__(self, plate, owner, start_date, end_date):
        self.plate = plate
        self.owner = owner
        self.start_date = start_date
        self.end_date = end_date

# Make plates json serializable
def serialize_plate(plate):
    return {
        "plate": plate.plate,
        "owner": plate.owner,
        "start_date": plate.start_date,
        "end_date": plate.end_date
    }

@app.route("/")
def home():
    return "Hello, Flask!"

# Get all the plates
@app.route("/plates", methods=['GET'])
def get_plates():
    plates = Plate.query.order_by(Plate.plate.asc()).all()
    plate_list = []
    for plate in plates:
        plate_list.append(serialize_plate(plate))
    return {'plates': plate_list}

# Adding a new plate
@app.route("/plates", methods=['POST'])
def create_plate():
    plate_name = request.json['plate']
    owner = request.json['owner']
    start_date = request.json['start_date']
    end_date = request.json['end_date']
    plate = Plate(plate_name, owner, start_date, end_date)
    db.session.add(plate)
    db.session.commit()
    return serialize_plate(plate)

if __name__ == "__main__":
    app.run()