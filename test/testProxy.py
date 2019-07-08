import sys,os
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'proxy')

sys.path.append(BASE_DIR)
import getProxy

# ipList = getProxy.parseHtmlToIPList(getProxy.getHtml(getProxy.getUrl(1)))
ipList = [{'IP': '125.115.181.229', 'PORT': '3128'}, {'IP': '117.93.83.55', 'PORT': '53281'}, {'IP': '183.129.207.86', 'PORT': '13974'}, {'IP': '222.184.254.170', 'PORT': '8888'}, {'IP': '60.216.101.46', 'PORT': '32868'}, {'IP': '114.55.103.83', 'PORT': '8089'}, {'IP': '106.12.124.116', 'PORT': '8118'}, {'IP': '1.197.204.244', 'PORT': '9999'}, {'IP': '223.100.166.3', 'PORT': '36945'}, {'IP': '117.87.178.237', 'PORT': '9000'}, {'IP': '180.118.128.188', 'PORT': '9000'}, {'IP': '163.125.31.16', 'PORT': '8118'}, {'IP': '180.118.247.89', 'PORT': '9000'}, {'IP': '117.90.252.71', 'PORT': '9000'}, {'IP': '163.125.112.192', 'PORT': '8118'}]

import requests, random, sqlite3




def getContentByProxy(url):
  count = 0
  while(count<100):
    try:
      rdm = random.randint(0, len(ipList)-1)
      ip = ipList[rdm]['IP']
      port = ipList[rdm]['PORT']

      proxies = {'http': 'http://{}:{}'.format(ip, port)}

      #http://34.80.19.146:8888/
      resp = requests.get(url, proxies=proxies)
      break
    except Exception as ex:
      print(ex)
    count+=1
    

  print(resp.text)
  return resp.text


getContentByProxy('http://34.80.19.146:8888/')




