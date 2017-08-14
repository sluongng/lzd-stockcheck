""" This is a test webdriver """
from selenium import webdriver
import csv

URL_LAZADA_VN = "http://www.lazada.vn"
URL_LAZADA_SG = "http://www.lazada.sg"
URL_LAZADA_MY = "http://www.lazada.com.my"
URL_LAZADA_TH = "http://www.lazada.co.th"
URL_LAZADA_PH = "http://www.lazada.co.ph"
URL_LAZADA_ID = "http://www.lazada.co.id"



BROWSER = webdriver.Chrome()
BROWSER.get(URL_LAZADA_VN)

BROWSER.quit()
