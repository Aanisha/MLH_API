from bs4 import BeautifulSoup as BS 
import requests 
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def getInfo(url):

    
    # getting the request from url  
    data = requests.get(url) 
  
    # converting the text  
    soup = BS(data.text, 'html.parser')

    event_links_tags = soup.find_all("a", class_ = "event-link")
    event_names = soup.find_all("h3", class_ = "event-name")
    event_date = soup.find_all("p", class_ = "event-date")
    
    event_links = []
    event_name = []
    event_dates = []

    for event in event_links_tags:
        event_links.append(event.get('href'))
    
    for event in event_names:
        event_name.append(event.text)
    
    for event in event_date:
        event_dates.append(event.text)
    
    

    event_dict = {}

    for i in range(0,len(event_links)):

        
        event = {'event_name':event_name[i],'event_link':event_links[i],'event_date':event_dates[i]}
        event_dict[i] = event
    
    final_events = {'2021' : event_dict}
    return final_events

@app.route('/hackathons/MLH', methods=['GET'])
def MLH(): 
    # url to get event info
    url = "https://mlh.io/seasons/2021/events"
  
    # calling the get_info method 
    ans = getInfo(url)
    return jsonify(ans)  

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
