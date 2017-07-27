#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' get the quantity of tanmu and the name by encoded string of a video '

__author__ = 'Linyxus'

import requests
from bs4 import BeautifulSoup

_headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'x-requested-with': 'ShockwaveFlash/26.0.0.137',
    'referer': 'http://v.youku.com/v_show/id_XMjY3MTQ2MDE0OA==.html'
    }
_cook = { 'Cookie': '__ysuid=1484628226488b2i; __yscnt=1; juid=01blvlaj4l61t; yseid=1501135852682TNPlDS; yseidcount=2; seid=01bm1aml4e2avq; referhost=http%3A%2F%2Fwelcome.jsinfo.net; premium_cps=2045381824__93%7C455%7C85751%7C0__; ykss=0b8479596ed70dfb5f86d6eb; __aryft=1501137643; rpvid=1501140421482lyoH7F-1501140467442; __utmarea=; __ayvstp=28; __aysvstp=42; isg=AnR0o_ghkd4cBwWTF4ibfc4gRTsm5ZldPkbmZA7VYP-CeRTDNl1oxyp5n45d; ypvid=1501140583287bgrxvV; ysestep=15; yseidtimeout=1501147783291; ycid=0; ystep=19; seidtimeout=1501142383298; cna=ot8EEZHbomYCAXBXbJb10GiE; __ayft=1501135852905; __aysid=1501079883235zrW; __arpvid=15011405837591FEiOd-1501140583763; __arycid=dd-3-2074-319177-717029520; __ayscnt=1; __arcms=dd-3-2074-319177-717029520; __aypstp=18; __ayspstp=22; P_ck_ctl=7579FFE20A9FD709CAC63B3ECBCBC299' }

def getData(s):
    url = "http://ups.youku.com/ups/get.json?vid=" + s + "&ccode=0401&client_ip=192.168.1.1&utid=btgAEswglxcCAXnqDMBGuoa2&client_ts=1501162380"
    r = requests.get(url, cookies = _cook, headers = _headers).json()
    # print(r)
    data = { }
    iid = 0
    try:
        data['name'] = r['data']['video']['title']
        data['category'] = r['data']['video']['subcategories']
        iid = r['data']['video']['id']
    except Exception as e:
        print("!!!!! Failed while fetching data for %s" % s)
        print("Url: %s" % url)
        return
    url = "http://service.danmu.youku.com/pool/info?iid="+ str(iid) + "&ct=1001&cid=96&ouid=97454045&lid=0&aid=306326"
    r = requests.get(url, cookies = _cook, headers = _headers).json()
    data['count'] = r['count']
    return data

def fetchUrls(url):
    html = requests.get(url, cookies = _cook, headers = _headers).content.decode('utf-8')
    parser = BeautifulSoup(html, 'lxml')
    links = parser.find_all('a')
    return list(set([link['href'] for link in links if 'href' in link.attrs]))

def parseUrls(urls):
    def delSuffix(s):
        i = s.find('.html')
        j = s.find('#')
        if i != -1:
            s = s[:i]
        if j != -1:
            s = s[:j]
        return s
    l = [delSuffix(url[24:]) for url in urls if url[:21] == '//v.youku.com/v_show/']
    return list(filter(lambda x:  x != None, list(set(l))))

def test():
    print(getData("XMjg2ODExODA4MA=="))
    print(parseUrls(fetchUrls('https://tv.youku.com/')))
    print(list(map(getData, parseUrls(fetchUrls('http://list.youku.com/category/show/c_97_s_1_d_2.html')))))

if __name__=='__main__':
    test()
