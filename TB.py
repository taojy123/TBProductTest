
import cookielib
import urllib2, urllib
import time
import re
import traceback
import time
import random
 
 
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.ProxyHandler({'http':"10.239.120.37:911"}))
opener.addheaders = [
    ("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
    ("Accept-Encoding","gzip,deflate,sdch"),
    ("Accept-Language","zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4"),
    ("Cache-Control","max-age=0"),
    ("Connection","keep-alive"),
    ("Cookie","cna=iooaDWlj5nECARtzb4o2BjVI; thw=cn; miid=5419896086933682990; ali_ab=192.102.204.36.1419221490535.7; cainiao_abtest9_1=0; lzstat_uv=2634468712242686820|3269294@3369100@2706017; x=135913393; unt=taojy123%26unit; _cc_=VT5L2FSpdA%3D%3D; tg=0; _tb_token_=H6O9fspE40538C4; uc3=nk2=&id2=&lg2=; tracknick=; mt=ci=0_0&cyk=0_0; ck1=; v=0; cookie2=2c165d981720564d64b53fbb3ae20a35; t=ba3d8b21a95290aedd52221979ab0bff; isg=642163065BB4F8F1E2A3B09C71AB937A"),
    ("Host","item.taobao.com"),
    ("RA-Sid","1B736F8A-20150109-013640-a1edc4-5e3f41"),
    ("RA-Ver","2.8.8"),
    ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1964.4 Safari/537.36"),
]
 



s = open("data.txt").read()

s = s.replace(" ", "").replace("\n", "").replace("\xa3\xac", ",").replace("\xef\xbc\x8c", ",")

ids = s.split(",")#[:20]

exist_ids = []
s = ""
for pid in ids:

    url = "http://item.taobao.com/item.htm?id=%s" % pid
    # url = "http://detail.tmall.com/item.htm?spm=a230r.1.14.19.jOJvQH&id=%s&ns=1&_u=c2nan5b7eb1&abbucket=12&smtmd=0.80828969529929?" % id
    print url

    try:
        p = opener.open(url, timeout=5)
        new_url = p.geturl()

        i = 0
        while "login" in new_url:
            t = random.random() * 3
            print t
            time.sleep(t)
            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            opener.addheaders = [
                ("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
                ("Accept-Encoding","gzip,deflate,sdch"),
                ("Accept-Language","zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4"),
                ("Cache-Control","max-age=0"),
                ("Connection","keep-alive"),
                ("Cookie","cna=iooaDWlj5nECARtzb4o2BjVI; thw=cn; miid=5419896086933682990; ali_ab=192.102.204.36.1419221490535.7; cainiao_abtest9_1=0; lzstat_uv=2634468712242686820|3269294@3369100@2706017; x=135913393; unt=taojy123%26unit; _cc_=VT5L2FSpdA%3D%3D; tg=0; _tb_token_=H6O9fspE40538C4; uc3=nk2=&id2=&lg2=; tracknick=; mt=ci=0_0&cyk=0_0; ck1=; v=0; cookie2=2c165d981720564d64b53fbb3ae20a35; t=ba3d8b21a95290aedd52221979ab0bff; isg=642163065BB4F8F1E2A3B09C71AB937A"),
                ("Host","item.taobao.com"),
                ("RA-Sid","1B736F8A-20150109-013640-a1edc4-5e3f41"),
                ("RA-Ver","2.8.8"),
                ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1964.4 Safari/537.36"),
            ]
            p = opener.open(url, timeout=5)
            new_url = p.geturl()
            i += 1
            if i > 10:
                raise

        print new_url
        if "noitem" in new_url:
            s += "<span style='color:red'>%s\xa3\xac</span>" % pid
        else:
            exist_ids.append(pid)
            s += "<span style='color:black'>%s\xa3\xac</span>" % pid
            
    except:
        print "timeout"
        s += "<span style='color:yellow'>%s,</span>" % pid

    time.sleep(0.3)


html = "<div >%s<div>" % s

open("output.html", "w").write(s)

open("output.txt", "w").write(",".join(exist_ids))


print "ok"

raw_input()



