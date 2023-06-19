from selenium import webdriver
import yagmail
import os
import time
from datetime import datetime as dt

def get_driver():
#   set to make browsing easily\
  
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")


  driver = webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver

def send_email(amount):
  sender = 'kunalrai67890@gmail.com'

  reciver = 'kunalatpython@gmail.com'

  subject = "This is the subject"

  contents = f"""
  The price has moved by {amount}
  """


  yag = yagmail.SMTP(user=sender,  password=os.getenv("password"))

  yag.send(to=reciver, subject=subject, contents=contents, )


def clean_text(text):
  """ Extract only temperature from text"""
  output = float(text.split(" ")[0])
  return output

def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath", value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
  price =  clean_text(element.text)

  if price < (-0.10):
    send_email(price)
  

 
while True:
    now = dt.now()
    if now.hour == 7 and now.minute == 55:   
      main()                                



