from get_url import get_request_url
import urllib.request
import json
import math
from config import *

def getNatVisitor(yyyymm, nat_cd, ed_cd):
    end_point="http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters="?_type=json&serviceKey="+service_key
    parameters+="&YM="+yyyymm
    parameters+="&NAT_CD="+ nat_cd
    parameters+="&ED_CD="+ ed_cd
    
    url = end_point+parameters
    retData = get_request_url(url)
    if(retData==None):
        return None
    else:
        return json.loads(retData)
jsonResult=[]
natinal_code = "112" #중국
ed_cd ="E"
for year in range(2011,2017):
    for month in range(1,13):
        yyyymm = "{0}{1:0>2}".format(str(year),str(month))            
        
        jsonData = getNatVisitor(yyyymm, natinal_code,ed_cd)
        print(json.dumps(jsonData, indent=4, sort_keys=True,
            ensure_ascii=False))
        if (jsonData['response']['header']['resultMsg'] == 'OK'):
            krName=jsonData['response']['body']['items']['item']['natKorNm']
            krName= krName.replace(' ','')
            iTotalvisit=jsonData['response']['body']['items']['item']['num'] 
            jsonResult.append({'nat_Nm': krName, 'nat_cd': natinal_code,
                            'yyyymm':yyyymm, 'visit_cnt': iTotalvisit})  
            print(krName,":" ,iTotalvisit)
                

with open('%s_해외방문객정보_%d_%d.json' %("중국", 2011,2016),'w',
         encoding='utf-8') as file:
    jsonOut=json.dumps(jsonResult, 
                    indent=4, sort_keys=True,
                    ensure_ascii=False)
    file.write(jsonOut)
    
print('%s_해외방문객정보_%d_%d.json' %("중국", 2011,2016))
