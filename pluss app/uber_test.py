from uberpy import Uber
import pprint 
import MySQLdb
import time
con =  MySQLdb.connect('localhost','root','','uber')
client_id ='hlbRMlhkB8kxRBozHiRccnfIHv6fsJ5e'
server_token = "2H26_n81qOVOJmafk_nRjUgMqepNCnWvIr4X9o1n"
secret = '6YA8yP80GMtYbLYmZsY1oNI3fwlEEOObDiws-1-o'
uber = Uber(client_id, server_token, secret)
latitude = 51.5286416
longitude = -0.1015987

uber_products = uber.get_products(latitude, longitude)
# pprint.pprint(uber_products)

start_latitude = '28.53544'
start_longitude = '77.26393'
end_latitude = '28.45950'
end_longitude = '77.02664'

# uber.get_fare_estimate
# time_estimate = uber.get_time_estimate(start_latitude, start_longitude, customer_uuid=None, product_id=None)
fare_estimate = uber.get_price_estimate(start_latitude, start_longitude, end_latitude, end_longitude)

pprint.pprint(fare_estimate)
date = str(time.strftime('%y/%m/%d'))

price_go = [ fe['low_estimate'] for fe in fare_estimate['prices'] if fe['display_name']=='uberGO (Delhi to NCR)'][0]
# print price_go
price_x =  [ fe['low_estimate'] for fe in fare_estimate['prices'] if fe['display_name']=='uberX (Within Delhi)'][0]
# for fe in fare_estimate['prices']:
# 	low_estimate = fe['low_estimate']
# 	display_name = fe['display_name']
# 	print low_estimate
# 	print display_name
# 	print date

	# if display_name=='uberGO (Delhi to NCR)' or display_name=='uberX (Within Delhi)':
with con:
	cur = con.cursor()
	sql='INSERT INTO uber_product VALUES(0,"%s","%s","%s")'%(date,price_go,price_x)
	cur.execute(sql)
	con.commit()




# pprint.pprint(fare_estimate)
