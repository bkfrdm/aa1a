import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




class TestsConsumerSide(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def table_membership_test(self, *data, table_id='id_table_storage_search'):
        table = self.browser.find_element_by_id(table_id)
        rows = table.find_elements_by_tag_name('tr')
        for target in data:
            self.assertIn(target, [row.text for row in rows])

    def form_data_enter(self, form, data, sleep_time=1):
        form.send_keys(data)
        form.send_keys(Keys.ENTER)
        time.sleep(1)

    def test_storage_page(self):
        # gets to home page
        self.browser.get(self.live_server_url)

        # sees a greeting header
        header = self.browser.find_element_by_tag_name('h1').text.lower()
        self.assertIn('aa1a', header)

        # sees a search form
        form = self.browser.find_element_by_id('id_storage_search')
        self.assertEqual(form.get_attribute('placeholder'), 'Enter supplier\'s name')
        # enters a valid id and submits
        self.form_data_enter(form, 'aa1a')
        # page now shows supplier info
        self.table_membership_test('1: aa1a')

        # Comsumer enters 2nd. Page now shows 2 supplier info
        form = self.browser.find_element_by_id('id_storage_search')
        self.form_data_enter(form, 'bb2b')
        self.table_membership_test('1: aa1a', '2: bb2b')





        self.fail('Test fails here')


if __name__ == "__main__":
    unittest.main(verbosity=2)
