#!/usr/bin/env python
#import os
#import time
#import logging
import csv 
import os
import time
import logging
import MySQLdb
import sqlite3
#from tomlkit import datetime
from datetime import datetime
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
import tornado.escape
import smtplib
import codecs
from smtplib import SMTP, SMTPException
from io import StringIO
#from PIL import Image
import profile as profile
import urllib
import wget
import shutil
# *******
import bcrypt
import concurrent.futures
#import MySQLdb
import markdown
import pymysql
import os.path
import re
import subprocess

import tornado.escape
from datetime import datetime
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import os.path, random, string
from tornado.options import define, options
# *******
from tornado import gen
import pymysql.cursors
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.websocket import WebSocketHandler
from tornado.options import define, options
class Connect:
   
    define("mysql_host", default="carlozanieri.it", help="carlozanieri database host")
    define("mysql_database", default="carlozanieri", help="carlozanieri database name")
    define("mysql_user", default="root", help="carlozanieri database user")
    define("mysql_password", default="trex39", help="carlozanieri database password")

    def get(sbarcode):
        barcodes = str(sbarcode)
        print(b"abcde".decode("utf-8"))
        print(bytes(barcodes, "utf-8").decode("utf-8"))

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        #b = bytes(barcodes, "utf-8").decode("utf-8")
        b = "pppp"
        print(b"ppp".decode("utf-8"))
        cursor = db.cursor()
        cursor.execute("SELECT *  from barcode where barcode = %s", b)

        barcode = cursor.fetchone()
       # if not barcode: raise tornado.web.HTTPError()
        #print( str(barcode['barcode']))
        #for centralinos in barcode:
        #print(barcode['nome'])
        return barcode
    def feed(sbarcode):
        import feedparser
        rss = Connect.rss("")
        for rssm in rss:
            d = [feedparser.parse(rssm['link'])]
            for post in d.entries:
                print(post.title + ": " + post.link + "       ")
            return d
    def rss(self):

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from feed  order by id asc")

        rss = cursor.fetchall()

        return rss

    def pdf(self):

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from primanota where id >= 13 and id <= 17 order by id asc")

        pdf = cursor.fetchall()

        return pdf

    def primanota(self, id):

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT *  from primanota where data='" + id + "'" )

        primanota = cursor.fetchall()
        #primanota = primanota[1]["descrizione"]
        return primanota

    def tab_primanota(self,datada, dataa):
        print(datada)
        print(dataa)
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
       ##### db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
       ##### db = pymysql.connect("carlozanieri.net", "root", "trex39", "prolocogest", cursorclass=pymysql.cursors.DictCursor)
        print(dataa)
        print(datada)
        cursor = db.cursor()

        cursor.execute("SELECT *  from primanota where data >='" + datada + "' and data <='" + dataa + "'" + " order by data")
        ## cursor.execute("SELECT *  from primanota")
        #print(datada, dataa)
        primanota = cursor.fetchall()
        #print(primanota)
        return primanota

    def conta(self, datada,dataa):
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        #db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT *  from primanota where data >='" + datada + "' and data <='" + dataa + "'" + " order by data")
        ## cursor.execute("SELECT *  from primanota")
        conta= cursor.rowcount
        #primanota = cursor.fetchall()
        #primanota = primanota[1]["descrizione"]
        print(conta)
        return conta

    def menu(self):

        ###db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)

        ###cursor = db.cursor()
        ###cursor.execute("SELECT *  from menuweb where livello=2")
        conn = sqlite3.connect("carlozanieri.db")
        ###cursor = db.cursor()
        ###cursor.execute("SELECT *  from menuweb where livello=2")
        data = conn.execute("SELECT *  from menuweb where livello=2");  
        rows = data.fetchall()
        #rows = cursor.fetchall()
        menu = [dict(id=row[0], codice=row[1],radice=row[2], titolo=row[4], link=row[6]) for row in rows]
        #menu = primanota[1]["descrizione"]
        return menu

    def submenu(self, menu):
        conn = sqlite3.connect("carlozanieri.db")
        #db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        #cursor = db.cursor()
        data = conn.execute("SELECT *  from menuweb where livello=3 and radice = '" + menu + "'")
        #cursor.execute("SELECT *  from menuweb where livello=3 and radice = '" + menu + "'")

        submenu = data.fetchall()
        #menu = primanota[1]["descrizione"]
        return submenu
    def submnu(self):
        conn = sqlite3.connect("carlozanieri.db")
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from menuweb where livello=3 ")
        data = conn.execute("SELECT *  from menuweb where livello=3 ")
        rows = data.fetchall()
        submenu = [dict(id=row[0], codice=row[1],radice=row[2], titolo=row[4], link=row[6]) for row in rows]
        return submenu
    def submnu2(self):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from menuweb where livello=4 ")

        rows = cursor.fetchall()
        submenu2 = [dict(id=row[0], radice=row[2], titolo=row[4], link=row[6]) for row in rows]
        return submenu2
    def body(self, pagina):
        conn = sqlite3.connect("carlozanieri.db")
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from entries where slug = '" + pagina + "'")
        data = conn.execute("SELECT *  from entries where slug = '" + pagina + "'")
        body = data.fetchone()
        #menu = primanota[1]["descrizione"]
        return body
    def slider(self, luogo):
        conn = sqlite3.connect("carlozanieri.db")
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        data = conn.execute("SELECT *  from slider where codice = '" + luogo + "'")
        #cursor.execute("SELECT *  from slider where codice = '" + luogo + "'")
        ##cursor.execute("SELECT *  from slider")
        slider = data.fetchall()
        #menu = primanota[1]["descrizione"]
        return slider

    def news(self):
        data =datetime.now()
        conn = sqlite3.connect("carlozanieri.db")
        #data = "2021-06-08 00:00:00"
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        dati = conn.execute("SELECT *  from news")
        cursor = db.cursor()
        ##cursor.execute("SELECT *  from news where published <= '" + str(data) + "'")
        cursor.execute("SELECT *  from news")
        ##cursor.execute("SELECT *  from slider")
        rows = dati.fetchall()
        
        news = [dict(id=row[0], title=row[2], dir=row[8], img=row[7], html=row[4], html2=row[9], date=row[6]) for row in rows]
        # menu = primanota[1]["descrizione"]
        return news

    def products(self):
        data =datetime.now()
        conn = sqlite3.connect("carlozanieri.db")
        
        #cursor = db.cursor()
        
        #cursor.execute("SELECT *  from product")
        data = conn.execute("SELECT *  from product")
        ##cursor.execute("SELECT *  from slider")
        rows = data.fetchall()
        products = [dict(id=row[0], title=row[1], img=row[2], price=row[3], description=row[4]) for row in rows]
        # menu = primanota[1]["descrizione"]
        return products

    def bicisgrana(self):
        data =datetime.now()
        conn = sqlite3.connect("bicisgrana")
        
        #cursor = db.cursor()
        
        #cursor.execute("SELECT *  from product")
        data = conn.execute("SELECT *  from Contacts")
        ##cursor.execute("SELECT *  from slider")
        rows = data.fetchall()
        bicisgrana = [dict(id=row[0], username=row[1], useremail=row[2], telefono=row[3], indirizzo=row[4], comune=row[5] ,cap=row[6], provincia=row[7], bikesino=row[8], tipobici=row[9], noleggiare=row[10]) for row in rows]
        # menu = primanota[1]["descrizione"]
        return bicisgrana

    def creacsv(self):
        import csv 

      #  mydict =[{'name': 'Kelvin Gates', 'age': '19', 'country': 'USA'}, 
      #   {'name': 'Blessing Iroko', 'age': '25', 'country': 'Nigeria'}, 
      #   {'name': 'Idong Essien', 'age': '42', 'country': 'Ghana'}]

        fields = ['nome', 'E-Mail', 'telefono', 'indirizzo', 'comune', 'CAP'] 
        lista = Connect.bicisgrana("")
        with open('lista_partecipantis3.csv', 'w', newline='') as file: 
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
           
            for listas in lista:
                mydict = [{'nome': listas['username'], 'E-Mail': listas['useremail'], 'telefono': listas['telefono']}, {'indirizzo': listas['indirizzo'], 'comune': listas['comune'], 'CAP': listas['cap']}]
                writer.writerows(mydict)
           # lista=Connect.download("")
           # Import the necessary libraries
        import openpyxl
        import pandas as pd

        # Create a new Excel workbook
        workbook = openpyxl.Workbook()
        # Select the default sheet (usually named 'Sheet')
        sheet = workbook.active
        # Add data to the Excel sheet
        data = ['nome', 'E-Mail', 'telefono', 'indirizzo', 'comune', 'CAP']
        sheet.append(data)
        for listas in lista:
            mydict = [listas['username'],  listas['useremail'], listas['telefono'], listas['indirizzo'], listas['comune'], listas['cap']]
            sheet.append(mydict)
            # Save the workbook to a file
            workbook.save("my_excel_file.xlsx")
            # Print a success message
            print("Excel file created successfully!")
        return lista
    
    def download(self):
        #import shutil
        import requests
        
        url = 'http://carlozanieri.it/home/carlo/Scaricati/lista_partecipantis3.csv'
        response = requests.get(url, stream=True)
        #file = requests.get(url, stream=True)
        local_path = os.path.abspath("/home/carlo/Scaricati/lista_partecipantis3.csv")
        #global dump
        #dump = file.raw
        #location = os.path.abspath("/home/carlo/Scaricati/lista_partecipantis2.csv")
        with open(local_path, 'wb') as f:
            f.write(response.content)
            #shutil.copyfileobj(dump, location)
        #del dump


       # with open('/home/carlo/Scaricati/lista_partecipantis2.csv', 'wb') as out_file:
        #    shutil.copyfileobj(response.raw, out_file)

           # print('The file was saved successfully')

    def blog(self):
        data =datetime.now()
        conn = sqlite3.connect("carlozanieri.db")
        #data = "2021-06-08 00:00:00"
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        ##cursor.execute("SELECT *  from blog where published <= '" + str(data) + "'")
        cursor.execute("SELECT *  from blog")
        data = conn.execute("SELECT *  from blog")
        ##cursor.execute("SELECT *  from slider")
        rows = data.fetchall()
        blogs = [dict(id=row[0], title=row[2], dir=row[8], img=row[7], html=row[4], html2=row[9],date=row[6]) for row in rows]
        # menu = primanota[1]["descrizione"]
        return blogs
    
    def blogs_one(self, id):
        #data = date.today().strftime("%Y-%m-%d %H:%M:%S")
        #data = "2021-06-08 00:00:00"
        ##titolo=titolo
        conn = sqlite3.connect("carlozanieri.db")
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(titolo)
        #cursor = db.cursor()
        ####cursor.execute("SELECT *  from blog where id = 3")
        data = conn.execute("SELECT *  from blog where id ='" + id + "'" )
        #cursor.execute("SELECT *  from blog where id ='" + id + "'" )
        ##cursor.execute("SELECT *  from slider")
        ##news = cursor.fetchall()
        rows = data.fetchall()
        blogs = [dict(id=row[0], title=row[2], dir=row[9], img=row[7], html=row[4], date=row[6]) for row in rows]
        return blogs
    
    def news_one(self, titolo, id):
        #data = date.today().strftime("%Y-%m-%d %H:%M:%S")
        #data = "2021-06-08 00:00:00"
        ##titolo=titolo
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(titolo)
        cursor = db.cursor()
        ####cursor.execute("SELECT *  from news where id = 3")
        cursor.execute("SELECT *  from news where id = '" + id + "'")
        ##cursor.execute("SELECT *  from slider")
        ##news = cursor.fetchall()
        rows = cursor.fetchall()
        news = [dict(id=row[0], title=row[3], dir=row[9], img=row[7], html=row[5], date=row[6]) for row in rows]
        return news
    def add_cart1(self, id, titolo):
        
        conn = sqlite3.connect("carlozanieri.db")
        c = conn.cursor()
        c.execute('''INSERT INTO cart (email, address, mobile, order_date, status, customer_id, product_id) VALUES('carlo.zanieri@gmail.com', '', '', '', '', 0, 0)''' )
        
        conn.commit
        conn.close

    def add_cart(self, id, titolo):

        db = sqlite3.connect("carlozanieri.db")
        mycursor = db.cursor()
        data=str(datetime.now())
        riga="INSERT INTO cart (email, address, mobile, order_date, status, customer_id, product_id) VALUES(?, ?, ?,?, ?,?, ?)"
        valori = ('carlo.zanieri@gmail.com', '', '', '', '', 0, 0)
        mycursor.execute(riga, valori)
        args = (data, data)
        #mycursor.execute(insertQuery)
  
        print("No of Record Inserted :", mycursor.rowcount)
  
        # we can use the id to refer to that row later.
        print("Inserted Id :", mycursor.lastrowid)
  
        # To ensure the Data Insertion, commit database.
        db.commit() 
  
        # close the Connection
        db.close()

    def manifesta(self):
        data = date.today().strftime("%Y-%m-%d %H:%M:%S")
        #data="2021-06-08 00:00:00"
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(menu)
        cursor = db.cursor()
        cursor.execute("SELECT *  from manifestazioni where published >= '" + data + "'")
        ##cursor.execute("SELECT *  from slider")
        rows = cursor.fetchall()
        manifesta = [dict(id=row[0], title=row[3], html=row[5], date=row[6], dir=row[9], img=row[8]) for row in rows]
        return manifesta

    def manifesta_one(self, titolo, id):
        data = date.today().strftime("%Y-%m-%d %H:%M:%S")
        #data = "2021-06-08 00:00:00"
        ##titolo=titolo
        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        ##print(titolo)
        cursor = db.cursor()
        ####cursor.execute("SELECT *  from news where id = 3")
        cursor.execute("SELECT *  from manifestazioni where id = '" + id + "'")
        ##cursor.execute("SELECT *  from slider")
        rows = cursor.fetchall()
        manifesta = [dict(id=row[0], title=row[3], dir=row[9], img=row[8], html=row[5], date=row[6]) for row in rows]
        # menu = primanota[1]["descrizione"]
        return manifesta

    def ins_manifesta(self, dir, file, titolo, descrizione):

        db = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database)
        mycursor = db.cursor()
        data=str(datetime.now())
        riga="INSERT INTO manifestazioni (id,author_id,title, markdown, html, img, dir, html2, html3, img2,img3) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
        valori = (0,2,titolo,descrizione,descrizione,file,dir,'html2','html3','img2','img3')
        mycursor.execute(riga, valori)
        args = (data, data)
        #mycursor.execute(insertQuery)
  
        print("No of Record Inserted :", mycursor.rowcount)
  
        # we can use the id to refer to that row later.
        print("Inserted Id :", mycursor.lastrowid)
  
        # To ensure the Data Insertion, commit database.
        db.commit() 
  
        # close the Connection
        db.close()
    
    def ins_news(self, dir, file, titolo, descrizione, tipo):

        db = sqlite3.connect("carlozanieri.db")
        mycursor = db.cursor()
        data=str(datetime.now())
        riga="INSERT INTO news (id,author_id,title, markdown, html, img, dir, html2, html3, img2,img3) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?)"
        valori = (0,2,titolo,descrizione,descrizione,file,dir,'html2','html3','img2','img3')
        mycursor.execute(riga, valori)
        args = (data, data)
        #mycursor.execute(insertQuery)
  
        print("No of Record Inserted :", mycursor.rowcount)
  
        # we can use the id to refer to that row later.
        print("Inserted Id :", mycursor.lastrowid)
  
        # To ensure the Data Insertion, commit database.
        db.commit() 
  
        # close the Connection
        db.close()
    
    def ins_iscrizioni(self, username, useremail,indirizzo,comune,cap,provincia,bikesino, telefono, noleggiare, tipobici):

        db = sqlite3.connect("bicisgrana")
        mycursor = db.cursor()
        data = str(datetime.now())
        
        riga = "INSERT INTO Contacts (username, useremail,indirizzo,comune,cap,provincia,telefono,bikesino, noleggiare, tipobici) VALUES (?,?,?,?,?,?,?,?,?,?)"
        valori = (username, useremail,indirizzo,comune,cap,provincia, bikesino, telefono, noleggiare, tipobici)
        mycursor.execute(riga, valori)
        args = (data, data)
        #mycursor.execute(insertQuery)
  
        print("No of Record Inserted :", mycursor.rowcount)
  
        # we can use the id to refer to that row later.
        print("Inserted Id :", mycursor.lastrowid)
  
        # To ensure the Data Insertion, commit database.
        db.commit() 
  
        # close the Connection
        db.close()

    def get_class(kls):
        parts = kls.split('.')
        function = ".".join(parts[:-1])
        m = __import__(function)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m
    
    def get_class(kls):
        parts = kls.split('.')
        function = ".".join(parts[:-1])
        m = __import__(function)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m



        # read image as grey scale
        img = cv2.imread('D:/image-1.png')

        # do some transformations on img

        # save matrix/array as image file
        isWritten = cv2.imwrite('D:/image-2.png', img)

        if isWritten:
            print('Image is successfully saved as file.')