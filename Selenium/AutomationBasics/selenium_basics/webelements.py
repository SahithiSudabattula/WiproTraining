import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service



#Start Driver
driver = webdriver.Edge()   #service=Service('../resources/msedgedriver.exe')
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(1)

#TextInput
text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

#Password
password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")


#TextArea
textarea_input = driver.find_element(By.NAME, "my-textarea")
textarea_input.clear()
textarea_input.send_keys("This is a sample message")

#CheckBox
checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()

#RadioButton
radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

#DropDown
dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()

#DropDown(DataList) -Multiselect
multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys('New York')

#FileUpload
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys("C:\\Wipro Training\\Selenium\\AutomationBasics\\selenium_basics\\waits.py")

#RangeSlider
range_slider = driver.find_element(By.NAME, "my-range")
driver.execute_script("arguments[0].value=10;",range_slider) #set slider value

#ColourPicker
colour_picker = driver.find_element(By.NAME, "my-colors")
colour_picker.send_keys("#00ff00")  #green

#DatePicker
date_input = driver.find_element(By.NAME, "my-date")
date_input.send_keys("2025-12-25")

#SubmitButton
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(20)
submit_btn.click()


time.sleep(5)
driver.quit()






