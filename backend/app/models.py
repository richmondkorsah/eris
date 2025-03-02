from app import db
from datetime import datetime

# Define the model for the user_data table
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)  # ✅ Allow NULL
    address = db.Column(db.String(9), nullable=False)
    area = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    district = db.Column(db.String(50))
    gpsname = db.Column(db.String(9))
    postcode = db.Column(db.String(10))
    region = db.Column(db.String(50))
    street = db.Column(db.String(10))

    def __init__(self, name, phone_number, address, area, latitude, longitude, district, gpsname, postcode, region, street):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.area = area
        self.latitude = latitude
        self.longitude = longitude
        self.district = district
        self.gpsname = gpsname
        self.postcode = postcode
        self.region = region
        self.street = street

# Define the model for the emergency_report table
class EmergencyReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.id'), nullable=False)
    emergency_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, emergency_type, description=None):
        self.user_id = user_id
        self.emergency_type = emergency_type
        self.description = description

UserData.emergencies = db.relationship('EmergencyReport', backref='user', lazy=True)

UserData.emergencies = db.relationship('EmergencyReport', backref='user', lazy=True)
