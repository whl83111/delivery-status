#!/usr/bin/python3
import requests as rq
from bs4 import BeautifulSoup as bs
import json
import datetime

#東風
class DongPoo():
	def __init__(self, deliveryId):
		self.deliveryId = deliveryId

	def getResponse(self):
		pass


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
				'nowNum' : i,
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


# 速力達
SKYLEADEREXPRESS_LINK_TEMPLATE = 'http://www.sldex.com/index_DetailSearchResult.php?ship_no=(%27{}%27)'
SKYLEADEREXPRESS_ID_LENGTH = 12
class SkyLeaderExpress():
	def __init__(self, deliveryId):
		self.deliveryId = str(deliveryId)
		self.responseData = {
			'deliveryId': deliveryId,
			'data': list()
		}
	
	def deliveryIdLengthIsCorrect(self):
		if (len(self.deliveryId) == SKYLEADEREXPRESS_ID_LENGTH) and (self.deliveryId.isdigit()):
			return True

	def getResponse(self):
		response = rq.get(SKYLEADEREXPRESS_LINK_TEMPLATE.format(self.deliveryId))
		response.encoding = 'UTF-8'
		soup = bs(response.text, 'lxml')
		responseTable = soup.select('div.alert.alert-danger')[0].select('b')
		responseDeliveryId = responseTable[0].text
		responseDatas = [data.text.split('·') for data in responseTable[1:]]
		if responseDeliveryId == self.deliveryId:
			for data in responseDatas:
				self.responseData['data'].append({
					'time': data[0],
					'status': data[1]
				})

	def getData(self):
		try:
			if self.deliveryIdLengthIsCorrect():
				self.getResponse()
		except:
			pass
		finally:
			return self.responseData

if __name__ == '__main__':
	# deliveryId = 900032521962
	# print(getDongPoo(deliveryId))
	# print(getBlackCat(deliveryId))
	slid = 300003938454
	print(SkyLeaderExpress(slid).getData())

