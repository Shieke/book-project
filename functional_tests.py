"""
* - - - - - - - - - - - - - - - - - - - - - - - - - *
|                 FUNCTIONAL  TESTS                 |
|                 FOR BOOK PROJECTS                 |
|                                                   |
|    AUTHOR: COLLEEN BERNUM     DATE: 10/04/2016    |
|    FILENAME: functional_tests.py                  |
|                                                   |
* - - - - - - - - - - - - - - - - - - - - - - - - - *

"""

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Colleen has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # She is invited to enter a to-do item straight away

        # She types "Buy notebook" into a text box (Colleen's hobby
        # is writing)
        
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy notebook" as an item in a to-do list
    
        # There is still a text box inviting her to add another item. She
        # enters "Use notebook to write a story" (Colleen is very methodical)

        # The page updates again, and now shows both items on her list

        # Colleen wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect

        # She visits the URL - her to-do list is still there.
    
        # Satisfied, she goes back to sleep

if __name__ == '__main__':
        unittest.main(warnings='ignore')
