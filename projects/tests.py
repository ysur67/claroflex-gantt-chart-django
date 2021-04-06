"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""

import time
from django.test import TestCase
from django.test import LiveServerTestCase
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from unittest import skip




#binary = FirefoxBinary("C:\'Program Files (x86)'\'Mozilla Firefox'\firefox.exe") 
#browser = WebDriver.Firefox(firefox_binary=binary)


class CreateContactIntegrationTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        #cls.selenium = WebDriver()
        cls.driver = webdriver.Chrome(r'C:\Project\chromedriver.exe')
        cls.driver.get('http://127.0.0.1:8000/')
        super(CreateContactIntegrationTest,cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        #cls.selenium.quit()
        super(CreateContactIntegrationTest,cls).tearDownClass()
        
    @skip("Don't want to test")
    def test_login(self):
                
        #self.selenium.get('%s/login' % (self.live_server_url,))
        #self.driver.get('http://127.0.0.1:8000/')
                
        #self.selenium.find_element_by_id('id_username').send_keys("admin")
        time.sleep(5) # Let the user actually see something!
        search_box = self.driver.find_element_by_name('username')
        search_box.send_keys('admin')
        #self.selenium.find_element_by_id('id_password').send_keys("adminadmin")
        search_box = self.driver.find_element_by_id('id_password').send_keys("adminadmin")
        #search_box.submit() 
                
        #self.selenium.find_element_by_xpath("//input[@type='submit']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
                
        #self.assertEqual(Contact.objects.all()[0].login_form, 'admin')
        
    def test_create_project(self):
        
        #time.sleep(3)
        search_box = self.driver.find_element_by_name('username')
        search_box.send_keys('admin')
        search_box = self.driver.find_element_by_id('id_password').send_keys("adminadmin")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        
        search_box = self.driver.find_element_by_xpath('//a[@href="/projects/1/"]').click()
        search_box = self.driver.find_element_by_id('task_desc_1').clear()
        search_box = self.driver.find_element_by_xpath("//textarea[@id='task_desc_1']").send_keys("Купить семена")
        search_box = self.driver.find_element_by_xpath('//div[@class="btn_cont"]').click()
        time.sleep(3)
        search_box = self.driver.find_element_by_xpath('//div[@class="ea_close_result"]').click()
        search_box = self.driver.find_element_by_id('add_project_btn').click()
        message = self.driver.find_element_by_xpath('//div[@class="error_box"]').text
        print (message)
        self.assertEqual(message, "Это поле не может быть пустым.")
        
        
#class SimpleTest(TestCase):
    #def test_basic_addition(self):
       # """
        #Tests that 1 + 1 always equals 2.
        #"""
        #self.assertEqual("Это поле не может быть пустым.", message)