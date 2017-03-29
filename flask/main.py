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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getData/', methods = ['POST'])
def getData():
    if not request.json or not 'deliveryId' in request.json:
        abort(400)
    else:
    	deliveryId = request.json['deliveryId']
    	print(deliveryId)
    	DongPoo = getDongPoo(deliveryId)
    	BlackCat = getBlackCat(deliveryId)
    	return jsonify(deliveryId = deliveryId, DongPoo = DongPoo, BlackCat = BlackCat)