from flask import Flask, render_template, jsonify, request, abort
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

# app = Flask(__name__)

app.config.update(
	DEBUG = True,
	TEMPLATES_AUTO_RELOAD = True,
	SEND_FILE_MAX_AGE_DEFAULT = 1,
)

INDEX_TEMPLATE = 'index_new.html'
# INDEX_TEMPLATE = 'index.html'

STATIC_FOLDER = 'dist/static'

@app.route('/')
def index():
	return render_template(INDEX_TEMPLATE)

@app.route('/getData/', methods = ['POST'])
def getData():
	if (not request.json) or (not 'deliveryId' in request.json):
		abort(400)
	else:
		deliveryId = request.json['deliveryId']
		DongPoo = getDongPoo(deliveryId)
		BlackCat = getBlackCat(deliveryId)
		return jsonify(deliveryId = deliveryId, DongPoo = DongPoo, BlackCat = BlackCat)

TEST_DATA = [{
	'delievryId': '111',
	'DongPoo': 'DongPooRes111',
	'BlackCat': 'BlackCatRes111'
},
{
	'delievryId': '222',
	'DongPoo': 'DongPooRes222',
	'BlackCat': 'BlackCatRes222'
}
]

@app.route('/testPOST/', methods = ['POST'])
def testPOST():
	if (not request.json) or (not 'deliveryId' in request.json):
		abort(400)
	else:
		return jsonify(TEST_DATA)

@app.route('/<int:deliveryId>', methods = ['POST'])
def testAPI():
	return jsonify(deliveryId = deliveryId)

@app.route('/testPOSTMulti/', methods=['POST'])
def testPOSTMulti():
	if (not request.json) or (not 'deliveryId' in request.json):
		abort(400)
	else:
		res = [dId.strip() for dId in request.json['deliveryId'].split(',')]
		return jsonify(res)

if __name__ == "__main__":
	app.run(host = '127.0.0.1', port = 8000)
