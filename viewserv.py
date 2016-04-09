from flask import jsonify

@app.route('/', methods=['POST'])

def locate():
	return jsonify({'test':return.form['lat'],return.form['long']})
