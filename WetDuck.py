#WetDuck.py
#Code written by Ryan Satterfield 11/3/2022
import requests as rq
from datetime import datetime as dt

class Duck:
    def __init__(self, city):
        #super().__init__()
        self.dcity = city
        self.url = f'https://duckduckgo.com/js/spice/forecast/{self.dcity}/en'

        payload = ""
        response = rq.request("GET", self.url, data=payload)
        string = response.text
        jason = eval(string[string.find('''{"la''') : string.find(''');\n''')])
        self.data = jason
        #print(self.response.text)

    def get_data(self, city): #allows the changing of city
        self.dcity = city
        self.url = f'https://duckduckgo.com/js/spice/forecast/{self.dcity}/en'

        #url = "https://duckduckgo.com/js/spice/forecast/Austin/en"

        payload = ""
        response = rq.request("GET", self.url, data=payload)
        string = response.text
        jason = eval(string[string.find('''{"la''') : string.find(''');\n''')])
        self.data = jason

    def update(self): #updates without changing the city
        payload = ''
        response = rq.request("GET", self.url, data=payload)
        string = response.text
        jason = eval(string[string.find('''{"la''') : string.find(''');\n''')])
        self.data = jason

    def now(self): #gets all the current weather data in a dictionary 
        return self.data['currently']

    def last_update(self): #gets the time it last updated in the data
        last  = dt.fromtimestamp(self.now()['time'])
        return last

    def temp(self): #gets the current temp as a float
        return self.now()['temperature']

    def sky(self): #gets the current sky condition 
        return self.now()['summary']
