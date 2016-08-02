from flask import Flask, render_template, json, request
from flask import Flask, session, redirect, url_for, escape, request
from flask.ext.mysql import MySQL
import MySQLdb
import datetime 
import time

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def high(chartID = 'chart_ID'):
	print "sdsdsd",request.method
	if request.method=='POST':
	    start_date = datetime.datetime.strptime(request.form['datepicker-13'], '%m/%d/%Y').strftime('%Y-%m-%d')
	    end_date = datetime.datetime.strptime(request.form['datepicker-14'], '%m/%d/%Y').strftime('%Y-%m-%d')
	    sql = "SELECT * FROM uber_product WHERE (date BETWEEN '%s' AND '%s')"%(start_date,end_date)
	    print sql
	else:
		sql='SELECT * FROM uber_product '
		print "god"
	
 	con =  MySQLdb.connect('localhost','root','','uber')
	
	with con:
		cur = con.cursor()
		cur.execute(sql)
		rows = cur.fetchall()
		data_list = []
		for row in rows:
			data_list.append({'date':str(row[1]),'price_go':int(row[2]), 'price_x':int(row[3])})

		data_list.sort(key=lambda r: r['date'])
		print 'data_list',data_list
	if request.method=='POST':
		print "krishna"
		return render_template('graph.html', chartID=chartID, data = data_list)
	else:
		return render_template('graph1.html', chartID=chartID, data = data_list)

if __name__ == '__main__':
	app.run(debug=True)