#! /usr/bin/env python
# -- coding: utf-8 --
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import time
import math
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datetime

link = "https://bavaria.client.bmw.kodixauto.ru/owners/vehicle-service-parts/service-form/#service_form"
name = 'Игорь'
lastname = 'Петров'
phone = '9124567897'
email = 'test@qa.test'
vin = '12345678912345678'
d = datetime.date.fromordinal(datetime.date.today().toordinal()+1).strftime("%d/%m/%Y")
t = time.strftime("%H/%M", time.localtime())
y = datetime.date.fromordinal(datetime.date.today().toordinal()+1).strftime("%Y")

class ServiceFormTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get(link) 
        assert 'Запись на сервис' in driver.title
        self = driver.find_element(By.ID, 'service_form_send')

        self = driver.find_element(By.CSS_SELECTOR, 'div.form__section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.send_keys(Keys.ENTER)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ENTER)

        self = driver.find_element(By.CSS_SELECTOR, '#vin').send_keys(vin)

        self = driver.find_element(By.XPATH, '//*[@id="year"]').send_keys(y)


        self = driver.find_element(By.CSS_SELECTOR, 'div.form-element:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.send_keys(Keys.ENTER)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ENTER)

        self = driver.find_element(By.XPATH, '//*[@id="datepicker"]').send_keys(d)

        self = driver.find_element(By.XPATH, '//*[@id="timepicker"]')
        self.click()
        self.send_keys(t)

        self = driver.find_element(By.CSS_SELECTOR, 'label.u116-00:nth-child(2)').click()

        self = driver.find_element(By.CSS_SELECTOR, 'label.u116-00:nth-child(1)').click()

        self = driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(name)  

        self = driver.find_element(By.ID, 'last_name').send_keys(lastname)

        self = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(phone)

        self = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)

        self = driver.find_element(By.XPATH, '//*[@id="replacement_car"]').click()

        self = driver.find_element(By.XPATH, '//*[@id="processing_of_personal_data"]').click()

        self = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[6]/div/button').click()
        time.sleep(2)
ts =  ServiceFormTest()