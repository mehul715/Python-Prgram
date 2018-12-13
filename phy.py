import sys
import xml.dom.minidom
import mysql.connector


cnx = mysql.connector.connect(host='localhost', user='root', password='xxx', database='demo')
cursor = cnx.cursor()
cursor.execute("DROP TABLE IF EXISTS nyexchange")
cursor.execute("CREATE TABLE nyexchange( exchange VARCHAR(50), symbol VARCHAR(50), company VARCHAR(100), volume INT(25), price DECIMAL(5,2), change1 DECIMAL(5,2))")
document = xml.dom.minidom.parse(sys.argv[1])
tableElements = document.getElementsByTagName('table')
#print("exchange,symbol,company,volume,price,change")
for tr in tableElements[2].getElementsByTagName('tr'):
	data = []
	for td in tr.getElementsByTagName('td'):
		for node in td.childNodes:
			if node.nodeType == node.TEXT_NODE:
				data.append(node.nodeValue.strip().strip('$').replace(',', ''))
			else:
				for s in node.childNodes[0].nodeValue.strip().rsplit(None, 1):
					data.append(s.strip().strip("(),").replace(",", ' '))
	datax=[]
	for x in data[2:3]:
		y=x.replace("'"," ")
		datax.append(y)

	if data[0].isdecimal():
		#print(','.join(['NYSE'] + data[3:4] + data[2:3] + data[5:8]))
	
		def insert(cursor):
   			query = ("INSERT INTO nyexchange(exchange, symbol,company,volume,price,change1) VALUES ('%s','%s','%s','%s','%s','%s')" %("NYSE",data[3:4][0],datax[0],data[5:6][0],data[6:7][0],data[7:8][0]))
  		 	cursor.execute(query)
		try:
		    
		    cnx = mysql.connector.connect(host='localhost', user='root', password='xxx', database='demo')
		    cursor = cnx.cursor()
		    
		    insert(cursor)
		    cnx.commit()

		   # update(cursor)
		    #cnx.commit()
		    
		    cursor.close()
		except mysql.connector.Error as err:
		    print(err)
		finally:
		    cnx.close()
	
print("Table is inserted")		
