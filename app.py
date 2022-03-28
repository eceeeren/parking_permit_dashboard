import re
from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:parola321@localhost/parking_permit_db'
migrate = Migrate(app, db)
CORS(app)


class Plate(db.Model):
    plate = db.Column(db.String, primary_key=True)
    owner = db.Column(db.String, nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)

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


def validate_plate(plate):
    response = Response("The plate is added.", status=200)
    not_valid = Response("This plate is not a valid German plate.", status=422)

    if len(plate.plate) == 0:
        response = Response("The plate area is blank.", status=400)
    else:
        if "-" not in plate.plate:
            response = not_valid
        else:
            plate_split = plate.plate.split("-")
            first_part = plate_split[0]
            second_part = plate_split[1]
            group_second = re.match(r"([a-z]+)([0-9]+)", second_part, re.I)
            group_second = group_second.groups()

            if len(first_part) > 3 or len(first_part) < 1 or type(first_part) != str:
                response = not_valid

            if len(group_second) != 2:
                response = not_valid
            elif not group_second[1].isdigit():
                response = not_valid
            else:
                if len(group_second[0]) > 2 or len(group_second[0]) < 1 or type(group_second[0]) != str:
                    response = not_valid
                elif len(group_second[1]) > 4 or len(group_second[1]) < 1 or group_second[1][0] == '0':
                    response = not_valid

    if len(plate.start_date) == 0 or len(plate.end_date) == 0:
        response = not_valid

    return response


@app.route("/")
def home():
    return "Hello, Flask!"

# Get all the plates


@app.route("/plate", methods=['GET'])
def get_plates():
    plates = Plate.query.order_by(Plate.plate.asc()).all()
    plate_list = []
    for plate in plates:
        plate_list.append(serialize_plate(plate))
    return {'plates': plate_list}

# Adding a new plate


@app.route("/plate", methods=['POST'])
def create_plate():
    plate_name = request.json['plate']
    owner = request.json['owner']
    start_date = request.json['start_date']
    end_date = request.json['end_date']
    plate = Plate(plate_name, owner, start_date, end_date)
    response = validate_plate(plate)
    if response.status_code == 200:
        db.session.add(plate)
        db.session.commit()
        print(response.response[0])
        return serialize_plate(plate)
    else:
        print(response.response[0])
        return response


if __name__ == "__main__":
    app.run()
