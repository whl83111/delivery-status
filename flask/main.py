from flask import Flask, render_template, jsonify, request
from getDeliveryData import getBlackCat
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
    print(request)
    if not request.json or not 'deliveryId' in request.json:
        abort(400)
    deliveryId = request.json
    print(deliveryId)
    return jsonify(deliveryId)