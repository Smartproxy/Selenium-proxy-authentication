from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
from extension import proxies

username = 'your_username'
password = 'your_password'
endpoint = 'gate.smartproxy.com'
port = '7000'
website = 'https://www.ipinfo.io/ip'

chrome_options = webdriver.ChromeOptions()

proxies_extension = proxies(username, password, endpoint, port)

chrome_options.add_extension(proxies_extension)

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
chrome.get(website)
