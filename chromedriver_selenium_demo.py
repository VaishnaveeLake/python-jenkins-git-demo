# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:33:38 2021

@author: VaishnaveeLake
"""

from selenium import webdriver

class ChromeDriverDemo:
    def test(self):
        driver=webdriver.Chrome(executable_path="C:\\NewDevopsWorkspace\\Devops\\devopsjan2021\\java-selenium-driver-demo\\src\\main\\resources\\chromedriver.exe")
        driver.get("http://www.google.com")
        searchElememt=driver.find_element_by_name("q")
        searchElememt.send_keys("ibm")
        searchElememt.submit()
chromedriverdemo= ChromeDriverDemo()
chromedriverdemo.test()
       