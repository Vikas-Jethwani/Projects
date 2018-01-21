#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot


app = Flask(__name__)
ACCESS_TOKEN = "EAAWSYLxC6dYBACDnYZCt6Rw7D4UnXL3APoHgetjy2dKRqPvlJHQ1oyT7B0rQn9om73IZCNT3MPcvObZCobV8xZCfUVI4R9RB1CklBk3dLahDC8ZAJciIhrts1ruhjCBEpgZCyp4AbupxQxRsPc8w22xrWacZCmIyZB3ee1ETHfXWtxNUNCHDpKM6KLvQUBLzMa0ZD"
VERIFY_TOKEN = "TooStrongForYou"
bot = Bot(ACCESS_TOKEN)
start = ['hi', 'hey', 'hello', 'good morning']
end = ['bye', 'goodbye', 'goodnight', 'ttyl', 'night']

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route('/', methods=['GET', 'POST'])
def receive_message():
	if request.method == 'GET':
		# Before allowing people to message your bot, Facebook has implemented a verify token
		# that confirms all requests that your bot receives came from Facebook. 
		token_sent = request.args.get("hub.verify_token")
		return verify_fb_token(token_sent)

	# if the request was not get, it must be POST and we can just proceed with sending a message # back to user
	else:
		# get whatever message a user sent the bot
		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for message in messaging:
				if message.get('message'):
					#Facebook Messenger ID for user so we know where to send response back to
					recipient_id = message['sender']['id']
					if message['message'].get('text'):
						user_msg = message['message'].get('text').lower()
						response_sent_text = get_message(user_msg)
						send_message(recipient_id, response_sent_text)
					#if user sends us a GIF, photo,video, or any other non-text item
					if message['message'].get('attachments'):
						response_sent_nontext = get_message()
						send_message(recipient_id, response_sent_nontext)
	return "Message Processed"

def verify_fb_token(token_sent):
	#take token sent by facebook and verify it matches the verify token you sent
	#if they match, allow the request, else return an error 
	if token_sent == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Invalid verification token'

#chooses a random message to send to the user
def get_message(user_msg=''):
	if user_msg in start:
		return "Hello, How are you today?"
	if user_msg in end:
		return "Bbye, see you later! Just remember : \"You're Awesome !\""
	sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
	# return selected item to the user
	return random.choice(sample_responses)


def send_message(recipient_id, response):
	#sends user the text message provided via input response parameter
	bot.send_text_message(recipient_id, response)
	return "success"



if __name__ == '__main__':
	app.run()