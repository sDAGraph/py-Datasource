import binascii
import pymongo
import json
import sys
import time
from bson.objectid import ObjectId
class MongoOrder():
	def __init__(self,db,col):
		self.client = pymongo.MongoClient("mongodb://192.168.51.202:27017")
		self.col = self.Connect(db,col)
	def Connect(self,db,col):
		mydb = self.client[db]
		mycol = mydb[col]
		return mycol
	def AddOrder(self, order):
		x = self.col.insert_one(order) 
	def UpdateFieldByExchange(self,exchange,data):
		myquery = {'exchange':exchange}
		newvalues =  { "$set":data}
		result = self.col.update_one(myquery, newvalues,upsert=True)
		return result
#UpdateFieldById(self,field,id,value):
#test = MongoOrder()
#client = test.client
test = MongoOrder('trade','place_order')
# test.UpdateFieldById('price',3100,'c87ebf6b-1385-2fec-c2ea-0e8c2c8df9d6')

#test.PlaceAllOrder(col)
#test.Update('price',344,col,'5c90c2bffa59b01a97820833')
#mydict = {"market" : "ETHUSD", "orderside" : "Sell", "volume" : 1, "price" : 234, "ordertype" : "limit",'status':1 }

# myquery = {'_id':ObjectId("5c90ae4ca4ece03e334ba868")}
# newvalues =  { "$set":{"market" : "ETHUSD", "orderside" : "Sell", "volume" : 1, "price" : 234, "ordertype" : "limit",'status':1,'exchange':'bitmex' } }
 
# col.update_one(myquery, newvalues)
#x = col.update()
#x = col.insert_one(mydict) 
#for post in result.find():
#	print (post)
#x = MongoOperations()
#d = x.Update({'id': 27380768},{'state': "cancel"}, "trade", "tradeGo")

