import re
from urllib.request import urlopen 
import json

def regex(content,url):
	regular = re.findall("[A-Z]{2,3}",content) #untuk singkatan nama kampus
	ekspresion = re.findall("[A-Z]+nivers....+[A-Z][a-z]{4,8}.....",content) #untuk mencari nama kampus
	regex = re.findall("[a-z]{3,5}[:]//[a-z]{3,9}.+[.][a-z]{2,3}",url)#untuk regex url
	return ekspresion,regular,regex

def regularex(url):
	nama_link = urlopen(url)
	output = str(nama_link.read())
	baca_expresion = re.findall("http[s][:]//+[\w\.][a-z]{2,7}.[A-Za-z0-9]{2,8}[\.][a-z]{2,3}.[\w\.]..[A-Za-z0-9]{2,9}",output)
	return baca_expresion
print(regex("""Berikut ini beberapa nama-nama universitas di Indonesia: Universitas Indonesia (UI),
		Institut Teknologi Bandung (ITB),Universitas Sebelas Maret (UNS), Universitas Gajah Mada (UGM)""","http://petanikode.com"))
print(regularex("http://rosihanari.net"))