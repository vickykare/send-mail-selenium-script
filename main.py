from selenium import webdriver
import time
driver = webdriver.Chrome(
    executable_path=r"C:\Users\User\Desktop\chromedriver.exe")  # chromedriver path

try:
    driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
except Exception as e:
    print(e)

sender = "sender_gmail"
sender_password = "sender_gmail_password"
to = "sendto@gmail.com"
subject = "This is for testing"
description = "This is description"


# find email input box write email

email_box = driver.find_element_by_id('identifierId')
email_box.send_keys(sender)
button = driver.find_element_by_class_name('RveJvd')
button.click()
print("Email entered successfully!")
time.sleep(2)


# find password box and write password
password_box = driver.find_element_by_class_name('zHQkBf')
password_box.send_keys(sender_password)
button = driver.find_element_by_class_name('RveJvd')
button.click()
print("Password entered successfully!")
time.sleep(3)

# get compose button and click on it
driver.find_element_by_xpath("//div[@class='z0']//div[@role='button']").click()
time.sleep(3)

# to the someone
to_box = driver.find_element_by_id(':pj')
to_box.send_keys(to)
time.sleep(1)

# write subject
subject_box = driver.find_element_by_id(':p1')
subject_box.send_keys(subject)
time.sleep(1)

# description
description_box = driver.find_element_by_id(':q6')
description_box.send_keys(description)
time.sleep(1)

# send

send_button = driver.find_element_by_id(':or')
send_button.click()
