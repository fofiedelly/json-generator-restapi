from flask import Flask, request, jsonify
from invalid_usage import InvalidUsage
import json

app = Flask(__name__)

authorized_types = ["text", "int", "double", "char"]

def read_file_content():
	f = open('lorem.txt')
	content = f.readlines()
	f.close()
	return content

@app.route('/', methods=['POST'])
def app_start():
	"""
	 Generate json content from the given schema
	"""
	content = read_file_content()
	if not request.is_json:
		raise InvalidUsage('You need to give a schema', status_code=410)
	schema = request.get_json()
	for key, value in schema.iteritems():
		print key, value
	return '%s' % "hello world" #% request.get_json()


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response