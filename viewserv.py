from flask import jsonify, Flask, render_template, request
import requests

app = Flask(__name__)

#API_key= 'AIzaSyBPyOr8dQoKhti7HW6w02oYtTkdgfScPaM'
@app.route('/locate', methods=['POST'])
def locate():
    coord = {'Latitude': str(request.json['lat']),'Longitude': str(request.json['long'])}
    print("lat: " + str(request.json['lat']))
    print("long: " + str(request.json['long']))
    
    USstate = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={Latitude},{Longitude}&key=AIzaSyBPyOr8dQoKhti7HW6w02oYtTkdgfScPaM'.format(**coord))
    #print USstate.headers()
    return jsonify({'title': request.json['lat'],'content': request.json['long']})

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
