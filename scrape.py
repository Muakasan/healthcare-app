#statesList = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

#$x('//table[thead/tr/th/text()="States"]/tbody/tr/td/text()')
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.PhantomJS('phantomjs')
driver.get("http://www.cdc.gov/outbreaks/index.html")
diseaseLinks = map(str, [x.get_attribute('href') for x in driver.find_elements(By.XPATH, '//div[@id="rss-outbreaksUS"]/ul/li/a')])
for j in map(lambda x: x[:x.index('index.html')]+"map.html", diseaseLinks):
    try:
        driver.get(j)
        print(j)
        print(map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/th/text()="States"]/tbody/tr/td')))
        print(map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/th/text()="State"]/tbody/tr/td')))
        print(map(lambda y: str(y.text), driver.find_elements(By.XPATH, '//table[thead/tr/td/text()="State"]/tbody/tr/td'))) 
    except:
        pass