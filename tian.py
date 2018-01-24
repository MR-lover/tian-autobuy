#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

import requests
import time
import urllib
import urllib.request
import urllib.parse
import json
import sys
# 引入命令行
# import sys, getopt
#opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
# for op, value in opts:
#     if op == "-u":
#         user = value
#     elif op == "-p":
#         password = value
#     elif op == "-c":
#         usage()
#         sys.exit()
import argparse

# 账号
user = ''
# 密码
password = ''
# 具体商品的fk_goods_id, 林俊杰:31799
goodsId = ''
# 31667
# 可以接受的价格范围
minPrice = 0
maxPrice = 1000
# 票的数量
ticketNum = 3
# 取票人姓名
name = '田大爷'
# 取票人电话
phone = ''
# 取票人QQ号
qq = ''
# 取票人身份证后6位数
idcard = ''

# 命令行参数
parser = argparse.ArgumentParser(description='tiandaye')
# 账号
parser.add_argument('-u', '--user', help='login user name', default='')
# 密码
parser.add_argument('-p', '--password', help='login user password', default='')
# 商品id
parser.add_argument('-g', '--good', help='good ID', default='')
# 数量
parser.add_argument('-c', '--count', type=int, help='The count to buy', default=1)
# 取票人姓名
parser.add_argument('-name', '--name', help='取票人姓名', default='田大爷')
# 取票人电话
parser.add_argument('-phone', '--phone', help='取票人电话', default='')
# 取票人QQ号
parser.add_argument('-qq', '--qq', help='取票人QQ号', default='408596288')
# 取票人身份证后6位数
parser.add_argument('-idcard', '--idcard', help='取票人身份证后6位数', default='')
# 可以接受的最低价
parser.add_argument('-minPrice', '--minPrice', type=int, help='可以接受的最低价', default=0)
# 可以接受的最高价
parser.add_argument('-maxPrice', '--maxPrice', type=int, help='可以接受的最高价', default=1000)
# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# parser.add_argument('-a', '--area',
#                     help='Area string, like: 1_72_2799_0 for Beijing', default='1_72_2799_0')
# parser.add_argument('-g', '--good',
#                     help='Jing Dong good ID', default='')
# parser.add_argument('-c', '--count', type=int,
#                     help='The count to buy', default=1)
# parser.add_argument('-w', '--wait',
#                     type=int, default=500,
#                     help='Flush time interval, unit MS')
# parser.add_argument('-f', '--flush',
#                     action='store_true',
#                     help='Continue flash if good out of stock')
# parser.add_argument('-s', '--submit',
#                     action='store_true',
#                     help='Submit the order to Jing Dong')
options = parser.parse_args()
print (options)
if options.user != '':
      user = options.user
if options.password != '':
      password = options.password
if options.good != '':
      goodsId = options.good
if options.count != 1:
      ticketNum = options.count

# 可以接受的价格范围
minPrice = options.minPrice
maxPrice = options.maxPrice
# 取票人姓名
name = options.name
# 取票人电话
phone = options.phone
# 取票人QQ号
qq = options.qq
# 取票人身份证后6位数
idcard = options.idcard

print ('接受的参数:')
print (options)
print('\n')
# sys.exit()

# 开始时间
print ('总的开始时间:')
print (time.strftime('%Y-%m-%d %H:%M:%S"',time.localtime(time.time())))
# 总的耗时统计-开始时间
allStartTime = time.clock()
# 耗时统计-开始时间
startTime = time.clock()
# 请求的路径
loginUrl='http://appo4.owhat.cn/api'
# 时间戳
t = time.time()
# 需要发送的数据
data={
      'apiv':'1.0.0',
      'cmd_s':'user.account',
      'cmd_m':'login',
      'v':'1.0',
      'client':{'platform':'ios','deviceid':'0A839A4E-B934-4A37-87BE-FC2E4A5DE60E','channel':'AppStore','version':'4.4.1'},
      'requesttimestap':t,
      'data':{'account':user,'password':password}
      }

data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
request = urllib.request.Request(loginUrl)
# adding charset parameter to the Content-Type header.
request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
f = urllib.request.urlopen(request, data)
response = f.read().decode('utf-8')
response = json.loads(response)
print ('第一次请求的数据:')
print (data)
print ('第一次请求-响应的数据:')
print (json.dumps(response))
# 耗时统计-结束时间
endTime = time.clock()
print ("消耗时间: %f s" % (endTime - startTime))
print ('\n')
print ('\n')

# 第一次请求得到的用户id和token
token = response['data']['token']
userid = response['data']['userid']

# 第二次请求
# 耗时统计-开始时间
startTime = time.clock()
# 时间戳
t = time.time()
data={
      'cmd_s':'msg',
      'cmd_m':'findjpushtaglist',
      'userid': userid,
      'token': token,
      'apiv': '1.0.0',
      'v':'1.0',
      'requesttimestap': t,
      'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"}
      }
