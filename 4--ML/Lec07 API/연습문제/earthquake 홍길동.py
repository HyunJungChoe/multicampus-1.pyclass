import urllib.request
import ssl 

from bs4 import BeautifulSoup

import datetime
import math
import pandas as pd

context = ssl._create_unverified_context()

def get_request_url(url):
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now() )
            return response.read().decode("CP949")
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None


#endpoint = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist.jsp?"


#if __name__ == "__main__":
