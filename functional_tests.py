from selenium import webdriver
import unittest
import time

# Create your tests here.
class NewVisitorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_main_site(self):  
        self.browser.get('http://127.0.0.1:8000')   
        self.assertIn('Główna', self.browser.page_source)

    def test_polls_site(self):  
        self.browser.get('http://127.0.0.1:8000/polls')   
        self.assertIn('Dzień dobry', self.browser.page_source)
                

if __name__ == '__main__':
    unittest.main()