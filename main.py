import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()
    #opening the url
    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()
 
    chrome_driver.find_element_by_name("li1").click()
    chrome_driver.find_element_by_name("li2").click()
 
    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title
 
    sample_text = "Testing"
    #box with the id
    email_text_field = chrome_driver.find_element_by_id("sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)
 
    chrome_driver.find_element_by_id("addbutton").click()
    sleep(5)
 
    output_str = chrome_driver.find_element_by_name("li6").text
    sys.stderr.write(output_str)
    
    sleep(2)
    chrome_driver.close()