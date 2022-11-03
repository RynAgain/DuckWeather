import requests as rq

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

    def get_data(self, city):
        self.dcity = city
        self.url = f'https://duckduckgo.com/js/spice/forecast/{self.dcity}/en'

        #url = "https://duckduckgo.com/js/spice/forecast/Austin/en"

        payload = ""
        response = rq.request("GET", self.url, data=payload)
        string = response.text
        jason = eval(string[string.find('''{"la''') : string.find(''');\n''')])
        self.data = jason

    def update(self):
        payload = ''
        response = rq.request("GET", self.url, data=payload)
        string = response.text
        jason = eval(string[string.find('''{"la''') : string.find(''');\n''')])
        self.data = jason

    def now(self):
        return self.data['currently']

    def UnixTime(self, timestamp):
        pass
