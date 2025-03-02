from flask import request, Blueprint, current_app, jsonify
import requests  
from app.models import UserData, EmergencyReport, db 
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

EXTERNAL_API_URL = os.getenv('EXTERNAL_API_URL')
if not EXTERNAL_API_URL:
    raise EnvironmentError("EXTERNAL_API_URL not set in environment variables.")

def ussd_callback(session_id, service_code, phone_number, text):
    emergency_mapping = {
        "1": "Flood",
        "2": "Fire",
        "3": "Earthquake",
        "4": "Accident",
        "5": "Medical Emergency",
        "6": "Power Outage",
        "7": "Other"
    }

    # Log the incoming request
    current_app.logger.info(f"USSD Callback Request: Session ID: {session_id}, Service Code: {service_code}, Phone Number: {phone_number}, Text: {text}")

    response = ""

    try:
        with current_app.app_context():
            if text == "":
                response = "CON Welcome to ERIS\n1. Register\n2. Report Emergency\n3. Exit"
            elif text == "1":
                response = "CON Please enter your name:\n"
            elif text.startswith("1*") and text.count("*") == 1:
                name = text.split("*")[1]
                response = f"CON Hi {name}, please enter your Digital Address (GhanaPost):\n"
            elif text.startswith("1*") and text.count("*") == 2:
                _, name, digital_address = text.split("*")

                # Check if the user already exists
                existing_user = UserData.query.filter_by(phone_number=phone_number).first()
                if existing_user:
                    response = "END You are already registered."
                    return response

                payload = {'address': digital_address}
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}

                try:
                    response_api = requests.post(EXTERNAL_API_URL, data=payload, headers=headers)
                    if response_api.status_code == 200 and response_api.json().get('found'):
                        location_data = response_api.json()['data']['Table'][0]

                        # Store user with phone number in the database
                        user_data = UserData(
                            name=name,
                            phone_number=phone_number,  
                            address=digital_address,
                            area=location_data.get('Area', ''),
                            latitude=location_data.get('CenterLatitude'),
                            longitude=location_data.get('CenterLongitude'),
                            district=location_data.get('District', ''),
                            gpsname=location_data.get('GPSName', ''),
                            postcode=location_data.get('PostCode', ''),
                            region=location_data.get('Region', ''),
                            street=location_data.get('Street', '')
                        )
                        db.session.add(user_data)
                        db.session.commit()

                        response = f"END Registration successful for {name} with phone number {phone_number}"
                    else:
                        response = "END Location not found. Please try again."
                except requests.RequestException as e:
                    current_app.logger.error(f"Error connecting to external service: {str(e)}")
                    response = f"END Error connecting to external service: {str(e)}"
            elif text == "2":
                response = "CON Report Emergency\n1. Flood\n2. Fire\n3. Earthquake\n4. Accident\n5. Medical Emergency\n6. Power Outage\n7. Other\nSelect an option:"
            elif text.startswith("2*"):
                emergency_type_code = text.split("*")[1]

                # Map the emergency type code to the emergency name
                emergency_type = emergency_mapping.get(emergency_type_code, "Unknown Emergency")

                # Get the user data from the database using the phone number
                user_data = UserData.query.filter_by(phone_number=phone_number).first()

                if user_data:
                    # Create a description with the emergency type and user's location
                    description = f"{emergency_type} at {user_data.area}, {user_data.region}, {user_data.street}"

                    # Create and commit the emergency report
                    emergency_report = EmergencyReport(user_id=user_data.id, emergency_type=emergency_type, description=description)
                    db.session.add(emergency_report)
                    db.session.commit()

                    response = "END Emergency report submitted successfully!"
                else:
                    response = "CON You need to register first."
            elif text == "3":
                response = "END Thank you for using our service!"
            else:
                response = "END Invalid option. Please try again."

    except Exception as e:
        current_app.logger.error(f"Error in USSD callback: {e}")
        response = "END Sorry, an error occurred. Please try again later."

    # Log the response
    current_app.logger.info(f"USSD Callback Response: {response}")

    return response
