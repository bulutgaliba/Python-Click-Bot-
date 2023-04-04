from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

button = driver.find_element_by_xpath("//button[@id='myButton']")
button.click()

driver.quit()
