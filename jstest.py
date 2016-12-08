from selenium import webdriver
import  time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
#time.sleep(3)
try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"loadedButton")))
finally:
    pagehtml=driver.page_source
    bsobj=BeautifulSoup(pagehtml,'lxml')
    print(bsobj.find(id='content').get_text())
    #print(driver.find_element_by_id('content').text)
    driver.close()