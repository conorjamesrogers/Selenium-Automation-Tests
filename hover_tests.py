from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time




def click_tests(element):
        element.click()






def hover_tests(driver):

        # <name>:
    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"

    # This 'By.<name>' can also be avoided by using keywords:
    # find_element_by_id
    # find_element_by_name
    # find_element_by_xpath
    # find_element_by_link_text
    # find_element_by_partial_link_text
    # find_element_by_tag_name
    # find_element_by_class_name
    # find_element_by_css_selector

    # Elements or a single element will be selected based on the (s) plural

    # these select the element I want to test, the banner, both lines 24-25 select the same group
    header_ul= driver.find_element(By.XPATH,"//*[@id='head']")
    # header_ul= chr_driver.find_element_by_class_name('header--links')
    
    # grabs list of elements using 'By.<name>':
    header_list=header_ul.find_elements(By.TAG_NAME,'li')



    # Hover Over Test
    print(header_list)
    for li in header_list:
        print("HoverTest On: " + li.text + " button")
        try:
            ActionChains(driver).move_to_element(li).perform()
            time.sleep(1)
            # driver.implicitly_wait(10)
        except:
            driver.close()
        
   


