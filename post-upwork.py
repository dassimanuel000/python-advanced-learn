from cgi import test
import email
import random
from logging import exception
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc

################

from fp.fp import FreeProxy
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import html2text
from datetime import datetime
from os.path import exists
# pour colorer les prints
from colorama import Fore
from colorama import Style
from urllib.parse import ParseResult, urlparse

# pour colorer les prints
import colorama
import os
import os.path
import re
import time
import json
import pymongo
import json
from pymongo import MongoClient
from pprint import pprint
import urllib.request
from urllib.parse import ParseResult, urlparse
import pandas as pd

from googletrans import Translator
translator = Translator()
import html








def scroll_function(i):
    height = i * 1000
    time.sleep(1.3)
    driver.execute_script("window.scrollTo("+ str(height) +", "+ str(height) +")")
    time.sleep(1.3)
    
# fonction pour donner du délai et cliquer les xpath
def waitBeforeClickOnXpath(driver, xPath):
    time.sleep(1)
    print("clicking on " + xPath + "...")
    button = driver.find_element(By.XPATH, xPath)
    driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    print("Continue the script")

def waitBeforeClickOnClass(driver, className):
    print("waiting page loading")
    time.sleep(3)
    print("clicking on " + className + "...")
    button = driver.find_element(By.CLASS_NAME, className)
    driver.execute_script("arguments[0].click();", button)
    print("button clicked")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def waitBeforeClickOnId(driver, id):
    print("waiting page loading")
    time.sleep(3)
    print("clicking on " + id + "...")
    button = driver.find_element(By.ID, id)
    driver.execute_script("arguments[0].click();", button)
    print("button clicked")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

# rempli de texte la case formulaire avec l'id correspondant
def fillById(driver, id, filler):
    print("waiting page loading")
    time.sleep(3)
    driver.find_element(By.ID, id).send_keys(filler)
    print("form filled")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def fillByIdWithSteps(driver, id ,filler):
    print("waiting page loading")
    time.sleep(3)
    driver.find_element(By.ID, id).send_keys(Keys.CONTROL + "a")
    print("Taking all that already exist")
    time.sleep(1)
    driver.find_element(By.ID, id).send_keys(Keys.DELETE)
    print("Cleaning")
    time.sleep(1)
    driver.find_element(By.ID, id).send_keys(filler)
    print("Fill with our value")
    time.sleep(1)
    print("Complete")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def fillByClass(driver, clss ,filler):
    print("waiting page loading")
    time.sleep(3)
    element = driver.find_element_by_class_name(clss).click()
    time.sleep(1)
    element.send_keys(filler)
    print("Fill with our value")
    time.sleep(1)
    print("Complete")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def fillByXpath(driver, xpath, filler):
    print("waiting page loading")
    time.sleep(3)
    driver.find_element(By.XPATH, xpath).send_keys(filler)
    print("form filled")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def tryAndRetryClickXpath(driver, xPath):
    try : 
        waitBeforeClickOnXpath(driver, xPath)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(10)
        waitBeforeClickOnXpath(driver, xPath)

def tryAndRetryClickClassName(class_name):
    try : 
        waitBeforeClickOnClass(class_name)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(10)
        waitBeforeClickOnClass(class_name)

def tryAndRetryClickID(driver, id):
    try : 
        waitBeforeClickOnClass(driver, id)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(10)
        waitBeforeClickOnClass(driver, id)


def tryAndRetryFillById(driver, id, value):
    try:
        fillById(driver,id, value)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(10)
        fillById(driver,id, value)

def tryAndRetryFillByIdWithSteps(driver, idStep1, id, value):
    try:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        fillById(id, value)
    except NoSuchElementException:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        print("the element needs to be charged...")
        time.sleep(10)
        fillById(id, value)
    except ElementNotInteractableException:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        print("the element needs to be charged...")
        time.sleep(10)
        fillById(id, value)

def writeLetterByLetterId(driver, id, word):
    print("waiting page loading")
    time.sleep(3)
    driver.find_element(By.ID, id).send_keys(Keys.CONTROL + "a")
    print("Taking all that already exist")
    time.sleep(1)
    driver.find_element(By.ID, id).send_keys(Keys.DELETE)
    print("Cleaning")
    for i in word:
        driver.find_element(By.ID, id).send_keys(i)
        
