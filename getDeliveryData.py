#!/usr/bin/python3
import requests as rq
from bs4 import BeautifulSoup as bs
import json
import datetime

#東風
DONGPOO_CUSTOMER_DATA_LINK = 'http://220.135.157.10:8088/goods_status'
DONGPOO_DELIVERY_DETAILS_LINK = 'http://220.135.157.10:8088/goods_queryGoodsStatus'
DONGPOO_ID_LENGTH = 12
class DongPoo():
	def __init__(self, deliveryId):
		self.deliveryId = str(deliveryId)
		self.handleDate = None
		self.consigneeName = None
		self.bookingDate = None
		self.realCcPrice = None
		self.details = list()

	def deliveryIdLengthIsCorrect(self):
		if (len(self.deliveryId) == DONGPOO_ID_LENGTH) and (self.deliveryId.isdigit()):
			return True
	
	def getCustomerData(self):
		response = rq.post(DONGPOO_CUSTOMER_DATA_LINK, data={'trackNo': self.deliveryId})
		if response.json() != []:
			responseData = response.json()[0]
			self.handleDate = responseData['handleDate']  # 送達日期
			self.consigneeName = responseData['consigneeName']  # 收件人
			self.bookingDate = datetime.datetime.strptime(
				responseData['bookingDate'], '%Y%m%d').strftime('%Y/%m/%d')  # 資料日期
			self.realCcPrice = responseData['realCcPrice']  # 代收款
	
	def getDetailsData(self):
		response = rq.post(DONGPOO_DELIVERY_DETAILS_LINK,
		                   data={'trackNo': self.deliveryId})
		responseDatas = response.json()
		for data in responseDatas:
			self.details.append({
				'rowNum': data['rowNum'],
				'handleDate': data['handleDate'],  # 日期
				'handleTime': data['handleTime'],  # 時間
				'remark': data['remark']  # 貨況
			})
	
	def getData(self):
		try:
			if self.deliveryIdLengthIsCorrect():
				self.getCustomerData()
				self.getDetailsData()
				return self.__dict__ if (self.handleDate != None and
									self.consigneeName != None and
									self.bookingDate != None and
									self.realCcPrice != None and
									self.details != list()) else None
		except:
			return None


# 黑貓
BLACKCAT_LINK_TEMPLATE = 'https://www.t-cat.com.tw/Inquire/TraceDetail.aspx?BillID={}&ReturnUrl=Trace.aspx'
BLACKCAT_ID_LENGTH = [10, 12]
class BlackCat():
	def __init__(self, deliveryId):
		self.deliveryId = str(deliveryId)
		self.responseData = list()

	def deliveryIdLengthIsCorrect(self):
		if (len(self.deliveryId) in BLACKCAT_ID_LENGTH) and (self.deliveryId.isdigit()):
			return True

	def getResponseData(self):
		response = rq.get(BLACKCAT_LINK_TEMPLATE.format(self.deliveryId))
		soup = bs(response.text, 'lxml')
		try:
			rows = soup.select('table.tablelist')[0].select('tr')
			for rowIndex in range(1, len(rows)):
				elementIndex = 0
				if rowIndex == 1:
					elementIndex += 1
				self.responseData.append({
					'rowNum': rowIndex,
					'status': rows[rowIndex].select('td')[elementIndex].text.strip(),
					'time': rows[rowIndex].select('td')[elementIndex + 1].text.strip(),
					'location': rows[rowIndex].select('td')[elementIndex + 2].text.strip()
				})
		except IndexError:
			pass

	def getData(self):
		try:
			if self.deliveryIdLengthIsCorrect():
				self.getResponseData()
				return self.responseData if self.responseData != list() else None
		except:
			return None


# 速力達
SKYLEADEREXPRESS_LINK_TEMPLATE = 'http://www.sldex.com/index_DetailSearchResult.php?ship_no=(%27{}%27)'
SKYLEADEREXPRESS_ID_LENGTH = 12
class SkyLeaderExpress():
	def __init__(self, deliveryId):
		self.deliveryId = str(deliveryId)
		self.responseData = list()
	
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
				self.responseData.append({
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
			return self.responseData if (self.responseData != list()) else None

class GetDeliveryData():
	def __init__(self, deliveryId):
		self.deliveryId = deliveryId
		self.skyLeaderExpress = SkyLeaderExpress(deliveryId)
		self.dongPoo = DongPoo(deliveryId)
		self.blackCat = BlackCat(deliveryId)
	
	def getDict(self):
		return {
			'deliveryId': self.deliveryId,
			'data': {
				'skyLeader': self.skyLeaderExpress.getData(),
				'dongPoo': self.dongPoo.getData(),
				'blackCat': self.blackCat.getData()
			}
		}

if __name__ == '__main__':
	# deliveryId = 900143300616
	deliveryId = 900032521962
	# print(DongPoo(deliveryId).getData())
	# print(BlackCat(deliveryId).getData())
	
	# deliveryId = 300003938454
	# print(SkyLeaderExpress(deliveryId).getData())
	print(GetDeliveryData(deliveryId).getDict())
