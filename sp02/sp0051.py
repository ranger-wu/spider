from selenium import webdriver
import time

url = 'http://www.bing.com'
wb = webdriver.Firefox()
wb.get(url)
wb.save_screenshot('bing.png')
wb.find_element_by_id('sb_form_q').send_keys('滁州学院')
wb.find_element_by_id('sb_form_q').click()
print(wb.page_source)
time.sleep(3)
wb.quit()