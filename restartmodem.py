import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.PhantomJS()

username = "admin"
password = "%0|F?H@f!berhO3e"

def restartModem():
    while(1):
        try:
            driver.delete_all_cookies()
            driver.switch_to.default_content
            driver.get("http://192.168.1.1")
            driver.switch_to.frame(1)
            driver.find_element_by_id("User").send_keys(username)
            driver.find_element_by_id("Passwd").send_keys(password)
            driver.find_element_by_id("submit").click()
            driver.refresh()
            driver.switch_to.frame(1)
            management = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Management")))
            driver.execute_script("arguments[0].click();", management)
            driver.execute_script("arguments[0].click();", driver.find_element_by_id("Device Management"))
            driver.execute_script("arguments[0].click();", driver.find_element_by_css_selector(".sub2Menu:nth-child(6) > div"))
            driver.switch_to.frame(0)
            driver.find_element_by_id("reboot_apply").click()
            driver.switch_to.alert.accept()
            break
        except KeyboardInterrupt:
            raise(KeyboardInterrupt)
        except:
            time.sleep(60)
    #driver.execute_script("window.confirm = function(){return true;}")

def main():
    restartModem()

if __name__ == '__main__':
    main()
