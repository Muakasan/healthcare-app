from flask import jsonify, Flask, render_template, request

app = Flask(__name__)

@app.route('/locate', methods=['POST'])
def locate():
    print("lat: " + str(request.json['lat']))
    print("long: " + str(request.json['long']))
    return jsonify({'title': request.json['lat'],'content': request.json['long']})

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)