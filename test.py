
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
    with open(file_name, "a+", encoding='utf-8') as file_object:
        # Déplacez-vous à la fin du fichier avant d'écrire
        file_object.seek(0, 2)  # Se déplacer à la fin du fichier
        if file_object.tell() > 0:  # Vérifie si le fichier n'est pas vide
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
        time.sleep(3)
        driver.find_element(By.XPATH, xpath)
        if True:
            return 0
    except NoSuchElementException:
        return 1

def check_exists_by_xpath(driver, xpath):
    try:
        waitloading(2, driver)
        driver.find_element(By.XPATH, xpath)
        if True:
            return 0
    except NoSuchElementException:
        return 1


def waitloading(times, driverinstance):
    times = int(times)
    time.sleep(times)
    wait = WebDriverWait(driverinstance, times)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))


def associer_mots(fichier_entree, fichier_sortie):
    with open(fichier_entree, 'r') as f:
        mots = f.read().splitlines()
    
    with open(fichier_sortie, 'w') as f:
        while len(mots) > 1:
            mot = mots.pop(0)
            mot_associe = random.choice(mots)
            mots.remove(mot_associe)
            association = f"{mot} {mot_associe}\n"
            f.write(association)
    
        if mots:
            dernier_mot = mots[0]
            f.write(f"Dernier mot isolé : {dernier_mot}\n")
        else:
            f.write("Tous les mots ont été associés.\n")
        
    fichier_entree = "D:/D/words_alpha.txt"
    fichier_sortie = "words_alpha.txt"
    



def search_array(list_search, words):
    """if any(words in s for s in list_search):
        print('seeeeeeeeeeeeaaaaaaaaaaarrrrrrrrcccccchhhhhhhhh  ok')
        return 'ok'
    
    else:
        return 'add'"""
    if any(words in word for word in list_search):
        return 11
    else:
        return 22
    
    
def publish(url, driverinstance):


    linkkk = str(linecache.getline(r"./wordpress_website_done.txt", url))
    
    print(linkkk)
    append_new_line(r'ERREUR.txt', str(linkkk))

    driverinstance.get(str(linkkk))
    waitloading(5, driverinstance)

    tag_names = []

    """h1_element = driverinstance.find_element(By.XPATH,'//h1')
    h1_2element = driverinstance.find_element(By.XPATH,'//h1')
    body_xpath = driverinstance.find_element(By.XPATH,'//body')

    preceding_elements = driverinstance.find_elements(By.XPATH,'//h1/preceding::*')
    
    parent_element = driverinstance.execute_script("return arguments[0].parentNode;", h1_element)

    parents = []  # Liste pour stocker les éléments parents
    current_element = h1_element"""

    """for i in range(5):  # Répéter l'opération jusqu'à 5 fois
        current_element = driverinstance.execute_script("return arguments[0].parentNode;", current_element)
        if current_element.tag_name == "html":  # Arrêter si le parent est la racine du document
            break
        parents.append(current_element)
        input(current_element.tag_name)"""

    """# first_child_element = driverinstance.execute_script("return arguments[0].children[0];", h1_2element)
    first_child_element = driverinstance.find_element(By.XPATH, '//h1/following-sibling::*[1]')
    for i in range(5):  # Répéter l'opération jusqu'à 5 fois
        first_child_element = first_child_element.find_element(By.XPATH, '/following-sibling::*[1]')
        if first_child_element.tag_name == "html":  # Arrêter si le parent est la racine du document
            break
        parents.append(first_child_element)
        input(first_child_element.tag_name)"""
        
        


    """siblings = [first_sibling]
    for i in range(1, 5):
        try:
            
            next_sibling = driverinstance.find_element(By.XPATH, f'(//h1/following-sibling::*)[{i+1}]')
            input(next_sibling.tag_name)
        except Exception as e:
            print(f"Erreur lors de la recherche du frère suivant {i+1}: {e}")
            break  # Sortir de la boucle si aucun frère suivant n'est trouvé"""



    """preceding_elements = list(reversed(preceding_elements))

    last_five_preceding_elements = preceding_elements[-5:]"""

    """for elem in last_five_preceding_elements:
        print(elem.tag_name) """
    
    following_elements = driverinstance.find_elements(By.XPATH, '//h1/following::*[not(self::span or self::li or self::ul or self::a or self::footer or self::script or self::small or self::i or self::br or self::label or self::svg or self::img or self::input or self::hr or self::meta or self::link or self::noscript or self::style or self::iframe or self::embed or self::object or self::param or self::source or self::track)]')
    if following_elements is None:
        pass
    premier_element_apres_body = driverinstance.find_element(By.XPATH, '//body')
    nombre_caractere_in_body = 0
    nombre_caractere_in_body = len(premier_element_apres_body.text)
    print(nombre_caractere_in_body)

    max_text_length = 0
    element_with_most_text = None

    # Parcourez tous les éléments suivants et comptez leur texte
    for elem in following_elements[:10]:
        texte_plus_long = len(elem.text)
        text_length = len(elem.text)
        if text_length > max_text_length:
            max_text_length = text_length
            element_with_most_text = elem


    html_de_lelement = driverinstance.execute_script("return arguments[0].outerHTML;", element_with_most_text)


    
    save_by_line = "IN BODY --------------"
    save_by_line += str(nombre_caractere_in_body)
    save_by_line += "IN DIV AFTER H1 --------------"
    save_by_line += str(max_text_length)

    
    pourcentage = (max_text_length / nombre_caractere_in_body) * 100

    if pourcentage < 10:
        save_by_line += str(f"Le premier texte représente moins de 10% du second ({pourcentage:.2f}%)")
    elif pourcentage > 30:
        save_by_line += str(f"Le premier texte représente plus de 30% du second ({pourcentage:.2f}%)")
    else:
        save_by_line += str(f"Le premier texte représente entre 10% et 30% du second ({pourcentage:.2f}%)")


    if element_with_most_text is not None:
        print(f"Balise avec le plus de texte: {element_with_most_text.tag_name}, Texte: {element_with_most_text.text[:30]}...")


    append_new_line(r'ERREUR.txt', str(save_by_line))
    append_new_line(r'ERREUR.txt', str(html_de_lelement))
    #input(parent_element.tag_name)






    """links = driverinstance.find_elements(By.XPATH,'//table[contains(@class, "responsive")]//a')
    for i in links:
        input("88888888")
        i.click()"""
        

option = FirefoxOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
driverinstance = webdriver.Firefox(options=option)

for id in range(17, 1500):
    try : 
        publish(id, driverinstance)
    except NoSuchElementException:
        append_new_line(r'ERREUR.txt', str("pas de H1 "))
    


