from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "12345"

@app.route('/')
def home():
    return "WhatsApp Bot is Running!"

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        return challenge
    return "Invalid token", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    return "ok", 200

if __name__ == '__main__':
    app.run()
