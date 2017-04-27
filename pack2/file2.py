from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome("C:\\Users\chetan\Downloads\\chromedriver.exe")
'''driver.set_page_load_timeout(30)'''
driver.get("http://newtours.demoaut.com/")

'''driver.maximize_window()
driver.implicitly_wait(20)'''
driver.find_element_by_link_text("REGISTER").click()
driver.find_element_by_name("firstName").send_keys("SFIRST")
driver.find_element_by_name("lastName").send_keys("USER")
driver.find_element_by_name("phone").send_keys("9945966577")
driver.find_element_by_name("userName").send_keys("rfchetan@gmail.com")

select = Select(driver.find_element_by_name("country"))

# select by visible text
select.select_by_index('6')



driver.quit()









