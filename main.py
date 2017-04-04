from flask import Flask, render_template, jsonify, request
from getDeliveryData import getDongPoo, getBlackCat
import json

class CustomFlask(Flask):
	jinja_options = Flask.jinja_options.copy()
	jinja_options.update(dict(
		block_start_string = '$$',
		block_end_string = '$$',
		variable_start_string = '$',
		variable_end_string = '$',
		comment_start_string = '$#',
		comment_end_string = '#$',
	))

app = CustomFlask(__name__)

app.config.update(
	DEBUG = True,
	TEMPLATES_AUTO_RELOAD = True,
	SEND_FILE_MAX_AGE_DEFAULT = 1,
)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/getData/', methods = ['POST'])
def getData():
	if (not request.json) or (not 'deliveryId' in request.json):
		abort(400)
	else:
		deliveryId = request.json['deliveryId']
		DongPoo = getDongPoo(deliveryId)
		BlackCat = getBlackCat(deliveryId)
		return jsonify(deliveryId = deliveryId, DongPoo = DongPoo, BlackCat = BlackCat)

if __name__ == "__main__":
	app.run(host = '0.0.0.0', debug = False)