headers = {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8"}
#postdata=urllib.parse.urlencode(data)
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
result=requests.post(loginUrl,data=data,headers=headers)
# print (result.encoding)
# print (result.json())
print ('第二次请求的数据:')
print (data)
print ('第二次请求-响应的数据:')
print (result.text)
# 耗时统计-结束时间
endTime = time.clock()
print ("消耗时间: %f s" % (endTime - startTime))
print ('\n')
print ('\n')

# 第三次请求
# 耗时统计-开始时间
startTime = time.clock()
# 时间戳
t = time.time()
data={
      'cmd_s':'common',
      'cmd_m':'usertoken',
      'userid': userid,
      'token': token,
      'apiv': '1.0.0',
      'v':'1.0',
      'requesttimestap': t,
      'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"}
      }
headers = {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8"}
#postdata=urllib.parse.urlencode(data)
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
result=requests.post(loginUrl,data=data,headers=headers)
# print (result.encoding)
# print (result.json())
print ('第三次请求的数据:')
print (data)
print ('第三次请求-响应的数据:')
print (result.text)
# 耗时统计-结束时间
endTime = time.clock()
print ("消耗时间: %f s" % (endTime - startTime))
print ('\n')
print ('\n')

# 第四次请求
# 耗时统计-开始时间
startTime = time.clock()
# 时间戳
t = time.time()
data={
      'cmd_s':'user.account',
      'cmd_m':'my',
      'userid': userid,
      'token': token,
      'apiv': '1.0.0',
      'v':'1.0',
      'requesttimestap': t,
      'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"}
      }
headers = {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8"}
#postdata=urllib.parse.urlencode(data)
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
result=requests.post(loginUrl,data=data,headers=headers)
# print (result.encoding)
# print (result.json())
print ('第四次请求的数据:')
print (data)
print ('第四次请求-响应的数据:')
print (result.text)
# 耗时统计-结束时间
endTime = time.clock()
print ("消耗时间: %f s" % (endTime - startTime))
print ('\n')
print ('\n')

# 下单操作一共分三步骤
# 耗时统计-开始时间
startTime = time.clock()
# 下单第一步:获得想购买的票
# 时间戳
t = time.time()
# 商品id
goodData = {"fk_goods_id":goodsId}
data={
      'cmd_s':'shop.price',
      'cmd_m':'findPricesAndStock',
      'userid': userid,
      'token': token,
      'apiv': '1.0.0',
      'v':'1.0',
      'requesttimestap': t,
      'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"},
      'data': goodData
      }
headers = {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8"}
#postdata=urllib.parse.urlencode(data)
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
result=requests.post(loginUrl,data=data,headers=headers)
# print (result.encoding)
# print (result.json())
print ('下单第一步, 请求的数据:')
print (data)
print ('下单第一步, 需要找那个商品下面的票:')
print (result.text)

# 价格列表
response = json.loads(result.text)
ticketId = ''
print ('价格列表:')
print (response['data']['prices'])
for good in response['data']['prices']:
    price = good['price']
    if price >= minPrice and price <= maxPrice:
      ticketId = good['id']
      print (good)
      break;
    else:
      continue
print ('具体价格的id:')
print (ticketId)
# 需要额外的数据
extList = response['data']['extlist']
# extraInfo = {}
strName = "取票人姓名（必须与有效证件一致）"
strPhone = "取票人电话（重要！别写错了！）"
strQQ = "取票人QQ号"
strIdCard1 = "取票人身份证后6位（如实填写，凭证取票）"
strIdCard2 = "取票人身份证后6位数"
for extend in extList:
    tempExtend = extend
    print (extend['key'])
    print (tempExtend['key'])
    print (tempExtend)
    if strName == tempExtend['key'] or strName.find(tempExtend['key']) > -1:
        extend['value'] = name
        # extraInfo.append = tempExtend
        # tempExtend["key"].contains(strName)
    elif strPhone == tempExtend['key'] or strPhone.find(tempExtend['key']) > -1:
        extend['value'] = phone
    elif strQQ == tempExtend['key'] or strQQ.find(tempExtend['key']) > -1:
        extend['value'] = qq
    elif strIdCard1 == tempExtend['key'] or strIdCard1.find(tempExtend['key']) > -1 or strIdCard2 == tempExtend['key'] or strIdCard2.find(tempExtend['key']) > -1:
        extend['value'] = idcard
    else:
      continue
print ('姓名+电话+qq+身份证-拼装的数据:')
print (extList)
# 耗时统计-结束时间
endTime = time.clock()
print ("消耗时间: %f s" % (endTime - startTime))
print ('\n')
print ('\n')

# 下单第二步:获得想购买的具体票
# 耗时统计-开始时间
startTime = time.clock()
# 时间戳
t = time.time()
# 填写地址信息[goodsid:具体的商品,goodspricetypeid:具体的票]
addressData ={
  "goodslist": [
    {
      "goodsid": goodsId,
      "goodspricecatelist": [
        {
          "num": 3,
          "goodspricetypeid": ticketId
        }
      ],
      "extrainfo": extList
    }
  ]
}
data={
      'cmd_s':'shop.order',
      'cmd_m':'findconfirmorderinfo',
      'userid': userid,
      'token': token,
      'apiv': '1.0.0',
      'v':'1.0',
      'requesttimestap': t,
      'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"},
      'data': addressData
      }
headers = {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8"}
#postdata=urllib.parse.urlencode(data)
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
result=requests.post(loginUrl,data=data,headers=headers)
# print (result.encoding)
# print (result.json())
print ('下单第二步, 请求的数据:')
print (data)
print ('下单第二步, 确认地址:')
print (result.text)
# 地址的id
response = json.loads(result.text)
addressId = response['data']['addressinfo']['id']
addressInfo = response['data']['addressinfo']
# 耗时统计-结束时间
endTime = time.clock()
print ("消耗时间: %f s" % (endTime - startTime))
print ('\n')
print ('\n')

# sleep一会
# print ("Start : %s" % time.ctime())
# time.sleep( 5 )
# print ("End : %s" % time.ctime())


# 下单第三步:确认订单
# 耗时统计-开始时间
startTime = time.clock()
# 时间戳
t = time.time()
# 拼接用户信息
for extend in extList:
    tempExtend = extend
    print (extend['key'])
    print (tempExtend['key'])
    print (tempExtend)
    if strName == tempExtend['key'] or strName.find(tempExtend['key']) > -1:
        extend['value'] = addressInfo['name']
        # extraInfo.append = tempExtend
        # tempExtend["key"].contains(strName)
    elif strPhone == tempExtend['key'] or strPhone.find(tempExtend['key']) > -1:
        extend['value'] = addressInfo['mobile']
    elif strQQ == tempExtend['key'] or strQQ.find(tempExtend['key']) > -1:
        extend['value'] = "408596288"
    elif strIdCard1 == tempExtend['key'] or strIdCard1.find(tempExtend['key']) > -1 or strIdCard2 == tempExtend['key'] or strIdCard2.find(tempExtend['key']) > -1:
        extend['value'] = "294112"
    else:
      continue
print ('姓名+电话+qq+身份证-拼装的数据:')
print (extList)
orderData = {
  "isshopagreement": 1,
  "goodslist": [
    {
      "goodsid": goodsId,
      "extrainfo": extList,
      "goodspricecatelist": [
        {
          "num": ticketNum,
          "goodspricetypeid": ticketId
        }
      ]
    }
  ],
  "addressid": addressId
}
data={
      'cmd_s':'shop.order',
      'cmd_m':'submitOrder',
      'userid': userid,
      'token': token,
      'apiv': '1.0.0',
      'v':'1.0',
      'requesttimestap': t,
      'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"},
      'data': orderData
      }
headers = {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8"}
#postdata=urllib.parse.urlencode(data)
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
result=requests.post(loginUrl,data=data,headers=headers)
# print (result.encoding)
# print (result.json())
print ('下单第三步, 请求的数据:')
print (orderData)
print ('下单第三步, 确认订单:')
print (result.text)
# 耗时统计-结束时间
endTime = time.clock()
print ("消耗时间: %f s" % (endTime - startTime))
print ('\n')
print ('\n')

# 结束时间
print ('总的结束时间:')
print (time.strftime('%Y-%m-%d %H:%M:%S"',time.localtime(time.time())))
# 总的耗时统计-结束时间
allEndTime = time.clock()
print ("总的消耗时间: %f s" % (allEndTime - allStartTime))



# 搜索接口
# 时间戳
# t = time.time()
# searchKeyword = '林俊杰'
# searchData = {"pagenum":"1","searchword":searchKeyword,"pagesize":"20"}
# data={
#       'cmd_s':'search',
#       'cmd_m':'search',
#       'userid': userid,
#       'token': token,
#       'apiv': '1.0.0',
#       'v':'1.0',
#       'requesttimestap': t,
#       'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"},
#       'data': searchData
#       }

# 商品详情
# 时间戳
# t = time.time()
# data={
#       'cmd_s':'shop.goods',
#       'cmd_m':'findgoodsbyid',
#       'userid': userid,
#       'token': token,
#       'apiv': '1.0.0',
#       'v':'1.0',
#       'requesttimestap': t,
#       'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"},
#       'data': {"goodsid":goodsId}
#       }

# 排行榜
# 时间戳
# t = time.time()
# data={
#       'cmd_s':'shop.goods',
#       'cmd_m':'findrankingbygoodsid',
#       'userid': userid,
#       'token': token,
#       'apiv': '1.0.0',
#       'v':'1.0',
#       'requesttimestap': t,
#       'client':{"platform":"ios","deviceid":"0A839A4E-B934-4A37-87BE-FC2E4A5DE60E","channel":"AppStore","version":"4.4.1"},
#       'data': {"goodsid":goodsId,"pagenum":"1","pagesize":"20"}
#       }
