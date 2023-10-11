import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

df = pd.read_csv('username - username.csv')
print(df)

for row, datos in df.iterrows():
    print('Datos: ', datos)
    print('Datos keys: ', datos.keys())
    print('Row: ', row)
    username = datos['Username']
    identifier = datos['Identifier']
    firstName = datos['First name']
    lastName = datos['Last name']

    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScowKVPHGmnoM1WYDlZc87daqRoddtuTKWh9EQbX7ygHWHFiA/viewform?usp=sf_link')

    time.sleep(0.1)

    element = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.RpC4Ne.oJeWuf > div.Pc9Gce.Wic03c > textarea").send_keys(username)
    element = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.RpC4Ne.oJeWuf > div.Pc9Gce.Wic03c > textarea").send_keys(identifier)
    element = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(firstName)
    element = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(lastName)
    time.sleep(0.1)
    element = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span > span").click()

