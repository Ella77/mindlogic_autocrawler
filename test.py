from selenium import webdriver
from selenium.webdriver.chrome.options import Options




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
driver.get('http://www.google.com')
print('test')
driver.close()