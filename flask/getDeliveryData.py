#!/usr/bin/python3
import requests as rq
from bs4 import BeautifulSoup as bs
import json
import datetime

def checkDeliveryIdForm(deliveryId):
	return True

def getDongPoo(deliveryId):
	link = 'http://220.135.157.10:8088/goods_status'
	postData = {'trackNo' : deliveryId}
	response = rq.post(link, data = postData)
	targetData = {}
	if response.json() != []:
		temp = response.json()[0]
		link2 = 'http://220.135.157.10:8088/goods_queryGoodsStatus'
		response2 = rq.post(link2, data = postData)
		temp2 = response2.json()
		targetData = {
			'deliveryId' : deliveryId,
			'handleDate' : temp['handleDate'], # 送達日期
			'consigneeName' : temp['consigneeName'], # 收件人
			'bookingDate' : datetime.datetime.strptime(temp['bookingDate'], '%Y%m%d').strftime('%Y/%m/%d'), # 資料日期
			'realCcPrice' : temp['realCcPrice'], # 代收款
		}
		targetData['details'] = []
		for data in temp2:
			data_temp = {
				'rowNum' : data['rowNum'],
				'handleDate' : data['handleDate'], # 日期
				'handleTime' : data['handleTime'], # 時間
				'remark' : data['remark'] # 貨況
			}
			targetData['details'].append(data_temp)
		targetData['expired'] = False
	else:
		targetData['deliveryId'] = deliveryId
		targetData['expired'] = True
	return targetData

def getBlackCat(deliveryId):
	link = 'https://www.t-cat.com.tw/Inquire/TraceDetail.aspx?BillID={}&ReturnUrl=Trace.aspx'.format(deliveryId)
	response = rq.get(link)
	# print(link)
	soup = bs(response.text, 'lxml')
	targetData = {'rows' : [], 'deliveryId' : deliveryId}
	try:
		rows = soup.select('table.tablelist')[0].select('tr')
		for i in range(1, len(rows)):
			j = 0
			if i == 1:
				j += 1
			targetData['rows'].append({
				'status' : rows[i].select('td')[j].text.strip(),
				'time' : rows[i].select('td')[j + 1].text.strip(),
				'location' : rows[i].select('td')[j + 2].text.strip()
			})
	except:
		targetData['error'] = True
	if targetData['rows'] == []:
		targetData['expired'] = True
	else:
		targetData['expired'] = False
	return targetData

if __name__ == '__main__':
	deliveryId = 900032521962
	print(getDongPoo(deliveryId))
	print(getBlackCat(deliveryId))