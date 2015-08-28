import requests
import json

class WebappBase(object):

    BASE_URL = "http://127.0.0.1:5000/"

    def __init__(self):
        self.token = ""
        self.username = ""
        self.password = ""


    def create_token(self):
        api_end = "%sapi/token" % self.BASE_URL
        auth = requests.auth.HTTPBasicAuth(self.username, self.password)
        print "*INFO* Sending request with username password to %s" % api_end
        r = requests.get(api_end, auth=auth)
        print "*INFO* Reponse is %s" % r.text
        resp = json.loads(r.text)
        self.token = resp['token']
        if 'token' not in resp:
            raise AssertionError

    def create_user(self, username, password):
        self.username = username
        self.password = password
        api_end = "%sapi/users" % self.BASE_URL
        payload = {'username' : self.username, 'password' : self.password}
        payload = json.dumps(payload)
        headers = {'Content-Type':'application/json'}
        print "*INFO* Sending request with username password to %s" % api_end
        r = requests.post(api_end, data=payload, headers=headers)
        print "*INFO* Reponse is %s" % r.text
        try:
            resp = json.loads(r.text)
        except ValueError, e:
            print "Exception caught %s" % e
        if self.username != str(resp['username']):
            raise AssertionError

    def do_cleanup(self):
        api_end = "%sapi/cleanup" % self.BASE_URL
        auth = requests.auth.HTTPBasicAuth(self.username, self.password)
        print "*INFO* Sending request with username password to %s" % api_end
        r = requests.get(api_end, auth=auth)
        print "*INFO* Reponse is %s" % r.text
        resp = json.loads(r.text)
        if self.username != str(resp['user']):
            raise AssertionError