def getinnertextXpath(driver, xPath):
    try:
        result = " "
        result = driver.find_element(By.XPATH, xPath)
        result = (result.get_attribute('innerText'))
    except NoSuchElementException:  #spelling error making this code not work as expected
        result = ' '
        pass
    return str(result)

JS_DROP_FILE = """
    var target = arguments[0],
        offsetX = arguments[1],
        offsetY = arguments[2],
        document = target.ownerDocument || document,
        window = document.defaultView || window;

    var input = document.createElement('INPUT');
    input.type = 'file';
    input.onchange = function () {
      var rect = target.getBoundingClientRect(),
          x = rect.left + (offsetX || (rect.width >> 1)),
          y = rect.top + (offsetY || (rect.height >> 1)),
          dataTransfer = { files: this.files };

      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        var evt = document.createEvent('MouseEvent');
        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        evt.dataTransfer = dataTransfer;
        target.dispatchEvent(evt);
      });

      setTimeout(function () { document.body.removeChild(input); }, 25);
    };
    document.body.appendChild(input);
    return input;
"""

def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)
    
def tryAndRetryFillByIdWithExtraSteps(driver, idStep1, id, value):
    try:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        writeLetterByLetterId(id, value)
    except NoSuchElementException:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        print("the element needs to be charged...")
        time.sleep(10)
        writeLetterByLetterId(id, value)
    except ElementNotInteractableException:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        print("the element needs to be charged...")
        time.sleep(10)
        writeLetterByLetterId(id, value)

def tryAndRetryFillByXpath(driver, xpath, value):
    try:
        fillByXpath(driver, xpath, value)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(5)
        tryAndRetryFillByXpath(driver, xpath, value)



def RefreshExcel():
    # connection à l'excel préalablement téléchargé
    df = pd.read_excel(r'/home/ds/Documents/LIFE/data/Life-cm/upwork.com-backlinks_pages.xlsx')
    # Entrer les lignes à scrap
    for i in range(10, 510):
        __url = str(df.at[i, 'Source url'])
        if '/freelancers/' in __url:
            if __url in 'merdee' :
                pass
            else:
                __title = str(df.at[i, 'Source title'])
                __title = __title.replace("upwork", " " )
                __title = __title.replace(" - Upwork Freelancer ", " " )
                __title = __title.replace(" | upwork", " " )
                list_search.append({'__url': __url, '__title': __title})
                print(list_search)
                append_new_line(r'link-upwork.txt', str(__url))
    

def recaptcha(driver, Xpath):
    try:
        time.sleep(5)
        tryAndRetryClickXpath(driver, Xpath)
        time.sleep(2)
    except NoSuchElementException:
        time.sleep(5)
        
def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)

def scroll_function(i, driver):
    height = i * 1000
    time.sleep(1.3)
    driver.execute_script(
        "window.scrollTo(" + str(height) + ", " + str(height) + ")")
    time.sleep(1.3)


TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(description):
    return TAG_RE.sub(' ', description)


def initGoogle(driver):
    cookieGoogle = driver.find_element(By.ID, 'L2AGLb').click()
    try:
        driver.find_element(By.CLASS_NAME, 'h-captcha')
        input(Fore.BLUE + 'Captcha à résoudre veuillez le résoudre et tapez entrez pour continuer...')
        print(Style.RESET_ALL)
    except NoSuchElementException:
        print("No captcha")

    if cookieGoogle:
        print("GOOGLE a changé l'id recupere le nouveau")
    else:
        print("Init Google...")

def findlogo(driver):
    try:
        img_src = driver.find_element(By.XPATH, '(//a[1]//img)')
        img_src = img_src.get_attribute('src')
    except NoSuchElementException:
        img_src = ''
        pass
    return str(img_src)



class Spoofer(object):

    def __init__(self, country_id=['FR'], rand=True, anonym=True):
        self.country_id = country_id
        self.rand = rand
        self.anonym = anonym
        self.userAgent, self.ip = self.get()

    def get(self):
        ua = UserAgent()
        proxy = FreeProxy(country_id=self.country_id, rand=self.rand, anonym=self.anonym).get()
        ip = proxy.split("://")[1]
        return ua.random, ip


class DriverOptions(object):

    def __init__(self):

        self.options = Options()
        
        self.options.binary_location = "/usr/bin/google-chrome"
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")

        self.helperSpoofer = Spoofer()

        self.options.add_argument('user-agent={}'.format(self.helperSpoofer.userAgent))
        self.options.add_argument('--proxy-server=%s' % self.helperSpoofer.ip)


