import selenium 
import time 
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver 
import webdriver_manager 
import os
import claves_fiscales
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

driver= r'webdriver//chromedriver.exe'

ruta_descarga=r'C:\Users\SOLO OUTLOOK\Documents\Domicilio fiscal electronico' #ACA SE PUEDE CAMBIAR CON UN INPUT
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" :  ruta_descarga}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=driver, options=chromeOptions)

df = pd.read_csv("cuits.csv", encoding="latin-1")
NOTIFICACIONES=open("NOTIFICACIONES.csv","a")

for row,cuits in df.iterrows():
    cuits=str(cuits['CUIT'])

    driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
    driver.maximize_window()
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').clear()
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').send_keys(cuits)
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/input[2]').click()
    try:
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[2]').send_keys(claves_fiscales.clave_fiscal(cuits))
            
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div/div/form/div/input[3]').click()
        time.sleep(1)
        try:
            driver.find_element("xpath", '/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]').click()
        except:
            pass
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[1]/div[5]/div/a/div[2]').click()
        time.sleep(10)   
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.close()
        driver.switch_to.window(window_after)
        time.sleep(3)
  
        
        def buscador():
            try:
                driver.find_element_by_css_selector(".fas.fa-envelope")
                if True:
                    print("SI NOTIFICACION "+ cuits + "----------SOCIEDAD------------")
                    NOTIFICACIONES.write(cuits + ";" + " SI NOTIFICACIONES ------- SOCIEDAD"+"\n")   
                else:
                    print("NO NOTIFICACION "+ cuits+"----------SOCIEDAD------------")  
                    NOTIFICACIONES.write(cuits +";"+ " NO NOTIFICACIONES ------- SOCIEDAD"+"\n")                            
            except:
                pass 
        
            try:
                driver.find_element_by_xpath("//*[contains(text(),\' Mis Comunicaciones (0) ')]")
                if True:
                    print("NO NOTIFICACION "+ cuits + "----------PERSONA FISICA------------")
                    NOTIFICACIONES.write(cuits + ";" + " NO NOTIFICACIONES ------- PERSONA FISICA"+"\n")    
                                        
            except:          
                print("SI NOTIFICACION "+ cuits + "----------PERSONA FISICA------------")
                NOTIFICACIONES.write(cuits + ";" +" SI NOTIFICACIONES ------- PERSONA FISICA"+"\n") 
        buscador()
        

    except:
        ERROR=open("ERRONEOS DOMICILIO FISCAL ELECTRONICO.csv","a")
        ERROR.write(cuits + ";" + " - CLAVE FISCAL ERRONEA O ERROR" + "\n")   
        
            
            
            
