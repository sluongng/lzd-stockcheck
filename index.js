const { Builder, By, Key, until } = require('selenium-webdriver');

const URL_LAZADA_VN = "http://www.lazada.vn";
const URL_LAZADA_SG = "http://www.lazada.sg";
const URL_LAZADA_MY = "http://www.lazada.com.my";
const URL_LAZADA_PH = "http://www.lazada.com.ph";
const URL_LAZADA_TH = "http://www.lazada.co.th";
const URL_LAZADA_ID = "http://www.lazada.co.id";

const SAMPLE_SKU = "XI431ELAA4RBY2VNAMZ-8760830";

const image_link_selector = "div[class^='c-product-list'] div[class*='img-placeholder'] a";

let driver = new Builder()
    .forBrowser('chrome')
    .build();

driver.get(URL_LAZADA_VN)
    .then(_ => driver.findElement(By.css("input[class*='textbox_search']")).sendKeys(SAMPLE_SKU, Key.RETURN))
    .then(_ => driver.wait(until.titleContains(SAMPLE_SKU), 1000))
    .then(_ => driver.quit);