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

@app.route('/communities' , methods=['GET'])
def communities():
    
    comms = {'1':{'name':'Women Who Code','link':'https://www.womenwhocode.com/','description':'Women Who Code is an international nonprofit organization that provides a global community for women in tech with events, coding resources, jobs, mentorship, and more. They aim to inspire, support, and help women develop technical skills and excel in their careers.'},'2':{'name':'Hashnode','link':'','description':''},'2':{'name':'Hashnode','link':'','description':''},'2':{'name':'Hashnode','link':'http://hashnode.com/','description':'Hashnode is an online community where developers share knowledge and grow their careers. Developers from around the world participate in consequential discussions on Hashnode. You can write stories, ask open-ended questions as well as technical questions, ask questions anonymously, and start polls.'},'3':{'name':'Freecodecamp','link':'https://www.freecodecamp.org/','description':'freeCodeCamp is a nonprofit organization that helps people learn to code for free through thousands of videos, articles, interactive coding lessons and thousands of freeCodeCamp study groups around the world.'},'4':{'name':'StackOverflow','link':'https://stackoverflow.com/','description':'Stack Overflow is a question and answer site for programmers with tons of questions and answers on a wide range of topics in computer programming.You can learn from already asked and answered questions, share your programming knowledge by answering asked questions or share your issues/bugs here.'},'5':{'name':'Facebook Developers Circle','link':'https://developers.facebook.com/developercircles/','description':'Developer Circles from Facebook is a program designed to create locally organized communities for developers. These communities educate and provide a forum for discussion and knowledge sharing around topics that are top-of-mind for developers in a particular market.'},'6':{'name':'Google Developer Groups','link':'https://developers.google.com/community/gdg','description':'GDG brings software developers with similar interests together to meet through meetups and hands-on workshops. The community welcomes everyone and anyone interested in tech from beginners to experienced professionals.`'},'7':{'name':'Microsoft Learn Student Ambassadors','link':'https://studentambassadors.microsoft.com/','description':'Microsoft Learn Student Ambassadors are a global group of campus leaders who are ready to help fellow students, create robust tech communities, and develop technical and career skills for the future'}}
    return jsonify(comms)

@app.route('/opensource', methods=['GET'])
def opensource():
    open_source = {'1'{'name':'MLH Fellowship','link':'https://fellowship.mlh.io/','desc':'The MLH Fellowship is a 12-week internship alternative for aspiring software engineers. Our programs pair fun, educational curriculum with practical experience that you can put on your resume right away. Its collaborative, remote, and happens under the guidance of expert mentors.'},'2':{'name':'Google Summer of Code','link':'https://summerofcode.withgoogle.com/','desc':'Google Summer of Code is a global program focused on bringing more student developers into open source software development. Students work with an open source organization on a 10 week programming project during their break from school.'},'3':{'name':'Outreachy','link':'https://www.outreachy.org/','desc':'Outreachy provides remote internships. Outreachy supports diversity in open source and free software!'}}
    return jsonify(opensource)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
