
from cgi import test
import email
from lib2to3.pgen2 import driver
import linecache
import random
from typing_extensions import Self
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
import requests

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




def scroll_function(driver, i):
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
        result = ""
        result = driver.find_element(By.XPATH, xPath)
        result = (result.get_attribute('innerText'))
    except NoSuchElementException:  #spelling error making this code not work as expected
        result = "ZZZZZZZZZZZ"
        pass
    return str(result)


    
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

def if_as_value_FillByXpath(driver, xpath, value):
    if(len(value) > 2):
        try:
            fillByXpath(driver, xpath, value)
        except NoSuchElementException:
            pass
    else:
        pass


def clear_element(driver, xpath):
    elem2 = driver.find_element(By.XPATH, xpath)
    driver.execute_script('arguments[0].value = "";', elem2)

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
        print(Fore.BLUE + 'Captcha à résoudre veuillez le résoudre et tapez entrez pour continuer...')
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

def substring_after(s, delim):
    return s.partition(delim)[2]

def count_nombre_de_chiffre(str):
    digit=letter=0
    for ch in str:
        if ch.isdigit():
            digit=digit+1
        elif ch.isalpha():
            letter=letter+1
        else:
            pass
    return digit

def valueifnull(returns, new):
    if returns is None:
        return new
    else:
        returns = str(returns)
        if len(returns.replace(" ", "")) < 4:
            return new
        else:
            return returns


def returnvalueif_delimiter_error(returns, delimiter, new):
    input_string = returns

    slots = input_string.split(delimiter,1)
    if len(slots) > 1:
        return slots[1]
    else:
        return new
    
def solve(x):
    try:
        return literal_eval(x)
    except (ValueError, SyntaxError):
        return x
    
def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        if True:
            return 0
    except NoSuchElementException:
        return 1



def search_array(list_search, words):
    """if any(words in s for s in list_search):
        print('seeeeeeeeeeeeaaaaaaaaaaarrrrrrrrcccccchhhhhhhhh  ok')
        return 'ok'
    
    else:
        return 'add'"""
    print('seeeeeeeeeeeeaaaaaaaaaaarrrrrrrrcccccchhhhhhhhh  ok')
    if any(words in word for word in list_search):
        return 11
    else:
        return 22

def post_commet(driverinstance):
    try:
        tryAndRetryFillByXpath(driverinstance, '//input[contains(@id, "author")]', str('Manuel Lombardi France'))
    except NoSuchElementException:
        pass
    try:
        tryAndRetryFillByXpath(driverinstance, '//input[contains(@id, "email")]', str('contact@life-community.fr'))
    except NoSuchElementException:
        pass
    try:
        tryAndRetryFillByXpath(driverinstance, '//textarea[contains(@id, "comment")]', str('Excellent Article, Merci pour votre promptidude ')+'<a href="https:/life-community.fr/" / rel="follow ugc">Good - Bien a vous</a> ')
    except NoSuchElementException:
        pass
    try:
        driverinstance.find_element(By.XPATH, '//input[contains(@id, "url")]').send_keys("https:/life-community.fr/")
    except NoSuchElementException:
        pass
    tryAndRetryClickXpath(driverinstance, '//input[contains(@id, "submit")]')
    
def publish():
    option = FirefoxOptions()
    option.add_argument('--disable-notifications')
    option.add_argument("--mute-audio")
    option.add_argument("--headless")
    option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
    word_file = r"C:/Users/admin/Documents/DEV TEST/ucoz-seo/words_alpha.txt"
    WORDS = open(word_file).read().splitlines()
    WORDS = str(WORDS[random.randint(10, 368660)])
    driverinstance = webdriver.Firefox(options=option)
        
    for item in range(1, 8000):
        title = linecache.getline(r"/opt/lampp/htdocs/avis-review.com/scrap/all_link_sitemap.txt", item)
        link = linecache.getline(r"/opt/lampp/htdocs/avis-review.com/scrap/all_link_sitemap.txt", item)
        append_new_line(r'all_link_googlebot_done.txt', str(title))
        
        if "https://life-community.fr/" in title:
            title = title
        else:
            title = WORDS
        if "/wp-content/"  in title  or "listivotheme"  in title or "data:image"  in title or "/listivo_template/"  in title or "/wp-admin/"  in title:
            title = WORDS            
        title = title.replace('https://life-community.fr/avis/', '').replace('https://life-community.fr/review/', '').replace('https://life-community.fr/category/', '').replace('https://life-community.fr/tag/', '').replace('https://', '').replace('/', '').replace('.fr', '')
        
        title = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿЀ-ӿ/]+', ' ', title)
        
        driverinstance.get("https://google."+final_result[random.randint(0, 8)]+"")
        initGoogle(driverinstance)
        time.sleep(5)
        try:
            driverinstance.find_element(By.XPATH, '//textarea[contains(@maxlength, "2048")]').send_keys(title)
        except NoSuchElementException:
            driverinstance.find_element(By.XPATH, '//input[contains(@maxlength, "2048")]').send_keys(title)
        #tryAndRetryFillByXpath(driverinstance, '//input[contains(@maxlength, "")]', title)
        
        actions = ActionChains(driverinstance)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(5)
        google_url = (driverinstance.current_url)
        google_url = google_url.replace('search?q=', 'search?num=80&q=')
        driverinstance.get(google_url)      
        links = driverinstance.find_elements(By.XPATH,"//div[contains(@data-header-feature, '0')]//a")
        #links = driverinstance.find_element_by_xpath("//div[contains(@data-, "")]//a")
        count = len(links)
        print(count)
        for i in links:
            step1 = (i.get_attribute('href'))
            if step1 in "avis-verifies.com":
                pass
            else:
                my_list.append(step1)
            
        for j in my_list:
            print(title)
            print(j)
            driverinstance.get(j)
            time.sleep(9)
            # from urlparse import urlparse  # Python 2
            parsed_uri = urlparse(j)
            result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            hostname = result
            driverinstance.get(hostname+"wp-admin/")
            time.sleep(5)
            if check_exists_by_xpath(driverinstance, '//*[contains(@id, "login")]') == 0:
                driverinstance.get(j)
                time.sleep(5)
                if check_exists_by_xpath(driverinstance, '//*[contains(@id, "author")]') == 0:
                    post_commet(driverinstance)
                else:
                    driverinstance.get(hostname+"?s=  s")
                    time.sleep(5)
                    recaptcha(driverinstance, '//h3//a[contains(@href, "'+hostname+'")][2]')
                    time.sleep(5)
                    if check_exists_by_xpath(driverinstance, '//*[contains(@id, "author")]') == 0:
                        post_commet(driverinstance)
                    else:
                        driverinstance.get(hostname+"/?s=  s")
                        time.sleep(5)
                        recaptcha(driverinstance, '//h4//a[contains(@href, "'+hostname+'")][2]')
                        if check_exists_by_xpath(driverinstance, '//*[contains(@id, "author")]') == 0:
                            post_commet(driverinstance)
                        else:
                            driverinstance.get(hostname+"/?s=  s")
                            time.sleep(5)
                            recaptcha(driverinstance, '//h2//a[contains(@href, "'+hostname+'")][2]')
                            time.sleep(5)
                            if check_exists_by_xpath(driverinstance, '//*[contains(@id, "author")]') == 0:
                                post_commet(driverinstance)
                            
            else:
                pass
                
        append_new_line(r'all_link_googlebot_done.txt', str(link))
        
        
list_search = list()
my_list = list()
final_result = list()
final_result = ["fr", "com","cn","es","ca","ru","de",".com.hk", ".co.uk"]

#browser()
#postbrowser()
publish()
