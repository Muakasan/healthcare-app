from flask import jsonify, Flask

app = Flask(__name__)

@app.route('/', methods=['POST'])
def locate():
    print(request.json['lat'])
    return jsonify({'title':request.json['lat'],'content': request.json['long']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)