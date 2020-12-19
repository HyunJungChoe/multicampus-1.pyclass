from get_url import get_request_url
import urllib.request
import json
import math
from config import *

def getTourPointVisitor(yyyymm, sido, gungu, nPageNum, nItems):
    end_point="http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
    parameters="?_type=json&serviceKey="+service_key
    parameters+="&YM="+yyyymm
    parameters+="&SIDO="+ urllib.parse.quote(sido)
    parameters+="&GUNGU="+ urllib.parse.quote(gungu)
    parameters+="&RES_NM="
    parameters+="&pageNo="+str(nPageNum)
    parameters+="&numOfRows="+str(nItems)
    url = end_point+parameters
    retData = get_request_url(url)
    if(retData==None):
        return None
    else:
        return json.loads(retData)
        

def getTourPointData(item, yyyymm, jsonResult):
    addrCd=0  if 'addrCD' not in item.keys() else item['addrCD']
    gungu=''  if 'gungu' not in item.keys() else item['gungu']
    resNm='' if 'resNm' not in item.keys() else item['resNm']
    sido='' if 'sido' not in item.keys() else item['sido']
    rnum=0 if 'rnum' not in item.keys() else item['rnum']
    csForCnt=0 if 'csForCnt' not in item.keys() else item['csForCnt']
    csNatCnt=0 if 'csNatCnt' not in item.keys() else item['csNatCnt']
    jsonResult.append({'yyymm':yyyymm, 'addrCd': addrCd,
                    'gungu':gungu, 'sido':sido, 'resNm':resNm,
                    'rnum':rnum, 'csForCnt':csForCnt, 'csNatCnt':csNatCnt})
    return

jsonResult=[]

for year in range(2011,2017):
    for month in range(1,13):
        yyyymm = "{0}{1:0>2}".format(str(year),str(month))
        nPageNum = 1        
        while True:
            jsonData = getTourPointVisitor(yyyymm,'서울특별시','',nPageNum,100)
            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                nTotal= jsonData['response']['body']['totalCount']
                if nTotal== 0: break

                for item in jsonData['response']['body']['items']['item']:
                    getTourPointData(item, yyyymm, jsonResult)

                nPage = math.ceil(nTotal/100)
                if(nPageNum == nPage): break;
            else:
                break;

with open('%s_관광지입장정보_%d_%d.json' %("서울특별시", 2011,2016),'w',
         encoding='utf-8') as file:
    jsonOut=json.dumps(jsonResult, 
                    indent=4, sort_keys=True,
                    ensure_ascii=False)
    file.write(jsonOut)
    
print('%s_관광지입장정보_%d_%d.json' %("서울특별시", 2011,2016))
