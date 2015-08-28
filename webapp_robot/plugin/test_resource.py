from webapp_robot.base import WebappBase
import requests
import json


class Resource(WebappBase):

    def access_resource_from_token(self):
        """
        Access resource using the token
        """
        api_end = "%sapi/resource" % self.BASE_URL
        auth = requests.auth.HTTPBasicAuth(self.token, 'x')
        print "*INFO* Sending request with username password to %s" % api_end
        r = requests.get(api_end, auth=auth)
        resp = json.loads(r.text)
        print "*INFO* Reponse is %s" % r.text
        if self.username not in str(resp['data']):
            raise AssertionError


    def access_resource_from_username(self):
        """
        Access resource using the username
        """
        api_end = "%sapi/resource" % self.BASE_URL
        auth = requests.auth.HTTPBasicAuth(self.username, self.password)
        print "*INFO* Sending request with username password to %s" % api_end
        r = requests.get(api_end, auth=auth)
        resp = json.loads(r.text)
        print "*INFO* Reponse is %s" % r.text
        if self.username not in str(resp['data']):
            raise AssertionError


