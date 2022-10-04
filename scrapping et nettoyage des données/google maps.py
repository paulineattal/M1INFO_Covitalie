#!/usr/bin/env python
# coding: utf-8



from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


#ouvrir la page 
driver = webdriver.Firefox()
#Chrome("/home/pauline/chromedriver_linux64/chromedriver")

url = "https://www.google.it/maps/place/Fontaine+de+Trevi/@41.9010333,12.4810843,17z/data=!3m1!5s0x132f60532f7ce5d1:0x189b3b81539ea84d!4m7!3m6!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!8m2!3d41.9009325!4d12.483313!9m1!1b1"
driver.get(url)

#accepter les cookies
accept_button = driver.find_element_by_xpath("//span[contains(text(), \"J\'accepte\")]")
if accept_button: 
    driver.execute_script("arguments[0].scrollIntoView();", accept_button)
    time.sleep(2)
    accept_button.click()
    time.sleep(2)
    
#trier 
wait = WebDriverWait(driver, 10)
menu_bt = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-value=\'Trier\']')))  
menu_bt.click()
time.sleep(0.5)
recent_rating_bt =driver.find_element_by_xpath('//*[@id="action-menu"]/ul/li[1]')
recent_rating_bt.click()


#scroll
total_number_of_reviews = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]').text.split(" ")[0]
total_number_of_reviews = total_number_of_reviews.replace(u"\u202f","") if u"\u202f" in total_number_of_reviews else int(total_number_of_reviews)
total_number_of_reviews=int(total_number_of_reviews)
scrollable_div = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]')
#Scroll as many times as necessary to load all reviews
for i in range(0,round(total_number_of_reviews / 100)):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',scrollable_div)
    time.sleep(0.3)



response = BeautifulSoup(driver.page_source, 'html.parser')
r = response.find_all('div', class_="ODSEW-ShBeI NIyLF-haAclf gm2-body-2")


rev_dict = {'Review Text': [],
            'Review Name' : [],
            'Review Time': [],
            'Review Role' : [],
            'Review Perso Num Rate' : [],
            'Review Rate' : []}

for rv in r :
    review_text = rv.find_all('span', class_='ODSEW-ShBeI-text')
    review_name = rv.find_all('span', jstcache='304')
    review_date = rv.find_all('span',class_='ODSEW-ShBeI-RgZmSc-date')
    review_role = rv.find_all('span', jstcache='323') 
    review_perso_num_rate = rv.find_all('span', jstcache='324') 
    review_rate = rv.find_all('span', class_="ODSEW-ShBeI-H1e3jb")
    
    if len(review_text) == 0 : 
        rev_dict['Review Text'].append(None)
    else :
        for rv in review_text :
            rev_dict['Review Text'].append(rv.get_text())
            
    if len(review_name) == 0 :
        rev_dict['Review Name'].append(None)
    else:
        for rv in review_name : 
            rev_dict['Review Name'].append(rv.get_text())
    if len(review_date) == 0:
        rev_dict['Review Time'].append(None)
    else:
        for rv in review_date :
            rev_dict['Review Time'].append(rv.get_text())
        
    if len(review_role) == 0 : 
        rev_dict['Review Role'].append(None)
    else :
        for rv in review_role : 
            rev_dict['Review Role'].append(rv.get_text())
            
    if len(review_perso_num_rate) == 0 : 
        rev_dict['Review Perso Num Rate'].append(None)
    else :
        for rv in review_perso_num_rate : 
            rev_dict['Review Perso Num Rate'].append(rv.get_text())
    for rv in review_rate : 
        attributes_dictionary = rv.attrs
        stars = attributes_dictionary['aria-label']
        rev_dict['Review Rate'].append(stars)

df=pd.DataFrame(rev_dict)
df.to_csv("fontaine_de_trevi_google_maps.csv")



liste_url['https://www.google.it/maps/place/Panth%C3%A9on/@41.8986108,12.4746842,17z/data=!4m7!3m6!1s0x132f604f678640a9:0xcad165fa2036ce2c!8m2!3d41.8986108!4d12.4768729!9m1!1b11',          'https://www.google.it/maps/place/Colis%C3%A9e/@41.8902102,12.4900422,17z/data=!4m7!3m6!1s0x132f61b6532013ad:0x28f1c82e908503c4!8m2!3d41.8902102!4d12.4922309!9m1!1b1',          'https://www.google.it/maps/place/Fontaine+de+Trevi/@41.9010333,12.4810843,17z/data=!3m1!5s0x132f60532f7ce5d1:0x189b3b81539ea84d!4m7!3m6!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!8m2!3d41.9009325!4d12.483313!9m1!1b1',          'https://www.google.it/maps/place/Pont+du+Rialto/@45.4379842,12.3337093,17z/data=!4m7!3m6!1s0x477eb1c7faa33a3b:0x732011a1298ecc89!8m2!3d45.4379842!4d12.335898!9m1!1b1',          'https://www.google.it/maps/place/Piazza+San+Marco/@45.4341549,12.3375331,18z/data=!4m11!1m2!2m1!1sPiazza+San+Marco!3m7!1s0x477eb1d76e418489:0x2d0bb9644fff61b!8m2!3d45.4341668!4d12.3384717!9m1!1b1!15sChBQaWF6emEgU2FuIE1hcmNvWhIiEHBpYXp6YSBzYW4gbWFyY2-SAQVwbGF6YQ',          'https://www.google.it/maps/place/Palais+des+Doges/@45.4337035,12.3392951,18z/data=!4m7!3m6!1s0x477eb1d76e418489:0xb809d204dcca74d1!8m2!3d45.4337035!4d12.3403894!9m1!1b1'
         ]

