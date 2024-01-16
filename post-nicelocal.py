
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
from selenium.webdriver.firefox.options import Options as FirefoxOptions

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
    print("Continues the script")

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
    time.sleep(2)
    try:
        waitBeforeClickOnXpath(driver, Xpath)
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


def substring_after(s, delim):
    return s.partition(delim)[2]

def RefreshExcel():
    # connection à l'excel préalablement téléchargé
    df = pd.read_excel(r'/home/ds/Documents/LIFE/data/W/nicelocal.fr-organic.Positions-fr-20230408-2023-04-09T18 21 22Z.xlsx')
    # Entrer les lignes à scrap
    for i in range(1, 5150):
        __url = str(df.at[i, 'URL'])
        if ('/avocats/avocat-' in __url or '/cabinets/cabinet' in __url) and int(df.at[i, 'Keyword Difficulty']) < 32 and int(df.at[i, 'Search Volume']) > 460 and int(df.at[i, 'Position']) < 40:
            if True:
                
                __title = str(df.at[i, 'Keyword'])
                __title = __title.replace("nicelocal", " " )
                __title = __title.replace(" | Reviews, Pricing, Features", " " )
                __title = __title.replace(" | nicelocal", " " )
                __img = ""
                __description = __title + " La "+ __title +" : définition     Les caractéristiques des "+ __title +"     Le business plan de "+ __title +"     Le financement de "+ __title +"     La forme juridique de "+ __title +""
                list_search.append({'__url': __url, '__title': __title, '__img': __img, '__description': __description})
                print(list_search)
                append_new_line(r'link-nicelocal.txt', str(__url))
            else:
                pass

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        if True:
            return 0
    except NoSuchElementException:
        return 1

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
    options.headless = False
    #driverinstance = uc.Chrome(executable_path=chrome_path, options=options)
    
    driverinstance = uc.Chrome(version_main=108, options=options)

    driverinstance.get("https://google.com/")
    initGoogle(driverinstance)
    time.sleep(2)
    driverinstance.get("https://www.nicelocal.fr")
    time.sleep(4)
    count = 0
    list_indeed = json.dumps(list_search)
    list_indeed = json.loads(list_indeed)
    while True:
        nombre = int(input("Entrez un nombre : "))
        iddd = str(input("Entrez un id (u9394741) : "))
        if nombre > 0:
            
            links = driverinstance.find_elements(By.XPATH,"//ul[contains(@data-uitest, 'results-container')]//li")
            count = len(links)
            print(count)
            count = count - 10
            for innn in range(count):
                
                myDict = {}
                myDict["TITRE"] = remove_tags(getinnertextXpath(driverinstance, "//*[@id='"+str(iddd)+"']//li["+str(innn)+"]//h2[contains(@class, 'minicard-item__title')]//a"))
                myDict["url"] = remove_tags(findATTR(driverinstance, "//*[@id='"+str(iddd)+"']//li["+str(innn)+"]//h2[contains(@class, 'minicard-item__title')]//a", 'href'))
                myDict["DESCRIPTION"] = " "
                myDict["CATEGORY"] = remove_tags(getinnertextXpath(driverinstance, "//*[@id='"+str(iddd)+"']//li["+str(innn)+"]//div[contains(@class, 'minicard-item__features')]//a[last()]"))
                myDict["YEAR"] = ''
                myDict["IMAGE1"] = remove_tags(findATTR(driverinstance, "//*[@id='"+str(iddd)+"']//li["+str(innn)+"]//img[contains(@data-uitest, 'org-card-image')]", 'src'))
                
                myDict["IMAGE2"] = " "
                
                myDict["VIDEO"] = ""
                
                myDict["WEBSITE"] = ""
                myDict["EMAIL"] = ''
                myDict["PHONE"] = remove_tags(findATTR(driverinstance, "//*[@id='"+str(iddd)+"']//li["+str(innn)+"]//a[contains(@data-uitest, 'phone-link')]", 'href'))
                myDict["PHONE"] = myDict["PHONE"].replace('tel:', '')
                myDict["FACEBOOK"] = ''
                myDict["TWITTER"] = ''
                myDict["INSTAGRAM"] = ''
                myDict["LINKEDIN"] = ''
                
                myDict["LOCATION"] = remove_tags(getinnertextXpath(driverinstance, "//*[@id='"+str(iddd)+"']//li["+str(innn)+"]//address[contains(@class, 'minicard-item__address')]//span"))
                    
                myDict["CREATED_AT"] = ''
                myDict["UPDATED_AT"] = ''
                append_new_line(r'result-nicelocal.txt', str(myDict))
                final_result.append(myDict)
        else:
            break
    
    with open("res-nicelocal.json", "wb") as writeJSON:
        jsStr = json.dumps(final_result)
        # the decode() needed because we need to convert it to binary
        writeJSON.write(jsStr.encode('utf-8')) 
        print ('end')
    


list_search = list()
my_list = list()
final_result = list()
#RefreshExcel()
browser()
