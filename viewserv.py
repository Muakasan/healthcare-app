from flask import jsonify, Flask, render_template

app = Flask(__name__)

@app.route('/locate', methods=['POST'])
def locate():
    print(request.json['lat'])
    return jsonify({'title':request.json['lat'],'content': request.json['long']})

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)