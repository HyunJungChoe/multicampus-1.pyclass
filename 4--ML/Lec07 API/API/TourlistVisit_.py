import urllib.request
import datetime
import json
from config import *

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            print("[%s] Url Request Success " %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None


def getNatVisitor(yyyymm, nat_cd, ed_cd):
    endPoint = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    param = "?_type=json&serviceKey="+service_key
    param += "&YM=" + yyyymm
    param += "&NAT_CD=" + nat_cd
    param += "&ED_CD=" +ed_cd
    url = endPoint + param
    retData = get_request_url(url)
    if(retData == None):
        return None
    else :
        return json.loads(retData)

jsonResult=[]
nStartYear = 2011
nEndYear = 2016
nat_cd ='275'
ed_cd ='E'
for year in range(nStartYear,  nEndYear+1):
    for month in range(1,13):
        yyyymm = "{0}{1:0>2}".format(str(year), str(month))
        jsonData = getNatVisitor(yyyymm,nat_cd, ed_cd)
        if( jsonData['response']['header']['resultMsg'] =='OK'):
            krName = jsonData['response']['body']['items']['item']['natKorNm']
            iTotalVisit = jsonData['response']['body']['items']['item']['num']
            print(krName, ":", yyyymm ,":", iTotalVisit)
            jsonResult.append({'nat_name':krName,'nat_cd': nat_cd,
                            'yyyymm':yyyymm, 'visit_cnt':iTotalVisit  })

with open('%s(%s)_해외방문객정보_%d%d.json'%(krName,nat_cd, nStartYear, nEndYear),'w',encoding='utf8') as outfile:
    retJson = json.dumps(jsonResult, indent= 4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)

# import matplotlib.pyplot as plt
# import matplotlib
# plt.xticks(index, visitYM)
# plt.plot(index, cntVisit)
# plt.show()
