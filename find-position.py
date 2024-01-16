
from cgi import test
import email
from lib2to3.pgen2 import driver
import linecache
import random
import unicodedata

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

import chardet
import codecs
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
import html
import pathlib

import openai
from openai.error import RateLimitError

from ast import literal_eval

import os
sys.setrecursionlimit(10000)


import codecs


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


def record_position(driverinstance, title):
    driverinstance.get("https://google.com/")
    try:
        driverinstance.find_element(By.XPATH, '//textarea[contains(@maxlength, "2048")]').send_keys(title)
    except NoSuchElementException:
        driverinstance.find_element(By.XPATH, '//input[contains(@maxlength, "2048")]').send_keys(title)
    #tryAndRetryFillByXpath(driverinstance, '//input[contains(@maxlength, "")]', title)
    
    actions = ActionChains(driverinstance)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)
        
    google_url = (driverinstance.current_url)
    google_url = google_url.replace('search?q=', 'search?num=25&q=')
    driverinstance.get(google_url)
    time.sleep(1)
    links = driverinstance.find_elements(By.XPATH, "//div[contains(@data-snhf, '0')]//a")
    pdf_position = -1

    for position, link in enumerate(links):
        href = link.get_attribute('href')
        if re.search(r'\btherapeute.net\b', href, re.IGNORECASE):
            pdf_position = position
            break
        

    if pdf_position == -1:
        print("Aucun lien ne contient de Therapeute.Net")
    return pdf_position

def strip_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def publish():
    option = FirefoxOptions()
    option.add_argument('--disable-notifications')
    option.add_argument("--mute-audio")
    option.add_argument("--headless")
    #option.profile = "C:/Users/admin/AppData/Local/Mozilla/Firefox/Profiles/a2wm8g9y.default"

    option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
    
    driverinstance = webdriver.Firefox(options=option)


    driverinstance.get("https://google.com/")
    initGoogle(driverinstance)
    time.sleep(2)
     
    
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    today = str(today)+".txt"


    dossier = "./TRACK"
    fichier = today
    chemin_fichier = os.path.join(dossier, fichier)
    chemin_fichier = str(chemin_fichier)
    
    if not os.path.exists(chemin_fichier):
        # Le fichier n'existe pas, on le crée
        with open(chemin_fichier, "w") as f:
            # Écrire le contenu initial du fichier si nécessaire
            f.write("1er Requete ,Position ,2e Requete,Position ,3e Requete,Position,")

        print("Le fichier", fichier, "a été créé dans le dossier", dossier)
    else:
        print("Le fichier", fichier, "existe déjà dans le dossier", dossier)
    

    fichier = open(source, "r", encoding='utf-8')  # Remplace "chemin_vers_ton_fichier.txt" par le chemin réel de ton fichier

    for ligne in fichier:
        valeurs = ligne.strip().split(",")
        if len(valeurs) >= 3:
            v1 = strip_accents(valeurs[0].strip())
            v2 = strip_accents(valeurs[1].strip())
            v3 = strip_accents(valeurs[2].strip())
            position_v1 = record_position(driverinstance, v1)
            position_v2 = record_position(driverinstance, v2)
            position_v3 = record_position(driverinstance, v3)
            print(str(v1)+" ,"+str(position_v1)+" ,"+ str(v2)+" ,"+str(position_v2)+" ,"+ str(v3)+" ,"+str(position_v3)+" ," )
            append_new_line(r''+chemin_fichier+'', str(v1)+" ,"+str(position_v1)+" ,"+ str(v2)+" ,"+str(position_v2)+" ,"+ str(v3)+" ,"+str(position_v3)+" ," )
    
    
derniernumer = "./TRACK/dernier_numero.txt"
source = "REFENCEMENT-PRATICIEN.txt"


list_search = list()
my_list = list()
my_list__ = list()
final_result = list()

def rewrite_utf():
         
    with open('./REFENCEMENT-PRATICIEN.txt', 'rb') as fichier:
        encodage = chardet.detect(fichier.read())['encoding']
            
    # Ouvrir le fichier en lecture avec l'encodage détecté
    with codecs.open('./REFENCEMENT-PRATICIEN.txt', 'r', encoding=encodage) as fichier:
        # Lire le fichier ligne par ligne
        for ligne in fichier:
            # Afficher la ligne sans modification
            print(ligne, end='')
            input(ligne)

publish()

#rewrite_utf()
""" 
while True:
    try:
        publish()
        break
    except Exception as e:
        print("Une erreur s'est produite :", str(e))
        print("Redémarrage du script dans 5 secondes...")
        time.sleep(360)"""
 