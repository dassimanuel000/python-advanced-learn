
from cgi import test
import email
from lib2to3.pgen2 import driver
import linecache
import random
from typing_extensions import Self
from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from http import HTTPStatus
from urllib.parse import urlparse
from logging import exception
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
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import Select

################

import sys
from fp.fp import FreeProxy
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
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
from dateutil.relativedelta import relativedelta
import datetime
import requests, socket
from urllib3.connection import HTTPConnection

HTTPConnection.default_socket_options = ( 
    HTTPConnection.default_socket_options + [
    (socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000), #1MB in byte
    (socket.SOL_SOCKET, socket.SO_RCVBUF, 1000000)
])
import logging

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
import pathlib
from urlextract import URLExtract
extractor = URLExtract()
from slugify import slugify


from ast import literal_eval

import os
sys.setrecursionlimit(10000)








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

def findATTR(driver, xpath, attr):
    try:
        value_attr = driver.find_element(By.XPATH, xpath)
        value_attr = value_attr.get_attribute(attr)
    except NoSuchElementException:
        value_attr = ' '
        pass
    return str(value_attr)


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

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
    
def substring_after(s, delim):
    return s.partition(delim)[2]

def get_website_status(url):
    
    retry_count = 2 # Nombre de tentatives de vérification en cas d'échec
    retry_interval = 3 # Intervalle entre chaque tentative de vérification (en secondes)

    for i in range(retry_count + 1):
        response = requests.get(url)
        status_code = response.status_code
        
        if status_code >= 200 and status_code < 300:
            print("L'URL", url, "a renvoyé une réponse valide:", status_code)
            result = "200"
            break # Sort de la boucle si la réponse est valide
        elif i == retry_count:
            result = "NONE"
            print("L'URL", url, "a échoué après", retry_count, "tentatives")
        else:
            result = "NONE"
            print("L'URL", url, "a renvoyé une réponse inattendue:", status_code)
            print("Reprise de la vérification dans", retry_interval, "secondes...")
            time.sleep(retry_interval)
    return str(result)
    """ result = "NONE"
     # handle connection errors
     try:
          # open a connection to the server with a timeout
          with urlopen(url, timeout=5) as connection:
               # get the response code, e.g. 200
               code = connection.getcode()
               result = (code)
               result = "200"
     except HTTPError as e:
          result = "NONE"
     except URLError as e:
          result = "NONE"
     except:
          result = "NONE"
     print(result)
     parsed_uri8888 = urlparse(url)
     result8888 = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri8888)
     hostname8888 = result8888
     list_search.append(hostname8888)
     return str(result)"""
     
     
def RefreshExcel():
    # connection à l'excel préalablement téléchargé
    df = pd.read_excel(r'/home/ds/Downloads/Telegram Desktop/franceverif_fr_organic_Positions_fr_20230320_2023_03_21T11_00_15Z.xlsx')
    # Entrer les lignes à scrap
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    

    for i in range(8721, 9999):
        __url = str(df.at[i, 'URL'])
        if '/site/' in __url and int(df.at[i, 'Keyword Difficulty']) < 32: # and int(df.at[i, 'Keyword Difficulty']) < 35 and int(df.at[i, 'Search Volume']) > 7000:
            if True:
                myDict = {}
                myDict["WEBSITE"] = (__url).replace("https://franceverif.fr/fr/site/", "")
                url__http = "http://"+myDict["WEBSITE"]
                url__https = "https://"+myDict["WEBSITE"]
                if "mandmdirect" in url__https:
                    pass
                else:
                    if get_website_status(url__http) == "200" or get_website_status(url__https) == "200":
                        __title = str(df.at[i, 'Keyword'])
                        __title = __title.replace("franceverif", " " )
                        __title = __title.replace(" | Reviews, Pricing, Features", " " )
                        __title = __title.replace(" | franceverif", " " )
                        __img = ""
                        __description = __title + "  <br> Évaluation de fiabilité du site "+ myDict["WEBSITE"] +" <br>  Les caractéristiques du site "+ __title
                        list_search.append({'__url': __url, '__title': __title, '__img': __img, '__description': __description})
                        print(i)
                        myDict["TITRE"] = " "
                        for k in __title.split("\n"):
                            myDict["TITRE"] += (re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿЀ-ӿ/]+', ' ', k))
                        myDict["TITRE"] = str(myDict["TITRE"]).title()
                        myDict["TITRE"] = myDict["TITRE"].replace("Review", "" ).replace("review", "" )
                        myDict["TITRE"] = myDict["TITRE"].replace("Avis ", "" ).replace(" avis ", "" ).replace("Www", "" ).replace("wwww", "" )
                        
                    
                        myDict["DESCRIPTION"] = myDict["TITRE"] +" " + __description
                        
                        myDict["TITRE"] = (__url).replace("https://franceverif.fr/fr/site/", "").replace(".", " ").replace("-", " ")
                        myDict["TITRE"] = valueifnull(myDict["TITRE"].title(), ' ')
                        myDict["url"] = __url
                        myDict["CATEGORY"] = "Compagnie"
                        myDict["YEAR"] = ""
                        myDict["IMAGE1"] = ""
                        myDict["IMAGE2"] = ""
                        myDict["IMAGE3"] = ""
                        myDict["LOCATION"] = ""
                        myDict["CREATED_AT"] = ""
                        myDict["UPDATED_AT"] = "2023"
                        
                        
                        
                        myDict["WEBSITE"] = (__url).replace("https://franceverif.fr/fr/site/", "")
                        
                        
                        myDict["EMAIL"] = "contact@"+(__url).replace("https://franceverif.fr/fr/site/", "")
                        
                        myDict["PHONE"] = ""
                        
                        
                        
                        myDict["FACEBOOK"] = ""
                        myDict["TWITTER"] = ""
                        myDict["INSTAGRAM"] = ""
                        myDict["LINKEDIN"] = ""
                        myDict["SNAPCHAT"] = " "
                        myDict["CHAINE_YOUTUBE"] = ""
                        myDict["VIDEO"] = ""
                        myDict["TIKTOK"] = ""
                        myDict["TWICH"] = ""
                        myDict["NIC-SIRET"] = ""
                        myDict["AVIS"] = ""
                        myDict["AUTHOR"] = ""
                        myDict["AVIS_EMAIL"] = ""
                        myDict["COMMENT"] = ""
                        #append_new_line(r'all.txt', str(myDict))
                        final_result.append(myDict)
                        append_new_line(r'all-2-franceverif.txt', str(myDict))
            else:
                pass
    

    with open("res-2-franceverif.json", "wb") as writeJSON:
        jsStr = json.dumps(final_result)
        # the decode() needed because we need to convert it to binary
        writeJSON.write(jsStr.encode('utf-8')) 
        print ('end')
        
        
        
