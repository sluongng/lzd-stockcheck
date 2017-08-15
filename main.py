""" This is a test webdriver """
from selenium import webdriver, common
# import csv

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

SAMPLE_SKU = "XI431ELAA4RBY2VNAMZ-8760830"

SEARCH_PATH = "/catalog/?q="

SAMPLE_XPATH = "//div[contains(@class, 'c-product-card__description')]/a"


class RunSelenium():
    """ RunSelenium is the main driver """
    def __init__(self):
        print("STARTING SELENIUM")
        self.browser = webdriver.Chrome()

    def is_element_present(self, locator):
        """ is_element_present blah blah """
        try:
            self.browser.find_element_by_xpath(locator)
            return True
        except common.exceptions.NoSuchElementException:
            return False

    def selenium(self):
        """ selenium blah blah """
        driver = self.browser

        for current_domain in URL_ALL_DOMAINS:
            search_url = current_domain + SEARCH_PATH + SAMPLE_SKU
            driver.get(search_url)

            if self.is_element_present(SAMPLE_XPATH):
                description = driver.find_element_by_xpath(SAMPLE_XPATH)
                print(description.get_attribute('href'))
            else:
                print('Cant find SKU = ' + SAMPLE_SKU + ' on domain ' + current_domain)

        print("STOPPING SELENIUM")
        driver.quit()

if __name__ == '__main__':
    RUN = RunSelenium()
    RUN.selenium()
