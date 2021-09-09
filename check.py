import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import time
import re
from datetime import datetime
import time


port = 465  # For SSL
ATT = "@mms.att.net"
Sprint = "@pm.sprint.com"
Tmobile = "@tmomail.net"
Verizon = "@vzwpix.com"

email = "" #Enter email here
password = "" #Enter password here
phone_number = "" #Enter phone number
gateway = "ATT"

# Create a secure SSL context
def_context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", port )

product = "Samsung Frame TV"
fifty = 1150
fiftyfive = 1350
sixtyfive = 1850
alert = "Price alert! An item you're monitoring has recently had a price reduction!"
url1 = "https://www.samsung.com/us/televisions-home-theater/tvs/the-frame/50-class-the-frame-tv-qled-4k-uhd-hdr-smart-tv-2020-qn50ls03tafxza/"
url2 = "https://www.samsung.com/us/televisions-home-theater/tvs/the-frame/55-class-the-frame-tv-qled-4k-uhd-hdr-smart-tv-2020-qn55ls03tafxza/"
url3 = "https://www.samsung.com/us/televisions-home-theater/tvs/the-frame/65-class-the-frame-tv-qled-4k-uhd-hdr-smart-tv-2020-qn65ls03tafxza/"
m1 = alert + " \n" + product + " \n" + url1
m2 = alert + " \n" + product + " \n" + url2
m3 = alert + " \n" + product + " \n" + url3


def get_date():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    date = now.strftime("%b-%d-%Y %H:%M")
    print("date and time: ", date)
    return date

def send_alert(email, password, phone_number, message):
    server.login(email, password)
    time.sleep(1)
    server.sendmail(email, phone_number, message)
    time.sleep(1)
    server.quit()

def frame_50():

    site = "Samsung 50\""
    url = "https://www.samsung.com/us/televisions-home-theater/tvs/the-frame/50-class-the-frame-tv-qled-4k-uhd-hdr-smart-tv-2020-qn50ls03tafxza/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    product = "Samsung Frame TV"
    m = "Price alert! An item you're monitoring has recently had a price reduction!"
    message = m + " \n" + product + " \n" + url

    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, "html.parser")
    html = soup.prettify()
    price = soup.find(class_="epp-price")
    print(price.text)

    date = get_date()
    pricelog = open("pricehistory.txt", "a")
    pricelog.write(price.text + " " + site + " " + date + "\n")
    pricelog.close()
    newprice = price.text


    p = newprice.replace(',', '')
    pt = float(p)
    return pt
    #if (pt<1290):
        #send_alert(email, password, phone_number, message)

def frame_55():

    site = "Samsung 55\""
    url = "https://www.samsung.com/us/televisions-home-theater/tvs/the-frame/55-class-the-frame-tv-qled-4k-uhd-hdr-smart-tv-2020-qn55ls03tafxza/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    product = "Samsung Frame TV"
    m = "Price alert! An item you're monitoring has recently had a price reduction!"
    message = m + " \n" + product + " \n" + url

    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, "html.parser")
    html = soup.prettify()
    price = soup.find(class_="epp-price")
    print(price.text)

    date = get_date()
    pricelog = open("pricehistory.txt", "a")
    pricelog.write(price.text + " " + site + " " + date + "\n")
    pricelog.close()
    newprice = price.text


    p = newprice.replace(',', '')
    pt = float(p)
    return pt
    #if (pt<1490):
        #send_alert(email, password, phone_number, message)

def frame_65():

    site = "Samsung 65\""
    url = "https://www.samsung.com/us/televisions-home-theater/tvs/the-frame/65-class-the-frame-tv-qled-4k-uhd-hdr-smart-tv-2020-qn65ls03tafxza/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    product = "Samsung Frame TV"
    m = "Price alert! An item you're monitoring has recently had a price reduction!"
    message = m + " \n" + product + " \n" + url

    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, "html.parser")
    html = soup.prettify()
    price = soup.find(class_="epp-price")
    print(price.text)

    date = get_date()
    pricelog = open("pricehistory.txt", "a")
    pricelog.write(price.text + " " + site + " " + date + "\n")
    pricelog.close()
    newprice = price.text


    p = newprice.replace(',', '')
    pt = float(p)
    return pt
    #if (pt<1990)
        #send_alert(email, password, phone_number, message)

server.login(email, password)
time.sleep(1)
if (frame_50()<fifty):
    #send_alert(email, password, phone_number, m1)
    server.sendmail(email, phone_number, m1)
if (frame_55()<fiftyfive):
    server.sendmail(email, phone_number, m2)
if (frame_65()<sixtyfive):
    server.sendmail(email, phone_number, m3)

time.sleep(1)
server.quit()
