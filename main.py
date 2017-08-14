""" This is a test webdriver """
from selenium import webdriver
import csv

URL_LAZADA_VN = "http://www.lazada.vn"
URL_LAZADA_SG = "http://www.lazada.sg"
URL_LAZADA_MY = "http://www.lazada.com.my"
URL_LAZADA_PH = "http://www.lazada.com.ph"
URL_LAZADA_TH = "http://www.lazada.co.th"
URL_LAZADA_ID = "http://www.lazada.co.id"

URL_ALL_DOMAINS = [
    URL_LAZADA_VN,
    URL_LAZADA_SG,
    URL_LAZADA_MY,
    URL_LAZADA_PH,
    URL_LAZADA_TH,
    URL_LAZADA_ID
]

BROWSER = webdriver.Chrome()

for current_domain in URL_ALL_DOMAINS:
    BROWSER.get(current_domain)

BROWSER.quit()
