from ics import Calendar
from flask import Flask, app
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

def main():
    url = "https://ade6-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=1b9e1ac2a1720dfd6bd1d42ad86c77f9c55ef35a53135e0070a97be8b09957efa9a0e9cb08b4730b&resources=4305&projectId=3&calType=ical&lastDate=2040-08-14"
    c = Calendar(requests.get(url).text)
    # print(c.events.begin)
    for event in c.events:
        print(f"Date : {event.begin.strftime('%d-%m-%Y %H:%M')}, matière : {event.name}, salle : {event.location.split(' ')[0]}")

    #string in datetime

main()