from flask import Flask, request
import africastalking
import os


app = Flask(__name__)
username = "sandbox"
api_key = "789jk8e4a3d3afd"
africastalking.initialize(username, api_key)
sms = africastalking.SMS


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get('sessionId', None)
    sercice_code = request.values.get('serviceCode', None)
    phone_number = request.values.get('phoneNumber', None)
    text = request.values.get('text', None)
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    def checkName():
        response = "CON invalid input, try again"

    registerInformation = {}
    warranties = []

    welcomeMsg = "CON Hello, welcome to e-registration platform\n 1. Register.\n 2. Check status validity."

    text_value = len(text.split('*'))
    txt = text.split('*')

    print(f"This is a text value: {text_value}")
    print(f"This is a text {txt}")
    print(f"Text values {text}")

    if(text == ''):
        response = welcomeMsg
    elif text_value == 1:
        response = "CON Please enter your full name to continue"
    elif text_value == 2:
        fullName = text.split('*')[1]
        if(len(fullName) < 3):
            response = "CON Invalid full name"
        else:
            response = "CON Enter your email address"
    elif text_value == 3:
        # check this in db before going to the next level, not yet implemented
        email = text.split('*')[2]
        response = "CON Enter your location"
    else:
        response = "END Thank you"
        loaction = text.split('*')[3]
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"), debug=True)
