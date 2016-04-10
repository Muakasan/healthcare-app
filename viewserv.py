from flask import jsonify, Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

app = Flask(__name__)

#API_key= 'AIzaSyBPyOr8dQoKhti7HW6w02oYtTkdgfScPaM'
@app.route('/locate', methods=['POST'])
def locate():
    coord = {'Latitude': str(request.json['lat']),'Longitude': str(request.json['long'])}
    print("lat: " + str(request.json['lat']))
    print("long: " + str(request.json['long']))
    
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={Latitude},{Longitude}&key=AIzaSyBPyOr8dQoKhti7HW6w02oYtTkdgfScPaM'.format(**coord))
    statesList = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    addressList = map(lambda x: str(x.values()[0]), response.json()[u'results'][1][u'address_components']) 
    print(addressList)
    state = ""
    for i in addressList:
        if i in statesList:
            state = i

    #state = str(response.json()[u'results'][1][u'address_components'][3][u'long_name'])
    print("State", state)
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://www.cdc.gov/outbreaks/index.html")
    print("Reached CDC Website")
    diseaseLinks = map(str, [x.get_attribute('href') for x in driver.find_elements(By.XPATH, '//div[@id="rss-outbreaksUS"]/ul/li/a')])
    outbreaksInAreaList = []
    for x in diseaseLinks:
        try:
            j = x[:x.index('index.html')]+"map.html"
            print("Arrived at", j)
            driver.get(j)
            if state in map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/th/text()="States"]/tbody/tr/td')):
                #print(map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/th/text()="States"]/tbody/tr/td')))
                outbreaksInAreaList.append(j)
            if state in map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/th/text()="State"]/tbody/tr/td')):
                #print(map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/th/text()="State"]/tbody/tr/td')))
                outbreaksInAreaList.append(j)
            if state in map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/td/text()="State"]/tbody/tr/td')):
                #print(map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/td/text()="State"]/tbody/tr/td')))
                outbreaksInAreaList.append(j)
            print("Found elements in", j)
        except:
            pass
 
    return jsonify({'link': outbreaksInAreaList, 'state': state})

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
