"""
Python
Licence Type
Author: Matteo Montanari
e-mail: matteo.montanari25@gmail.com

INSTALLATION guide:

sudo pip3 install beautifulsoup4 selenium
# apt-get install xvfb #as per http://www.alittlemadness.com/2008/03/05/running-selenium-headless/

 Xvfb :10 -ac & # as per this https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2

https://github.com/mozilla/geckodriver/releases
#export PATH=$PATH:/home/matteo/Public

"""    


# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random


#CONSTANTs

                          
listOf_Currency = {
					'http://www.bsi.si/podatki/tec-bs-en.asp': [ '/html/body/div/table[2]/tbody/tr[1]/td[3]/table[2]/tbody/tr[3]/td/table/tbody/tr/td/table[2]/tbody/tr[3]'],

				   }



# INITIALIZATION OF WEB-BROWSER
internal_browser = webdriver.Firefox()
internal_browser.implicitly_wait(20)



for key, value in listOf_Currency.items():
	internal_browser.get(key)
	time.sleep(2)
	value_of_exchange_rate = internal_browser.find_element_by_xpath(value[0])
	print(value_of_exchange_rate)

















