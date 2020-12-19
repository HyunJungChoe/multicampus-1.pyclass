import urllib.request
import datetime
from config import *
import json

def get_request_url(url):

    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        # 잘 됐을 때
        if response.getcode() == 200:
            print("[%s] Url Request Success " %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None


# url =f"http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?YM=201201&NAT_CD=100&ED_CD=D&serviceKey={service_key}"
endPoint ="http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

param = "?_type=json&serviceKey="+service_key
param += "&YM=" +"201401"
param += "&NAT_CD=" +"112"
param += "&ED_CD=" +"E"
url = endPoint + param

'''
{"response":{"header":
{"resultCode":"0000","resultMsg":"OK"},
"body":{"items":
{"item":{"ed":"방한외래관광객","edCd":"E","natCd":112,"natKorNm":"중  국",
"num":167022,"rnum":1,"ym":201201}},
"numOfRows":10,"pageNo":1,"totalCount":1}}}
'''
arr1=[]
retData = get_request_url(url)
if (retData != None):
    jsonData = json.loads(retData)

if( jsonData['response']['header']['resultMsg'] =='OK'):
    krName = jsonData['response']['body']['items']['item']['natKorNm']
    iTotalVisit = jsonData['response']['body']['items']['item']['num']
    print(krName, ":", iTotalVisit)
    arr1.append(krName)
    arr1.append(iTotalVisit)
    print(arr1)



