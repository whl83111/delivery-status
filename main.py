from flask import Flask, render_template, jsonify, request, abort
from getDeliveryData import GetDeliveryData
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

# app = Flask(__name__)

app.config.update(
	DEBUG = True,
	TEMPLATES_AUTO_RELOAD = True,
	SEND_FILE_MAX_AGE_DEFAULT = 1,
)

INDEX_TEMPLATE = 'index.html'

@app.route('/')
def index():
	return render_template(INDEX_TEMPLATE)

@app.route('/<int:deliveryId>', methods = ['POST'])
def testAPI():
	return jsonify(deliveryId = deliveryId)

@app.route('/getData/', methods=['POST'])
def testPOSTMulti():
	if (not request.json) or (not 'deliveryId' in request.json):
		abort(400)
	else:
		deliveryIds = [dId.strip() for dId in request.json['deliveryId'].split(',')]
		print(deliveryIds)
		responseDatas = [GetDeliveryData(deliveryId).getDict() for deliveryId in deliveryIds]
		print(responseDatas)
		return jsonify(responseDatas)

if __name__ == "__main__":
	app.run(host = '127.0.0.1', port = 8000)
