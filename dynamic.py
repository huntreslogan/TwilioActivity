from twilio.rest import TwilioRestClient
from flask import Flask, request
import twilio.twiml

app = Flask(__name__)

callers = {
	"[yourNumber]":"[yourName]",
	"[otherNumber]":"[otherName]",
	"[otherNumber2]":"[otherName2]"
}

@app.route("/", methods=["GET","POST"])
def hello_custom():
	from_number = request.values.get("From")
	if from_number in callers:
		name = callers[from_number]
	else:
		name = "Hacker"

	message = "Hello, {}, thanks for the message!".format(name)
	resp = twilio.twiml.Response()
	resp.message(message)
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
