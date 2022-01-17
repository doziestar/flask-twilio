from flask import Flask, jsonify, request
from pydantic import BaseModel
from twilio.rest import Client

app = Flask(__name__)


class Model(BaseModel):
    message: str
    phone: str

# initialize the Client with the api key 
client = Client('account_sid', 'auth_token')

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    """Send a message with twilio api"""
    
    # get message and phone number from request body
    message = request.json['message']
    phone = request.json['phone']
    
    # send message through api
    message = client.messages.create(
        body=message,
        to=phone,
        from_="+1i8939393340" # your number here
    )
    # return token
    return jsonify(message.sid)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
