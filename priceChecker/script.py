import smtplib
import time
import requests as rq
from bs4 import BeautifulSoup


class PriceChecker:    
    def __init__(self,url,expectedPrice,emailId):
        self.__site = url
        self.__expectedPrice = expectedPrice
        self.__emailToSend = emailId
    
    def get_price(self):
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        html = rq.get(self.__site, headers=header).text
        soup = BeautifulSoup(html, 'html.parser')
        price = soup.findAll('div', {'id': 'price'})
        price = [i.get_text() for i in soup.find_all('span', {'class': 'a-size-medium a-color-price priceBlockBuyingPriceString'})]
        print(price)
        final_price = ''.join(price)[2:8]
        print(final_price)
        final_price = int(final_price.replace(',', ''))
        if final_price <= self.__expectedPrice:
            send_email)
    def send_email()
        # TODO
        print("Sending email to "+str(self.__emailId))


if __name__ =="__main__":
    site = "https://www.amazon.in/gp/product/B07GW23M7T/ref=ox_sc_saved_title_5?smid=A14CZOWI0VEHLG&psc=1"
    expPrice = 300000
    emailId = "self@example.com"
    object = PriceChecker(site,expPrice,emailId)
    object.get_price()
