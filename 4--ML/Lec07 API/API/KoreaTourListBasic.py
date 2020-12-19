from get_url import get_request_url
import urllib.request
import json
import math
from config import *

end_point="http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"

parameters="?_type=json&serviceKey="+service_key
parameters+="&YM=201201"
parameters+="&SIDO="+ urllib.parse.quote("부산광역시")
parameters+="&GUNGU="+ urllib.parse.quote("해운대구")
parameters+="&RES_NM="
parameters+="&pageNo=1"
parameters+="&numOfRows=100"
url = end_point+parameters
retData = get_request_url(url)

if(retData==None):
    print("None")
else:
    json_data = json.loads(retData)
    print(json_data)