class WebDriver(DriverOptions):

    def __init__(self, path=''):
        DriverOptions.__init__(self)
        self.driver_instance = self.get_driver()

    def get_driver(self):

        print("""
        IP:{}
        UserAgent: {}
        """.format(self.helperSpoofer.ip, self.helperSpoofer.userAgent))

        PROXY = self.helperSpoofer.ip
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy":PROXY,
            "ftpProxy":PROXY,
            "sslProxy":PROXY,
            "noProxy":None,
            "proxyType":"MANUAL",
            "autodetect":False
        }
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

        path = os.path.join(os.getcwd(), '/home/ds/env/selenium/2023/chromedriver_linux64/chromedriver')

        driver = webdriver.Chrome(executable_path=path, options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })

        return driver

def substring_after(s, delim):
    return s.partition(delim)[2]

def browser():
    
    #driver= WebDriver()

    options = webdriver.ChromeOptions() 
    options.headless = True
    driverinstance = uc.Chrome(options=options)
    driverinstance.get("https://google.com/")
    driverinstance.get("https://google.com/")
    initGoogle(driverinstance)
    time.sleep(2)
    list_indeed = json.dumps(list_search)
    #json_raw= list_indeed.readlines()
    list_indeed = json.loads(list_indeed)
    driverinstance.get("https://www.upwork.com")
    recaptcha(driverinstance, '//button[@id="onetrust-accept-btn-handler"]')
    time.sleep(4)
    input('/////////////////////////')
    for item in list_indeed:
        driverinstance.get(item["__url"])
        time.sleep(5)
        myDict = {}
        myDict["TITRE"] = getinnertextXpath(driverinstance, '//h1')
        if myDict["TITRE"] == "www.upwork.fr" or myDict["TITRE"] == " ":
            myDict["TITRE"] = item["__title"].replace('https://www.upwork.com/freelancers/', '').replace('/', '')
        myDict["url"] = item["__url"]
        myDict["DESCRIPTION"] = remove_tags(getinnertextXpath(driverinstance, '//div[contains(@class, "skills")]'))
        myDict["CATEGORY"] = remove_tags(getinnertextXpath(driverinstance, '//div[contains(@class, "up-nav-pills")]//button[2]//span'))
        myDict["CATEGORY"] +=  myDict["CATEGORY"] + ", Influenceur, Influencer, Freelance"
        myDict["CATEGORY"] = myDict["CATEGORY"].replace('|', ',')
        myDict["YEAR"] = '2022'
        try:
            wait = WebDriverWait(driverinstance, 10)
            try:
                img_src = wait.until(EC.visibility_of_element_located((By.XPATH, '//img[contains(@class, "up-avatar-80")]')))
                img_src = img_src.get_attribute('src')
            except:
                pass
        except:
            img_src = item["__title"]
            pass
        myDict["IMAGE1"] = str(img_src)
        
        myDict["VIDEO"] = ''
        myDict["LOCATION"] = remove_tags(getinnertextXpath(driverinstance, '//div[contains(@class, "location-status")]'))
        
        myDict["CREATED_AT"] = "2023"
        
        append_new_line(r'result-upwork.txt', str(myDict))
        final_result.append(myDict)


    with open("res-upwork.json", "wb") as writeJSON:
        jsStr = json.dumps(final_result)
        # the decode() needed because we need to convert it to binary
        writeJSON.write(jsStr.encode('utf-8')) 
        print ('end')
    
    driverinstance.get("https://life-cm.com/wp-admin/")
    # connection au compte wp-admin
    driverinstance.find_element(By.XPATH,'//*[@id="user_login"]').send_keys('CEOLIFEMARKET')
    driverinstance.find_element(By.XPATH,'//*[@id="user_pass"]').send_keys('ppOxkyI&PQY!g^13ZGU69FxM')

    # collection des xPath important
    xPathLogin= '//*[@id="wp-submit"]'

    waitBeforeClickOnXpath(driverinstance, xPathLogin)
    time.sleep(6)


    print('------------------------------------------------------------------------------------------')
    #for i in range(16):
    for i in range(20):
        time.sleep(4)
        print(i)
    
    


list_search = list()
my_list = list()
final_result = list()
RefreshExcel()
browser()