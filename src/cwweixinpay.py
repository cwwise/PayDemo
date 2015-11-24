# coding: UTF-8
__author__ = 'weiwei'

import random
import hashlib
import time

import urllib.parse
import urllib.request

from xml.parsers.expat import ParserCreate
import json

#配置微信支付信息
APP_ID = ""
PARTNER_ID = ""
PARTNER_KEY = ""
#url
weixinPayURL = "https://api.mch.weixin.qq.com/pay/unifiedorder"

# 通知地址
notify_url = "http://www.weixin.qq.com/wxpay/pay.php"


def weixinSign(tradedict,paykey):
    listArray = []
    keys = sorted(tradedict)

    for key in keys:
        if key == "sign":
            continue
        string = key + "=" + tradedict[key]
        listArray.append(string)
    str = "&".join(listArray)
    str = str +"&" + "key=" + paykey
    return md5(str)

# 记录一下问题，python3.3上有问题。
# TypeError: Unicode-objects must be encoded before hashing，需要添加encode('utf-8')
# stackoverflow.com/questions/13265439/python-3-3-unicode-objects-must-be-encoded-before-hashing
def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest().upper()

def weixintradeno():

    timestr = time.time()
    tradeno = "weiwei" + "%d"%timestr
    return tradeno

def weixinnonce_str():
    list = random.sample('123456789ABCDEFGHIGKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba',32)
    return "".join(list)

#生成xml
def transformToXML(payDict):
    xml = []
    xml.append(r'<xml>')
    for key,value in payDict.items():
        xml.append(r"<%s>"%key)
        xml.append(value)
        xml.append(r"</%s>"%key)
    xml.append(r'</xml>')
    return "".join(xml)


def weipayaction(xml):
    website_bytes_utf8 = xml.encode(encoding="utf-8")
    req = urllib.request.Request(weixinPayURL)
    req.data = website_bytes_utf8

    f = urllib.request.urlopen(req)
    request = f.read().decode('utf-8')
    return request


class DefaultSaxHandler(object):
    dict = {}
    xmlName = ""
    def start_element(self, name, attrs):
        self.xmlName = name
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        self.xmlName = ""
        # print('sax:end_element: %s' % name)
        pass

    def char_data(self, text):
        if self.xmlName != "":
            self.dict[self.xmlName] = text
        # print('sax:char_data: %s' % text)

def weixinpayactionDemo():
    nonce_str = weixinnonce_str()
    tradeno = weixintradeno()

    info = {"appid": APP_ID}
    info["mch_id"] = PARTNER_ID
    info["device_info"] = "ios"
    info["nonce_str"] = nonce_str
    info["body"] = "微微helloworld"
    info["detail"] = "gooddetail"
    info["out_trade_no"] = tradeno
    info["total_fee"] = "1"
    info["spbill_create_ip"] = "192.168.1.1"
    info["notify_url"] = notify_url
    info["trade_type"] = "APP"

    sign = weixinSign(info,PARTNER_KEY)
    info["sign"] = sign

    xml = transformToXML(info)
    request = weipayaction(xml)

    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(request)

    weixinresponse = handler.dict

    # if weixinresponse["return_code"] == "SUCCESS" and weixinresponse["return_msg"] == "SUCCESS":
    #     print("成功")
    # else:
    #     return json.dumps({"flag":"101","msg":weixinresponse["return_msg"]})

    print(weixinresponse)
    timestamp = "%d"%time.time()
    response = {"appid":weixinresponse["appid"],
                "partnerid":weixinresponse["mch_id"],
                "prepayid":weixinresponse["prepay_id"],
                "package":"Sign=WXPay",
                "noncestr":weixinresponse["nonce_str"],
                "timestamp":timestamp}
    responsesign = weixinSign(response,PARTNER_KEY)
    #传给客户端的sign 是现在这几个参数的签名，不是微信服务器返回的。
    response["sign"] = responsesign

    return json.dumps(response)

if __name__ == '__main__':
    weixinpayactionDemo()

