#import requests
from bs4 import BeautifulSoup
from urllib import request
import psycopg2

#connection parameters for the Postgres DATABASE
conn_string = "host='localhost' dbname='postgres' user='postgres' password='Abhinav69'"
conn = psycopg2.connect(conn_string)
cursor =  conn.cursor()
print("connected to DB")

#Creating new table
sql = "drop table PHONE_INVENTORY;"
cursor.execute(sql)
sql = "CREATE TABLE PHONE_INVENTORY(_ID SERIAL PRIMARY KEY,_NAME VARCHAR (200),_PRICE VARCHAR (10));"
#print(sql)
cursor.execute(sql)
conn.commit()

#Search_string = input("Enter the item name : ")
#Search_string = Search_string.replace(' ','%20')

#Web scraping the data from the e-commerce website
resp = request.urlopen("https://www.flipkart.com/search?q=" + "iphone"+ "&otracker=search&otracker=start&as-show=on&as=off");
soup = BeautifulSoup(resp.read(),"html.parser")
resp.close()
ph_container = soup.find_all('div',{'class' : '_1UoZlX'})

i=0
#Loop Through Each data in top container
for phone in ph_container:
    i = i+1
    phone_soup = BeautifulSoup(phone.__str__(),"html.parser")
    #print(phone_soup.find('img',{'class':'_1Nyybr'})['alt'])
    ph_name = phone_soup.find('img',{'class':'_1Nyybr'})['alt']
    #print(phone_soup.find('div',{'class':'_1vC4OE _2rQ-NK'}).text)
    ph_price = phone_soup.find('div',{'class':'_1vC4OE _2rQ-NK'}).text
    sql = "INSERT INTO PHONE_INVENTORY (_NAME, _PRICE) VALUES ('{}','{}');".format(ph_name,ph_price)
    #print(sql)
    cursor.execute(sql)
    conn.commit()
conn.close()
