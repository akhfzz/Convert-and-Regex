import pandas as pd 
import mysql.connector as sql
import json
import collections

conn = sql.connect(user='root', password='',
                              host='localhost',database='myapp')
mydict = {}
select_employee = """SELECT * FROM admin_app"""
cursor = conn.cursor()
cursor.execute(select_employee)
result = cursor.fetchall()

rowarray_list = []
for row in result:
	t = (row[0], row[1], row[2], row[3], row[4], row[5])
	rowarray_list.append(t)
j = json.dumps(rowarray_list)
with open("app.json", "w") as f:
	f.write(j)
# Convert query to objects of key-value pairs
objects_list = []
for row in result:
	d = collections.OrderedDict()
	d["id_admin"] = row[0]
	d["Nama"] = row[1]
	d["Password"] = row[2]
	d["Gen"] = row[3]
	d["Jenis_Penjualan"] = row[4]
	d["no_telp"] = row[5]
	objects_list.append(d)
j = json.dumps(objects_list)
with open("app.json", "w") as f:
	f.write(j)
