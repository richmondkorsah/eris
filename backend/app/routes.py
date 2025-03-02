from flask import Blueprint, request, jsonify
from app.services.ussd import ussd_callback

bp_ussd = Blueprint('ussd', __name__)

# USSD Route
@bp_ussd.route('/ussd', methods=['POST'])
def ussd_handler():  # Renamed to avoid conflict
    # Log the incoming request for debugging
    print("USSD request data:", request.form)
    
    # Safely retrieve the USSD request data
    session_id = request.form.get('sessionId', '')
    service_code = request.form.get('serviceCode', '')
    phone_number = request.form.get('phoneNumber', '')
    text = request.form.get('text', '')

    # Ensure all fields are present
    if not session_id or not service_code or not phone_number:
        return jsonify({"error": "Missing required fields"}), 400

    # Call the USSD handling function
    try:
        response = ussd_callback(session_id, service_code, phone_number, text)
        return response
    except Exception as e:
        print("Error in USSD callback:", str(e))  # Log the error
        return jsonify({"error": "An internal error occurred"}), 500
