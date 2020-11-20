import json
import openpyxl
import pandas as pd 
from urllib.request import urlopen
from sqlalchemy import create_engine
import mysql.connector as sql


file_nama = urlopen("https://jsonplaceholder.typicode.com/users")
load = json.loads(file_nama.read())

def WritetoJson(file):
	global file_nama,load
	with open(file,"w") as room:
		taked = json.dump(load,room)
		print(taked)

def JsontoExcel(file):
	global file_nama,load
	read_file= pd.read_json(file)
	read_file.to_excel("e:\\latihan pemrograman\objektif.xlsx")
	print(read_file)

def ExceltoDatabase(file):
	global file_nama,load
	database = sql.connect(host="localhost",database="",user="Akhfzz",password="kertosari23")
	kurs = database.cursor()
	make = """CREATE DATABASE Convertation"""
	kurs.execute(make)
	file_excel = pd.read_excel("e:\\latihan pemrograman\gesampel.xls")
	engine = create_engine("file")
	file_excel.to_sql("Penjualan",con=engine)
	print(file_excel)
WritetoJson("e:\\latihan pemrograman\marks.json")
JsontoExcel("e:\\latihan pemrograman\marks.json")
ExceltoDatabase("mysql://Akhfzz:kertosari23@localhost/Convertation")