def valueifnull(returns, new):
    if returns is None:
        return new
    else:
        if len(returns.replace(" ", "")) < 4:
            return new
        else:
            return returns
def browser():
    
    
    """option = FirefoxOptions()
    option.add_argument('--disable-notifications')
    option.add_argument("--mute-audio")
    option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

    driverinstance = webdriver.Firefox(options=option)"""
    
    chrome_path = r"/home/ds/env/selenium/3/chromedriver"
    options = webdriver.ChromeOptions()
    options.headless = True
    #driverinstance = uc.Chrome(executable_path=chrome_path, options=options)
    
    driverinstance = uc.Chrome(version_main=108, options=options)

    driverinstance.get("https://google.com/")
    initGoogle(driverinstance)
    time.sleep(2)
    driverinstance.get("https://franceverif.fr/")
    time.sleep(8)
    recaptcha(driverinstance, '//button[contains(@class, "iubenda-cs-accept-btn")]')
    time.sleep(4)
    list_indeed = json.dumps(list_search)
    list_indeed = json.loads(list_indeed)
    for item in list_indeed:
        driverinstance.get(item["__url"])
        time.sleep(5)
        myDict = {}
        myDict["TITRE"] = remove_tags(getinnertextXpath(driverinstance, '//h1'))
        if myDict["TITRE"] == ' ':
            myDict["TITRE"] = item["__title"]
        myDict["url"] = item["__url"]
        myDict["DESCRIPTION"] = remove_tags(getinnertextXpath(driverinstance, '//div[contains(@class, "description")]'))
        if myDict["DESCRIPTION"] == ' ':
            myDict["DESCRIPTION"] = item["__description"]
        myDict["CATEGORY"] = remove_tags(getinnertextXpath(driverinstance, '//div[contains(@class, "activity")][1]'))
        if myDict["CATEGORY"] == ' ':
            myDict["CATEGORY"] = remove_tags(getinnertextXpath(driverinstance, '//div[contains(@class, "activity")][2]'))
        myDict["CATEGORY"] += ', Entreprises'
        myDict["YEAR"] = '2022'
        myDict["IMAGE1"] = valueifnull(remove_tags(findATTR(driverinstance, "//div[contains(@class, 'thumbnail')]//img", 'src')), item["__img"])
        myDict["IMAGE2"] = valueifnull(remove_tags(findATTR(driverinstance, "//div[contains(@id, 'media-0')]//img", 'src')), item["__img"])
        myDict["IMAGE3"] = valueifnull(remove_tags(findATTR(driverinstance, "//div[contains(@id, 'media-1')]//img", 'src')), item["__img"])
        
        myDict["VIDEO"] = remove_tags(getinnertextXpath(driverinstance, '//iframe[contains(@src, "youtube")]'))
        
        recaptcha(driverinstance, '//button[contains(@class, "popup-close-btn")]')
        myDict["WEBSITE"] = remove_tags(findATTR(driverinstance, "//a[contains(@onclick, 'company.websiteClick();')]", 'href'))
        myDict["EMAIL"] = ''
        myDict["PHONE"] = remove_tags(getinnertextXpath(driverinstance, '//button[contains(@id, "phone-display")]'))
        myDict["FACEBOOK"] = ''
        myDict["TWITTER"] = ''
        myDict["INSTAGRAM"] = ''
        myDict["LINKEDIN"] = ''
        myDict["LOCATION"] = remove_tags(getinnertextXpath(driverinstance, '//address//br'))+  remove_tags(getinnertextXpath(driverinstance, '//span[contains(@class, "city")]'))
        
        myDict["CREATED_AT"] = ''
        myDict["UPDATED_AT"] = '2022'
        
        append_new_line(r'result-franceverif.txt', str(myDict))
        final_result.append(myDict)


    with open("res-franceverif.json", "wb") as writeJSON:
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
#browser()
